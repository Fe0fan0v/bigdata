import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('Введите свое имя\n')
print('Запуск захвата. Смотрите в камеру и ожидайте.')
capture = cv2.VideoCapture(0)
count = 0

while capture.isOpened():
    _, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.3,
                                          minNeighbors=5,
                                          minSize=(20, 20))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        count += 1
        cv2.imwrite(f'faces/{face_id}_{count}.jpg', gray[y:y+h, x:x+w])
    cv2.imshow('Camera', frame)
    if cv2.waitKey(10) == 27 or count >= 30:
        break
print('\nОбучающая выборка сохранена')
capture.release()
cv2.destroyAllWindows()
