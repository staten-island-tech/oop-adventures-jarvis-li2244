import json
def file_modify(file_name, mode, content ):
    with open(f'{file_name}.json')  as infile:
        file = json.load(infile)
