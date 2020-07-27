from adafruit_motorkit import MotorKit
from  pynput import keyboard

kit = MotorKit()

# Park motors
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
kit.motor3.throttle = 0.0
kit.motor4.throttle = 0.0

# Motor configuration dependant on individual build.
# Motor 1 = front left
# Motor 2 = back left
# Motor 3 = front right
# Motor 4 = back right

# Motor 1 + 3 are positive facing forward, 2 + 4 are negative facing forward
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
    
# Right motors (3,4) will arc around left motors (1,2) to turn left
def motorsLeft():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 1.0
    kit.motor4.throttle = -1.0

# Left motors (1,2) will arc around right motors (3,4) to turn right
def motorsRight():
    kit.motor1.throttle = 1.0
    kit.motor2.throttle = -1.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0

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

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
