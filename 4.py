import cv2

# image = cv2.imread('img.jpg')
# rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# crop_image = image[10:500, 60:250]
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _, tres = cv2.threshold(image, 90, 255, 0)
# blur = cv2.GaussianBlur(image, (75, 75), 0)
# # cv2.rectangle(image, (300, 300), (600, 600), (0, 255, 255), 5)
# cv2.putText(image, 'Image', (600, 600),
#             cv2.FONT_ITALIC, 4, (0, 255, 255), 10)

image = cv2.imread('img2.jpg')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray)
faces_detected = f'Обнаружено лиц: {len(faces)}'
print(faces_detected)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
