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
    def file_modification(file, values, content_change):
        try:
            with open(file, 'r+') as filecabinet:
                filecab = json.load(filecabinet)
            current_level = filecab
            for i in range(len(values)-1):
                current_level = current_level[values[i]]
            current_level[values[-1]] = content_change
            with open(file, 'w+') as outfile:
                outfile.write(json.dumps(filecab, indent=2))
        except ValueError:
            print("error")
#mke sure to specify the erorr otherwise itll be hard debugging
mod = Modified_Functions
