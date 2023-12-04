# Name: An Tran, Morgan Miller, Duc Name Le, Johnny Liu 
# email: tran2a3@mail.uc.edu, mille8m9@mail.uc.edu, le2dc@mail.uc.edu, liu4j4@mail.uc.edu
# Assignment Title: Final Project
# Due Date: 12/01/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: 
# Citations: https://stackoverflow.com/questions/9803784/basic-encrypt-and-decrypt-function
# Anything else that's relevant:

# decryptMovie.py 

import base64
import json
from cryptography.fernet import Fernet

def decrypt_movie_title():

    # the provided decryption key
    decryption_key = "bTkQSmlNDEfiNJCuSuyUq0PPtiH-DDUwiGLCjlVw6uY="
    # create a Fernet, since the key is base64
    fernet_key = Fernet(decryption_key)
    
    # encrypted messages
    encrypted_messages_file = "TeamsAndEncryptedMessagesForDistribution.json"
    # read the file and find McGee
    with open(encrypted_messages_file, 'r') as file:
        encrypted_file = json.load(file)['McGee'][0]
    
    # decrypt the message     
    decrypted_message = fernet_key.decrypt(encrypted_file.encode())
    return(decrypted_message.decode())
decrypted_message = decrypt_movie_title()

print(f"Decrypted Movie Title: ", decrypted_message)


