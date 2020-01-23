import requests
import json

Columns={
"Item":["item_code","item_group","stock_uom"],
"Item Barcode":[],
"Item Reorder":["warehouse","warehouse_reorder_level","material_request_type"],
"UOM Conversion Detail":[],
"Item Variant Attribute":["attribute"],
"Item Default":["company"],
"Item Supplier":[],
"Item Customer Detail":["ref_code"],
"Item Tax":["item_tax_template"],
"Website Item Group":["item_group"],
"Item Website Specification":[]
}

parameters = {
'doctype': 'Item',
'parent_doctype': 'Item',
'select_columns': Columns,
'with_data': 0,
'all_doctypes': 'true',
'file_type': 'CSV',
'template': 'true',
'csrf_token': '139b6a77fc452e8598cad1f41784b2b13b35c6ce8c35bb0662b06778'
}

headers = {
    'Authorization': "token <api_key>:<api_secret>"
}

response=requests.get("http://0.0.0.0:8000/api/method/frappe.core.doctype.user.user.generate_keys?user=Administrator")
print(response.status_code)

response = requests.get("http://localhost:8000/api/method/frappe.core.doctype.data_export.exporter.export_data?usr=Administrator&pwd=admin",params=parameters)
print(response.status_code)