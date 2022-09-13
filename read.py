import cv2
img = cv2.imread("img1.jpg")
cv2.imshow("How to read an image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()