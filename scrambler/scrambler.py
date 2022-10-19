from PIL import Image, ImageColor
import numpy as np
import random
import sys

def main():
    #inputs still need validation and sanitization
    usr_input = input("file to load: ")
    img = Image.open(usr_input)
    na = np.array(img)
    pixel_number = len(na)*len(na[0])
    pixel_list = []
    for i in range(0, pixel_number):
        pixel_list.append(i)
    key_list = []
    usr_input2 = input("output filename: ")
    write_encrypt(encrypt(na, pixel_number, pixel_list, key_list), usr_input2)
    
    
def encrypt(na, pixel_number, pixel_list, key_list):
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
                
        #a way to see if it's not stuck
        if yee > len(na)/9: 
            yee = 0
            print(".", end="")
            sys.stdout.flush()
        yee = yee + 1
    return na
        
def write_encrypt(image_array, output_name):
    new_img = Image.fromarray(image_array)
    new_img.save(output_name, quality=100)
            
def decrypt():
    print(key_list)
    
    
if __name__ == "__main__":
        main()
