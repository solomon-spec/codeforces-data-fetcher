import json
def text_to_list():
    array = []
    while True:
        try:
            ip,port,user,pas = input().split(':')

            array.append(f'{user}:{pas}@{ip}:{port}')
            # array.append(input())
        except:
            break
    print(array)


def is_valid_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            parsed_json = json.load(file)  
    except ValueError as e:
        return False
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    return parsed_json


file_path = 'docs/data.txt'
parsed_json = is_valid_json_file(file_path)
if is_valid_json_file(file_path):
    print("The file contains valid JSON.")
    print(parsed_json)
else:
    print("The file does not contain valid JSON.")
