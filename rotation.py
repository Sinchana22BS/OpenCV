import cv2
import numpy as np
img = cv2.imread("img2.jpg")
height = img.shape[0]
width = img.shape[1]
rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),90,0.5) #Here 90 is the degree of rotation & 0.5 is the scaling factor
rotation = cv2.warpAffine(img,rotation_matrix,(width,height))
cv2.imshow("Image rotation",rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()