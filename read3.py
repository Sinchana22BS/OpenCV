import cv2
img = cv2.imread("img1.jpg")
cv2.imshow("How to read an image",img)
while True:
    if cv2.waitKey(1)==ord('a'):     #press d to destroy the window
        break
cv2.destroyAllWindows()