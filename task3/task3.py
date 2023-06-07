import sys
import json

args = sys.argv

for item in args:
    if 'tests.json' in item:  tests = item
    if 'values.json' in item:  values = item

with open(tests, 'r', encoding='utf-8') as f:
    tests_json = json.load(f)

with open(values, 'r', encoding='utf-8') as f:
    values_json = json.load(f)

def getReport(tests, values):
    for test in tests:
        if 'values' in test:
            getReport(test['values'], values)    
        for value in values['values']:
            if test['id'] == value['id'] and 'value' in test:
                test['value'] = value['value']
             

getReport(tests_json['tests'], values_json)

with open('report.json', 'w', encoding='utf-8') as jsonf: 
    jsonString = json.dumps(tests_json, indent=4, ensure_ascii=False)
    jsonf.write(jsonString)
