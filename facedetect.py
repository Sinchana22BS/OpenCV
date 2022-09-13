import cv2
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("img4.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(gray,1.06,5)
#scale factor is the rotation of their corresponding side
#scale factor of 1.06 means to decreases the shape value by 3% until the faces find
#minimum neighbour means how much minimum distanceyour webcam find your face

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("Face detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()