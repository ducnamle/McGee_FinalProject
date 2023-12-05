#Name: Duc Nam Le, An Tran, Morgan Miller, Johnny Liu
#email: mille8m9@mail.uc.edu, tran2a3@mail.uc.edu, liu4j4@mail.uc.edu, le2dc@mail.uc.edu
#Assignment Title: Final Project
#Due Date: December 7th, 2023
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Decrypt the location for team McGee
#Citations: 
#Anything else that's relevant:

# main.py

from LocationPackage.DecryptLocation import *
from moviePackage.decryptMovie import *
from picturePackage.loadPicture import *

if __name__ == "__main__":
    
    decrypt_location()
    
    decrypt_movie_title()
    
    rotate_and_display(r"../filesPackage/McGee_Crosley.png")