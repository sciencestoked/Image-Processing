import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from My_Module import module
import cv2


image = mpimg.imread('/home/sciencestoked/Robotics/sample2.jpg')

plt.imshow(image)
plt.show()

# for channeling out the red channel
red_channel = np.copy(image)
red_channel[:,:,[1,2]]=0

# for channeling out the green channel
green_channel = np.copy(image)
green_channel[:,:,[0,2]]=0

# for channeling out the blue channel
blue_channel = np.copy(image)
blue_channel[:,:,[0,1]]=0


src = np.float32([[14,140],[300,139],[200,96],[119,95]])
dst = np.float32([[20,140],[70,140],[70,90],[20,90]])


tranformed_color_image      = module.perspect_transform(image,src,dst)

bw_transformed_image        = module.bw_3_channel_using_thresh(tranformed_color_image,150)

bw_image                    = module.bw_3_channel_using_thresh(image,150)

singl_chnnl_img             = module.single_channel_using_thresh(image,150)

singl_chnnl_transformed_img = module.single_channel_using_thresh(tranformed_color_image,150)


plt.imshow(bw_image)
plt.show()

plt.imshow(tranformed_color_image)
plt.show()

plt.imshow(bw_transformed_image)
plt.show()

plt.imshow(singl_chnnl_img)
plt.show()

plt.imshow(singl_chnnl_transformed_img)
plt.show()



xpos,ypos = singl_chnnl_transformed_img.nonzero()

plt.plot(xpos,ypos,".")
plt.xlim(0,320)
plt.ylim(0,160)
plt.show()










