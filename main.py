import json
import sys
import inflect
from utils import get_v_k, check_type, number_2_word
import pprint


p = inflect.engine()


def create_json(file_name, output_name):
    num = 1
    output = {}
    with open(f'data/{file_name}.json', 'r') as f:
        data = json.load(f)
    message = data.get("message", {})
    for i in get_v_k(message):
        value_type = check_type(i[1])
        output[f"key_{p.number_to_words(num)}"] = {"type": value_type,
                                                "tag": "",
                                                "description": "",
                                                "required": False
                                                }
        num += 1    
    with open(f'schema/{output_name}.json', 'w') as json_file:
        json.dump(output, json_file, indent = 4)






create_json(sys.argv[1], sys.argv[2])