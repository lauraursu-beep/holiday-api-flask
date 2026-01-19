from json2html import json2html
import json 

def convert_json_table():
    with open('file.json','r') as file:
        data = json.load(file)
    
    table_html = json2html.convert(json = data)
    with open('method_2.html','w') as file:
        file.write(table_html)
    
    return("HTML table generated") 


