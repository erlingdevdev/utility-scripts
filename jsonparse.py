import json

def parse_json(file):
    with open("test.json", 'r') as f: 
        parsed_json = json.load(f)
        for i in parsed_json:
            print(i)
        print(json.dumps(parsed_json, indent = 4))


