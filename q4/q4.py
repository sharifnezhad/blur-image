import cv2
import numpy as np
import math

def custom_array(number):
    filter=np.ones((number,number))/ math.pow(number,2)
    return filter
noise_image=cv2.imread('chris2.jpg',0)

output=np.zeros(noise_image.shape)

number=int(input('number:'))
filter=custom_array(number)
num=(number-1)//2
row,col=noise_image.shape
for i in range(num,row-num):
    for j in range(num,col-num):
            small_image=noise_image[i-(num):i+(num+1),j-(num):j+(num+1)]
            output[i,j]=np.sum(small_image*filter)

cv2.imwrite('res-15X15.jpg',output)
