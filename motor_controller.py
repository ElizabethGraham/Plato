from adafruit_motorkit import MotorKit  # Error on Windows, functions on Raspberry Pi
from pynput import keyboard


# Motor configuration: **dependant on individual build**
# Motor 1 = front left
# Motor 2 = back left
# Motor 3 = front right
# Motor 4 = back right

kit = MotorKit


def motors_forward():
    motors_right()
    motors_left()


def motors_backward():
    MotorKit.motor1.throttle = -1.0
    MotorKit.motor2.throttle = 1.0
    MotorKit.motor3.throttle = -1.0
    MotorKit.motor4.throttle = 1.0


# Right motors (3,4) will arc around left motors (1,2) to turn left
def motors_left():
    MotorKit.motor3.throttle = 1.0
    MotorKit.motor4.throttle = -1.0


# Left motors (1,2) will arc around right motors (3,4) to turn right
def motors_right():
    MotorKit.motor1.throttle = 1.0
    MotorKit.motor2.throttle = -1.0


# Park motors
def motors_stop():
    MotorKit.motor1.throttle = 0.0
    MotorKit.motor2.throttle = 0.0
    MotorKit.motor3.throttle = 0.0
    MotorKit.motor4.throttle = 0.0


def motor_one_test():
    MotorKit.motor1.throttle = 1.0


def motor_two_test():
    MotorKit.motor2.throttle = 1.0


def motor_three_test():
    MotorKit.motor3.throttle = 1.0


def motor_four_test():
    MotorKit.motor4.throttle = 1.0


# Dictionary holding all movement keys and corresponding movement functions
keypress_dict = {"w": motors_forward, "a": motors_left, "s": motors_backward,
                 "d": motors_right, "1": motor_one_test, "2": motor_two_test,
                 "3": motor_three_test, "4": motor_four_test, "space": motors_stop}

if __name__ == '__main__':
    # Start with the motors parked.
    motors_stop()

    def on_press(key):
        try:
            # Did a movement key get pressed
            if key.char in keypress_dict:
                # Run the movement keys corresponding function
                keypress_dict[key.char]()
        except KeyError:
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
