import cv2
import evdev
from evdev import UInput, AbsInfo, ecodes as e
'''
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)

    /dev/input/event7 VirtualBox Webcam - HD User Fac usb-0000:00:06.0-2/button
    /dev/input/event4 VirtualBox USB Tablet usb-0000:00:06.0-1/input0
    /dev/input/event6 VirtualBox mouse integration 
    /dev/input/event5 ImExPS/2 Generic Explorer Mouse isa0060/serio1/input0
    /dev/input/event3 Video Bus LNXVIDEO/video/input0
    /dev/input/event2 AT Translated Set 2 keyboard isa0060/serio0/input0
    /dev/input/event1 Sleep Button LNXSLPBN/button/input0
    /dev/input/event0 Power Button LNXPWRBN/button/input0
'''

device = evdev.InputDevice('/dev/input/event5')
cap = {
    e.EV_KEY : [e.KEY_A, e.KEY_B],
    e.EV_ABS : [
        (e.ABS_X, AbsInfo(value=0, min=0, max=255,
                          fuzz=0, flat=0, resolution=0)),
        (e.ABS_Y, AbsInfo(0, 0, 255, 0, 0, 0)),
        (e.ABS_MT_POSITION_X, (0, 128, 255, 0)) ]
 }
ui = UInput(cap, name='example-device', version=0x3)
'''
print(device.capabilities(verbose=True))
{('EV_SYN', 0): [('SYN_REPORT', 0), ('SYN_CONFIG', 1), ('SYN_MT_REPORT', 2)], 
 ('EV_KEY', 1): [(['BTN_LEFT', 'BTN_MOUSE'], 272), ('BTN_RIGHT', 273), 
('BTN_MIDDLE', 274), ('BTN_SIDE', 275), ('BTN_EXTRA', 276)], ('EV_REL', 2): 
[('REL_X', 0), ('REL_Y', 1), ('REL_HWHEEL', 6), ('REL_WHEEL', 8)]}
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
    ui.write(e.EV_ABS, e.ABS_X, 20)
    ui.write(e.EV_ABS, e.ABS_Y, 20)
    ui.syn()
    print('a')
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
