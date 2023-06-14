import cv2
import os
# fix bug cannot read cv2.imread : file integrity. Ganti dengan direktori folder ini
os.chdir(r"D:\Kerja\Timedoor\Bahan Ajar\Coding Camp 2023\Coding Files\M1_Intro")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Manusia', (x, y),

        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)
    cv2.imshow('Detect Face', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()