#Name: Duc Nam Le, An Tran, Morgan Miller, Johnny Liu
#email: mille8m9@mail.uc.edu, tran2a3@mail.uc.edu, liu4j4@mail.uc.edu, le2dc@mail.uc.edu
#Assignment Title: Final Project
#Due Date: December 7th, 2023
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Loading picture into project
#Citations: https://stackoverflow.com/questions/48729915/how-to-read-images-into-a-script-without-using-using-imageio-or-scikit-image
#Anything else that's relevant:

#picture
#code will load picture 

from PIL import Image


def rotate_and_display(image_path):
    original_image = Image.open(image_path)
    rotated_image = original_image.transpose(Image.ROTATE_270)
    rotated_image.show()

# Use this code in the main module to display the image: 
# rotate_and_display("McGee_Crosley.png")