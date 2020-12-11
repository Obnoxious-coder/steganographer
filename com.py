import cv2
import numpy as np

raw_text="Hello my name is Jonathan."
import convert,image_encoder
raw_binary=convert.text_to_binary(raw_text)

print(image_encoder.encode("lena.jpg",raw_binary))
img=cv2.imread("lena.jpg")
img2=cv2.imread("lena_con.jpg")

print(img2)


extracted_data=image_encoder.decode("lena_con.jpg")
print(convert.binary_to_text(extracted_data))

