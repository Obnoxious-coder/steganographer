import cv2
import numpy as np

def encode(filename,binary_str):
    binary_str=binary_str +'11111111111111'
    img=cv2.imread(filename)
    i=0
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
                if i<len(binary_str):
                    if(img[x][y][0]%2==1 and binary_str[i]=='0'):
                        img[x][y][0]=img[x][y][0]&~1
                    elif(img[x][y][0]%2==0 and binary_str[i]=='1'):
                        img[x][y][0]=img[x][y][0]|1
                    i=i+1
                else:
                    break
    filename1 = filename.split('.')[0]+"_con."+filename.split('.')[1]
    cv2.imwrite(filename1,img)
    print(img)
    return filename1

def decode(filename):
    img=cv2.imread(filename)
    bin_str=''
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
                if bin_str[-14:]=='11111111111111':
                    break
                if img[x][y][0]%2==0:
                    bin_str+='0'
                else:
                    bin_str+='1'

    return bin_str



