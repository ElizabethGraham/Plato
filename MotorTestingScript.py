from adafruit_motorkit import MotorKit
from  pynput import keyboard
kit = MotorKit()

kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
kit.motor3.throttle = 0.0
kit.motor4.throttle = 0.0

def on_press(key):
    try:
        if key.char == "w":
            motorsForward()
            print("Forward")
        elif key.char == "a":
            motorsLeft()
            print("Left")
        elif key.char == "s":
            motorsBackward()
            print("Reverse")
        elif key.char == "space":
            motorsStop()
            print("Stop")
        elif key.char == "d":
            motorsRight()
            print("Right")
        elif key.char == "1":
            motorOneTest()
            prindaadaadadaaaat("1")
        elif key.char == "2":
            motorTwoTest()
            print("2")
        elif key.char == "3":
            motorThreeTest()
            print("3")
        elif key.char == "4":
            motorFourTest()
            print("4")
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    else:
        motorsStop()
        print("Motors Released")
    
def motorsForward():
    kit.motor1.throttle = 1.0
    kit.motor2.throttle = -1.0
    kit.motor3.throttle = 1.0
    kit.motor4.throttle = -1.0
    
def motorsBackward():
    kit.motor1.throttle = -1.0
    kit.motor2.throttle = 1.0
    kit.motor3.throttle = -1.0
    kit.motor4.throttle = 1.0
    
def motorsLeft():
    kit.motor1.throttle = 1.0
    kit.motor2.throttle = 1.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0
    
def motorsRight():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 1.0
    kit.motor4.throttle = 1.0

def motorsStop():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0
    
def motorOneTest():
    kit.motor1.throttle = 1.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0
def motorTwoTest():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 1.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0
def motorThreeTest():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 1.0
    kit.motor4.throttle = 0.0
def motorFourTest():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 1.0

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()