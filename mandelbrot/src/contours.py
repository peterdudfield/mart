import cv2
import numpy as np


def mask_to_coord(arr,idx,threshold_area=1000,include_holes=False,smooth_len=5):
    """
    Function to change mask into list of coordinates
    param arr: massk array, numpy (HxW) array, unit8
    param idx: idx in mask that coordinates will be made from
    param threshold_area: 
    return: List of coordinates of outline of area
    """
    
    #make black and white image array of area wanted
    bw_img = np.zeros_like(arr)
    bw_img[arr==idx] = 255
    
    #smooth image
    kernel = np.ones((smooth_len,smooth_len),np.uint8) #square image kernel used for smoothing
    bw_img_smooth = cv2.erode(bw_img, kernel,iterations = 1) #refines all edges in the binary image
     
    #get contours
    t,contours_all, hierarchy = cv2.findContours(bw_img_smooth,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find contours with simple approximation
    
    #areas = [] #list to hold all areas
    contour=[]
    #print(hierarchy)
    for i in range(len(contours_all)):
        contour_all = contours_all[i]
        ar = cv2.contourArea(contour_all)
        if ar>threshold_area:
            if include_holes:
                contour.append(contour_all[:,0,:])
            else:
                if len(hierarchy)==0 or hierarchy[0][i][3]==-1:
                    contour.append(contour_all[:,0,:])
            
    return contour

def coord_to_mask(contours,size,value=255):
    """
    Function to change list of coordinates into mask
    param contours: List of coordinates of outline of area
    param size: (h,w) of return mask
    param value: value of area inside contour
    return mask of filled in by contours
    """
    
    mask = np.zeros(size).astype('int32')
    mask = cv2.fillPoly(mask,contours,255).astype('uint8')
    
    return mask
