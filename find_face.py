import cv2
import os
import time

# Функция делающая снимок с веб-камеры 
def getphoto(filename, cameranumber):
    # Включаем по номеру камеру из списка камер
    cap = cv2.VideoCapture(cameranumber)
    # "Прогреваем" камеру, чтобы снимок не был тёмным
    # для прогрева читаем несколько раз видеокадры с камеры
    for i in range(5):
        cap.read()
    # Делаем снимок    
    ret, frame = cap.read()
    # Ищем лица на фото с помощью .xml модуля для opencv
    # различные модули для opencv лежат тут https://github.com/opencv/opencv/tree/master/data/haarcascades
    face_cascade = cv2.CascadeClassifier(os.getcwd()+'/haarcascade_frontalface_default.xml')
    # Прежде чем искать лица преобразовываем фото в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Ищем лица
    faces = face_cascade.detectMultiScale(gray,scaleFactor= 1.1,minNeighbors= 5,minSize=(10, 10))
    # Получаем количество человеческих лиц на сделанном фото
    faces_detected = format(len(faces))
    # Записываем фото в файл 
    cv2.imwrite(filename, frame)  
    # Отключаем камеру
    cap.release()
    # В качестве результата выдаем количество найденных лиц
    return(faces_detected)


# Формируем имя файла, из текущего каталога, каталога photos (должен существовать), даты и времени
filename=os.getcwd()+'/photos/'+time.ctime().replace(':','_')+'.png'
print(filename)
# Делаем снимок с первой камеры в списке камер, и сохраняем его
facescount=getphoto(filename, 0)
# Печатаем сколько лиц мы нашли на фото с веб камеры
print('Лиц обнаружено:'+facescount)
