from __future__ import unicode_literals, absolute_import, print_function
from pathlib import Path
import click
import csv
import json, os, sys, subprocess
from distutils.spawn import find_executable
import frappe
from frappe.commands import pass_context, get_site
from frappe.utils import update_progress_bar, get_bench_path
from frappe.utils.response import json_handler
from coverage import Coverage
import cProfile, pstats
from six import StringIO
from frappe.core.doctype.data_import import importer
from frappe.utils.csvutils import read_csv_content

def transformFile(masterFilePath=None) :
    from frappe.utils.csvutils import read_csv_content
    if isValidPath("/"+masterFilePath):
        jsonData=getJsonMap()
        for key in jsonData:
            templateRows=getTemplate(key)
            mainFileData=getMainData("/"+masterFilePath)
            mappedData=getMappedData(templateRows,mainFileData,jsonData[key])
            saveTemplateWithData(key,mappedData)


def isValidPath(*args):
    try:
        for arg in args:
            if not(os.path.exists(arg)):
                print("The specified path",arg,"doesn't exist. Please provide a valid path.")
                return False
    except:
        return False
    return True

def getMappedData(templateContent,mainContent,jsonMap):
    templateColumn=templateContent[15]
    dataColumn=mainContent.pop(0)
    listArray=[]
    for index,val in enumerate(mainContent):
        listArray=[]
        for i in templateColumn:
            listArray.append(None)
        for jsonData in jsonMap:
            try:
                if(not (val[dataColumn.index(jsonData["source"])] and val[dataColumn.index(jsonData["source"])].strip())):
                    listArray[templateColumn.index(jsonData["destination"])]=jsonData["constant"]
                else:
                    listArray[templateColumn.index(jsonData["destination"])]=val[dataColumn.index(jsonData["source"])]
            except ValueError:
                listArray[templateColumn.index(jsonData["destination"])]=jsonData["constant"]
        templateContent.append(listArray)
    return templateContent

def getJsonMap():
    jsonMapPath = Path(__file__).parent / "json_maps/item-data.json"
    with open(jsonMapPath) as jsonfile:
        jsonData = json.load(jsonfile)
    return jsonData

def getTemplate(doctypeName):
    templatePath=Path(__file__).parent / "data/Item-template.csv"
    with open(templatePath,'r') as tempcsvfile:
        templateContent=read_csv_content(tempcsvfile.read())
    return templateContent


def getMainData(fileLocation):
    with open(fileLocation,'r') as csvFile:
        fileContent=read_csv_content(csvFile.read())
    return fileContent

def saveTemplateWithData(fileName,mappedData):
    with open(Path(__file__).parent / ("output/"+str(fileName)+".csv"), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(mappedData)
    print("Successfully created the file at ",Path(__file__).parent / ("output/"+str(fileName)+".csv"))






	