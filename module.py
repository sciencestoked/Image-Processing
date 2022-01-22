import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2


def bw_3_channel_using_thresh(img_arr,thresh):
    ro,col,channl=img_arr.shape[:]
    blank_img=np.zeros((ro,col,channl))
    
    for r in range(ro):
        for c in range(col):
            
            curr_px_color=img_arr[r][c]

            if ( ( (curr_px_color[0] > thresh)and(curr_px_color[1] > thresh) )and(curr_px_color[2] > thresh) ):

                blank_img[r][c][:]=255

    return blank_img




def single_channel_using_thresh(img_arr,thresh):
    ro,col,channl=img_arr.shape[:]
    blank_img=np.zeros((ro,col))
    
    for r in range(ro):
        for c in range(col):
            
            curr_px_color=img_arr[r][c]

            if ( ( (curr_px_color[0] > thresh)and(curr_px_color[1] > thresh) )and(curr_px_color[2] > thresh) ):

                blank_img[r][c]=1

    return blank_img





def perspect_transform(img, src, dst):
  matrx=cv2.getPerspectiveTransform(src,dst)
  warped_img = cv2.warpPerspective(img , matrx , (img.shape[1],img.shape[0]))
  return warped_img
