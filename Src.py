!git clone https://github.com/udacity/CarND-LaneLines-P1.git
%cd CarND-LaneLines-P1
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2 
import math
%matplotlib inline

# Helper Functions

def grayscale(img):
   return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices):
  mask = np.zeros_like(img)  
  if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
  else:
        ignore_mask_color = 255
  cv2.fillPoly(mask, [vertices], ignore_mask_color)
  masked_image = cv2.bitwise_and(img, mask)
  return masked_image

