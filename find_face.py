import os
import cv2
import time


#  modules for opencv  https://github.com/opencv/opencv/tree/master/data/haarcascades

def getphoto(filename, cameranumber):
    cap = cv2.VideoCapture(cameranumber)
    for i in range(5):
        cap.read()
     
    ret, frame = cap.read()
    face_cascade = cv2.CascadeClassifier(os.getcwd()+'/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor= 1.1, minNeighbors= 5, minSize=(10, 10))
    faces_detected = format(len(faces))
    cv2.imwrite(filename, frame)  
    cap.release()  
    
    return(faces_detected)



filename = os.getcwd()+'/photos/'+time.ctime().replace(':','_')+'.png'
print(filename)

facescount = getphoto(filename, 0)
print('Faces find : ' + facescount)
