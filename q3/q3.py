import cv2
import numpy as np

noise_image=cv2.imread('building.tif',0)

output=np.zeros(noise_image.shape)

filter=np.array([[-1,-1,1],[0,0,0],[1,1,1]])

row,col=noise_image.shape
for i in range(1,row-1):
    for j in range(1,col-1):
            small_image=noise_image[i-1:i+2,j-1:j+2]
            output[i,j]=np.sum(small_image*filter)

cv2.imwrite('res4.jpg',output)
