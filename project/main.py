# A conglomeration of TestCamera.ipynb and Ultrasonic+IR avoid.ipynb, with original code thrown in
from YB_Pcb_Car import YB_Pcb_Car
from avoidance import Avoidance
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
from fabric import Connection
import json
import cv2


# IP address of the laptop
HOST = "144.39.54.141"
# Path to the project directory in the laptop
REMOTE_PATH = "gabe\\traffic\\5510Midterm\\project\\"
CLASSFILE_NAME = "classfile.json"

# Because the robot keeps veering right
RIGHT_COMPENSATION = 1
LEFT_COMPENSATION = 0.85

# Classifies image which can be found at path
def classify(path, connection):
    newClassfile = oldClassfile = connection.run(f"type {REMOTE_PATH}{CLASSFILE_NAME}").stdout
    connection.put(path, REMOTE_PATH + "data")
    while newClassfile == oldClassfile:
        newClassfile = connection.run(f"type {REMOTE_PATH}{CLASSFILE_NAME}").stdout
    resultArray = json.loads(newClassfile)
    signNameArray = []
    for object in resultArray:
        if 'name' in object:
            signNameArray.append(object['name'])
    return signNameArray
    

# Converts a speed out of 100 to a number the robot can understand
def drive(car, left, right):
    MAX_SPEED = 255 # This seems to be the fastest the robot can go
#     MAX_SPEED /= 2    # For a slower ride
    right = int(right * MAX_SPEED * RIGHT_COMPENSATION / 100)
    left = int(left * MAX_SPEED * LEFT_COMPENSATION / 100) 
    car.Car_Run(left, right)


def main():
    frames = 0 # Number of images the robot has taken
    car = YB_Pcb_Car()
    speed = 25
    dt = 0.1
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)
#     sleep(0.1)    # Let camera warm up
    # swivel camera
    car.Ctrl_Servo(1, 55)
    sleep(0.5)
    car.Ctrl_Servo(2, 95)
    sleep(0.5)

    avoidance = Avoidance(car)

    connection = Connection(HOST)

    try:
        while True:
            avoidance.avoid()
            camera.capture(rawCapture, format="bgr")
            image = rawCapture.array
            frames += 1
            # save the image
            path = f"data/image{frames}.jpg"
            cv2.imwrite(path, image)
            signs = classify(path, connection)
            if 'Stop' in signs:
                print("Stopping")
                car.Car_Stop()
                sleep(1)
                drive(car, speed, speed)
                sleep(dt)
            elif 'School' in signs:
                print("School zone")
                drive(car, 20, 20)
                sleep(1)
            elif 'Speed_limit_50' in signs:
                print("Speed limit sign")
                speed = 50
                print(f"Changing speed limit to {speed}")
                drive(car, speed, speed)
                sleep(dt)
            else:
                drive(car, speed, speed)
                sleep(dt)
            # Clear the frame for the next picture
            rawCapture.truncate(0)
    except(KeyboardInterrupt):
        print("Ending program")
    finally:
        car.Car_Stop()
        camera.close()
        del car

        
main()
