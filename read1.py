import cv2
img = cv2.imread("img1.jpg")
cv2.imshow("How to read an image",img)
while True:
    if cv2.waitKey(1)==13:      # 13 is the ASCII value of enter key
        break
cv2.destroyAllWindows()