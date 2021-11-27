import cv2
import numpy as np

noise_image=cv2.imread('flower_input.jpg',0)

output=np.zeros(noise_image.shape)

filter=np.ones((15,15))/225

row,col=noise_image.shape
flower=[]
for i in range(12,row-12):
    for j in range(12,col-12):
        if noise_image[i,j]<220:
            small_image=noise_image[i-7:i+8,j-7:j+8]
            output[i,j]=np.sum(small_image*filter)
        else:
            output[i,j]=255
# flower_list=np.array(flower)
# mask_flower=np.zeros(noise_image.shape,dtype='uint8')
# cv2.drawContours(mask_flower,[flower_list],-1,(255,255,255),-1)
# mask_flower=mask_flower/255
# result=noise_image*mask_flower
# for x,y,w,h in noise_image:
#     print(x,y,w,h)
#     exit()
# result = img_as_float(result)
# noise_image = img_as_float(noise_image)

# noise_image[:,:]*=1-result[:,:]
# cv2.imwrite('res.jpg',noise_image)
cv2.imwrite('res.jpg',output)
