from adafruit_motorkit import MotorKit
from pynput import keyboard

kit = MotorKit()

kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
kit.motor3.throttle = 0.0
kit.motor4.throttle = 0.0


def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single char keys
    except:
        k = key.name
    if k in ["1", "2", "left", "right"]:  # keys of interest
        # self.keys.append(k) store in globalish variable
        print("Key pressed: " + k)
        return False  # stop listener, remove if you want more keys


def motorsForward():
    kit.motor1.throttle = 1.0
    kit.motor2.throttle = 1.0
    kit.motor3.throttle = 1.0
    kit.motor4.throttle = 1.0


def motorsStop():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0


listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a seperate thread
listener.join()  # remove if main thread is poling off self.key

x = True
while x == True:
    on_press()
