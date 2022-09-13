import cv2
img = cv2.imread("img2.jpg")        
resize = cv2.resize(img,(int(img.shape[1]*2),int(img.shape[0]*2)))

cv2.imshow("Resized image",resize)

cv2.waitKey(0)
cv2.destroyAllWindows()
