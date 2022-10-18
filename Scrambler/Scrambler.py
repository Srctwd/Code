from PIL import Image, ImageColor
import numpy as np
import random
import sys

#Initialization
img = Image.open("image.png")
na = np.array(img)
pixel_number = len(na)*len(na[0])
pixel_list = []
for i in range(0, pixel_number):
    pixel_list.append(i)
key_list = []
    
def encrypt():
    yee=0
    print("Image is", pixel_number, "Pixels") 
    print("Encrypting.", end="")
    sys.stdout.flush()
    for i in range(0, len(na)):
        for j in range(0, len(na[i])):
            if i*len(na[i])+j in pixel_list:
                pixel_list.remove(i*len(na[i])+j)
                if len(pixel_list) > 0:
                    rc = random.choice(pixel_list)
                    while rc == i*len(na[i])+j:
                        rc = random.choice(pixel_list)
                    pixel_list.remove(rc)
                rc_pos1 = rc//len(na[i])
                rc_pos2 = rc%len(na[i])
                var = na[i][j].copy()
                na[i][j] = na[rc_pos1][rc_pos2]
                na[rc_pos1][rc_pos2] = var
                key_list.append(rc)
                
        #a way to see it's not stuck
        if yee > len(na)/9: 
            yee = 0
            print(".", end="")
            sys.stdout.flush()
        yee = yee + 1
            
def decrypt():
    print(key_list)
    
    
    
usr_input = input("e for encrypt, d for decrypt ")
if usr_input == "e" or "E":
    encrypt()
    
new_img = Image.fromarray(na)
new_img.save("hello.png", quality=100)
