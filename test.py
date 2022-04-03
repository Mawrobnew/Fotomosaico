#Companies that choose to stitch the images into a photomosaic autonomously are tasked with creating 
#software to “stitch” the images together. Companies may manually pilot their vehicle to any location to 
#take the eight individual images, but the program must “stitch” the images into a photomosaic. 
#Companies that successfully “stitch” the images together autonomously will receive 20 points. 
#Successfully “stitching” the images together autonomously is defined as no input from company 
#members other than taking the images.
import cv2
import glob
import os

#Rename
list_rename = glob.glob('*.jpg')
for i in range(len(list_rename)):
    os.rename(list_rename[i],f"{i}.jpg")
    
#Read
images={}
for i in range(8): # 8 images
    images[i]=cv2.imread(f"{i}.jpg") #  # of Images
    #Resize
    images[i]=cv2.resize(images[i],(200,200))
       
#Stack 
stack1=cv2.hconcat([images[0],images[1],images[2],images[3]])
stack2=cv2.hconcat([images[4],images[5],images[6],images[7]])
stack3=cv2.vconcat([stack1,stack2])

#Show
cv2.imshow("Foto",stack3)
#Download
cv2.imwrite('image.jpg',stack3)
cv2.waitKey(0)
cv2.destroyAllWindows