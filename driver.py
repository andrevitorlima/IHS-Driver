import cv2
import evdev

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)
    '''
    /dev/input/event4 VirtualBox USB Tablet usb-0000:00:06.0-1/input0
    /dev/input/event6 VirtualBox mouse integration 
    /dev/input/event5 ImExPS/2 Generic Explorer Mouse isa0060/serio1/input0
    /dev/input/event3 Video Bus LNXVIDEO/video/input0
    /dev/input/event2 AT Translated Set 2 keyboard isa0060/serio0/input0
    /dev/input/event1 Sleep Button LNXSLPBN/button/input0
    /dev/input/event0 Power Button LNXPWRBN/button/input0
    '''
face_recognition = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_recognition = cv2.CascadeClassifier('haarcascade_eye.xml')


def detect(gray, frame):
    faces = face_recognition.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        '''

        print (x,y)
        print('tamanho')
        print (w,h)
         x(0;490) ; centralizado 245
        y(0;290) ; centralizado 145
        tam medio square = 160
        teste 10%x 5%y

        '''

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_recognition.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            #print(ew,eh)
    return frame

video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
