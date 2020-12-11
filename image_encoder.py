import cv2
import numpy as np
binary_str="1101000110010111011001101100110111111011011111001110111011000011101101110010111010011110011100000110101011011111101000110111010000111111111111111"
img=cv2.imread("lena.jpg")
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


bin_str=''
for x in range(img.shape[0]):
      for y in range(img.shape[1]):
            if bin_str[-14:]=='11111111111111':
                break
            if img[x][y][0]%2==0:
                bin_str+='0'
            else:
                bin_str+='1'

print(bin_str)



