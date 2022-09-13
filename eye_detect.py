import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
img = cv2.imread("img3.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.06,5)
for x,y,w,h in faces:
    roi_gray = gray[y:y+h,x:x+w]
    roi_img = img[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for ex,ey,ew,eh in eyes:
        cv2.rectangle(roi_img,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
cv2.imshow("Eye detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()