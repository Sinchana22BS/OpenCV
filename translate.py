import cv2
import numpy as np
img = cv2.imread("img2.jpg")
height = img.shape[0]
width = img.shape[1]
quarter_height, quarter_width = height/4, width/4
T = np.float64([[1,0,quarter_width],[0,1,quarter_height]])
translate = cv2.warpAffine(img,T,(width,height))
cv2.imshow("Image Translation",translate)
cv2.waitKey(0)
cv2.destroyAllWindows()
