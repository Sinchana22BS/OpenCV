import cv2
gray = cv2.imread("img1.jpg",0)        # 0 means grayscale img & 1 is the rgb img
cv2.imshow("My grayscale image",gray)

cv2.waitKey(0)
cv2.destroyAllWindows()