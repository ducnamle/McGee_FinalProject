#decrypt the location file

import json

def func_1():
    file_path_1 = "EncryptedGroupHints Fall 2023 Section 001 (1).json"
    file_path_2 = "english-2 (1).txt"


    with open(file_path_1, 'r') as file:
        data_1 = json.load(file)['McGee']
        data_1 = [int(x) for x in data_1]


    with open(file_path_2, 'r') as file:
        lines = file.readlines()
        english_vocab_list = [line.strip() for line in lines]


    #EncryptedGroupHints-Fall-2023-Section-001
    result_1 = ' '.join([english_vocab_list[x] for x in data_1])

    return result_1
    
result_1 = func_1()

result_1