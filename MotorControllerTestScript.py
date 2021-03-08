from adafruit_motorkit import MotorKit
from pynput import keyboard

kit = MotorKit()


# Motor configuration dependant on individual build.
# Motor 1 = front left
# Motor 2 = back left
# Motor 3 = front right
# Motor 4 = back right

# Motor 1 + 3 are positive facing forward, 2 + 4 are negative facing forward
def motors_forward():
    kit.motor1.throttle = 1.0
    kit.motor2.throttle = -1.0
    kit.motor3.throttle = 1.0
    kit.motor4.throttle = -1.0


def motors_backward():
    kit.motor1.throttle = -1.0
    kit.motor2.throttle = 1.0
    kit.motor3.throttle = -1.0
    kit.motor4.throttle = 1.0


# Right motors (3,4) will arc around left motors (1,2) to turn left
def motors_left():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 1.0
    kit.motor4.throttle = -1.0


# Left motors (1,2) will arc around right motors (3,4) to turn right
def motors_right():
    kit.motor1.throttle = 1.0
    kit.motor2.throttle = -1.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0


# Park motors
def motors_stop():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0


def motor_one_test():
    kit.motor1.throttle = 1.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0


def motor_two_test():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 1.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0


def motor_three_test():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 1.0
    kit.motor4.throttle = 0.0


def motor_four_test():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 1.0

# Start with the motors parked. 
motors_stop()


# Dictionary holding all movement keys and corresponding movement functions
keypress_dict = {"w": motors_forward, "a": motors_left, "s": motors_backward,
                 "d": motors_right, "1": motor_one_test, "2": motor_two_test,
                 "3": motor_three_test, "4": motor_four_test, "space": motors_stop}


def on_press(key):
    try:
        # Did a movement key get pressed
        if key.char in keypress_dict:
            # Run the movement keys corresponding function
            keypress_dict[key.char]()
    except:
            pass


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    else:
        # If any key is released, stop motors. 
        # I think this is better than making a function to stop only on movement key releases
        # since really any time a key is released the motors should be off.
        motors_stop()
        print("Motors Released")


# Initialize the keyboard listener
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
