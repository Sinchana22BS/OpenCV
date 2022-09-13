import cv2
img = cv2.imread("img2.jpg")        
resize = cv2.resize(img,(600,600))

cv2.imshow("Resized image",resize)

cv2.waitKey(0)
cv2.destroyAllWindows()
