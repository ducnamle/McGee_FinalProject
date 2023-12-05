#Name: Duc Nam Le, An Tran, Morgan Miller, Johnny Liu
#email: mille8m9@mail.uc.edu, tran2a3@mail.uc.edu, liu4j4@mail.uc.edu, le2dc@mail.uc.edu
#Assignment Title: Final Project
#Due Date: December 7th, 2023
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Decrypt the location for team McGee
#Citations: 
#Anything else that's relevant:


#decrypt the location file

import json

def decrypt_location():
    file_path_1 = r"../filesPackage/EncryptedGroupHints Fall 2023 Section 001.json"
    file_path_2 = r"../filesPackage/english-2.txt"


    with open(file_path_1, 'r') as file:
        data_1 = json.load(file)['McGee']
        data_1 = [int(x) for x in data_1]


    with open(file_path_2, 'r') as file:
        lines = file.readlines()
        english_vocab_list = [line.strip() for line in lines]


    #EncryptedGroupHints-Fall-2023-Section-001
    result_1 = ' '.join([english_vocab_list[x] for x in data_1])

    print(result_1)

if __name__ == "__main__":
    decrypt_location()
