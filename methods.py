import json
import time
import sys
class Modified_Functions():
    def timing(func):
        def tim():
            start_time = time.time()
            func()
            time_run = time.time() - start_time
            print(f'{time_run} seconds to run')
        return tim
    def delay_print(s):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
    def proper_input(type):
        data_types = {
            'int':int,
            'str':str,
            'bool':bool,
            'float':float
        }
        while True:
            try:
                anput = input()
                output = data_types.get(type, str)(anput)
                return output
            except:
                print("Enter a valid input please")
    def file_modify(file, value_change, values, modified_content):
        try:
            with open(file) as filing_cabinet:
                data = json.load(filing_cabinet)
            new_data = value_change(data, values, modified_content)
            with open(file, 'w+') as outfile:
                outfile.write(json.dump(new_data, indent=2))
        except:
            print('Error')
    def modifier(info, values, modified_data):
        info[values[0]] = modified_data
        temp_value = info[values[0]]
        print(temp_value, values[0])
Modified_Functions.file_modify('test.json', Modified_Functions.modifier, ['new_value'], 1)
def file_modification(file, value_change, values, content_chance):
    try:
        with open(file, 'r+') as filecabinet:
            filecab = json.load(filecabinet)
        new_data = value_change()
        with open(file, 'w+') as outfile:
            outfile.write(json.dumpm(new_data, indent=2))
    except:
        print("error")
def val_change(data, index):
    new_value = data + index 
    print(new_value)
data = [10, 100]
val_change(data, [0])