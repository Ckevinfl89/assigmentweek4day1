import re

def file_reader():
    with open('regex_test.txt') as file:
        data = file.readlines()
        full_name_pattern = re.compile(r'^[A-Z][a-zA-Z]*(?: [A-Z][a-zA-Z]*)*$')
        for name in data:
            if re.match(full_name_pattern, name) and ' ' in name:
                print(name)
            else:
                print("None")
file_reader()