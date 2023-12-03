#Name: Morgan Miller
#email: mille8m9@mail.uc.edu
#Assignment Title: Final Project
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Loading picture into project
#Citations: https://stackoverflow.com/questions/48729915/how-to-read-images-into-a-script-without-using-using-imageio-or-scikit-image
#Anything else that's relevant:

#picture
#code will load picture 

from PIL import Image
Original_Image = Image.open("McGee_Crosley.png") 
rotated_image1 = Original_Image.transpose(Image.ROTATE_270) 
rotated_image1.show()

