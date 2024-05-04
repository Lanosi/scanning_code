import cv2

img = cv2.imread("dorito.jpg")

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier("ai_faces.xml")

result = faces.detectMultiScale(img,scaleFactor=2, minNeighbors=1)

for (x, y, w, h) in result:
    cv2.rectangle(img,(x,y),(x+w,y+h), (77, 47, 58),thickness=3)

cv2.imshow("Resulr",img)
cv2.waitKey(0)
