import cv2
import time
import uinput

#eventos que podem ser utilizados pelo driver
events = (
        uinput.REL_X,
        uinput.REL_Y,
        uinput.BTN_LEFT,
        uinput.BTN_RIGHT,
        )

#arquivos do modelo Haar Cascade
face_recognition = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_recognition = cv2.CascadeClassifier('haarcascade_eye.xml')

#função que cria reconhece e cria o frame do rosto e dos olhos
def detect(gray, frame, device):
    faces = face_recognition.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #calibração manual, delimitando a altura e largura
        #print(x, y)
        
        #calibração automática após os testes feitos manualmente
        direita=(largura-w)/2
        esquerda=(largura*1.2-w)/2
        baixo=(altura-h)/2
        cima=(altura*0.9-h)/2
        
        #calibração manual
        #print('esquerda',esquerda)
        #print('direita',direita)
        #print('cima',cima)
        #print('baixo',baixo)

        #movimento do mouse
        #ajustar a velocidade para conforto
        if x > esquerda:
            for i in range(20):
                device.emit(uinput.REL_X, -2)
                time.sleep(0.01)
        if x < direita:
            for i in range(20):
                device.emit(uinput.REL_X, 2)
                time.sleep(0.01)
        if y > baixo:
            for i in range(20):
                device.emit(uinput.REL_Y, 2)
                time.sleep(0.01)
        if y < cima:
            for i in range(20):
                device.emit(uinput.REL_Y, -2)
                time.sleep(0.01)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_recognition.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            if (len(eyes) < 2) and (len(faces)==1):
                #clique esquerdo
                device.emit(uinput.BTN_LEFT, 1)
                device.emit(uinput.BTN_LEFT, 0)

    return frame

#criação da janela
window_name='Video'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
video_capture = cv2.VideoCapture(0)
altura = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
largura = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)


with uinput.Device(events) as device:
    while True:
        _, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canvas = detect(gray, frame, device)
        cv2.imshow(window_name, canvas)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
video_capture.release()
cv2.destroyAllWindows()
