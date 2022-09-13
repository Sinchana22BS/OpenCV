import cv2
gray = cv2.imread("img2.jpg",0)        # 0 means grayscale img & 1 is the rgb img
ret,binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.imshow("Binary image",binary)

cv2.waitKey(0)
cv2.destroyAllWindows()