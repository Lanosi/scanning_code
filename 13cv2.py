import cv2

img = cv2.imread("121.jpg")
img = cv2.resize(img,(700,600))

img_optim = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces = cv2.CascadeClassifier("ai_faces.xml")

result = faces.detectMultiScale(img_optim,scaleFactor=1.4, minNeighbors=2)

for (x, y, w, h) in result:
    cv2.rectangle(img,(x,y),(x+w,y+h), (0, 0, 255),thickness=10)

img = cv2.resize(img,(700,600))

cv2.imshow("Resulr",img)
cv2.waitKey(0)
