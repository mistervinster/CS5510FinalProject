# CS 5510 Final Project

## `main.py` Pseudocode

```
speed = 25 // Between 0 and 100
dt = 0.1 // All times are in seconds
while true
    take picture
    signs = classify(picture)
    if stop in signs
        drive(0)
        sleep(1)
        drive(speed)
        sleep(dt)
    elif school in signs
        drive(20)
        sleep(1)
    elif "speed limit 50" in signs
        speed = 50
        drive(speed)
        sleep(dt)
    else
        drive(speed)
        sleep(dt)
```

## Why two different programs on two different computers? 
Several high-level designs were proposed during the creation of this project. Since there is no known interface with this robot for controlling it on a laptop, we hoped to run all the code on the robot itself. This would be the most elegant software design. However, after training and testing our pytorch model we ran into a major hurdle, eventually discovering that pytorch could not be installed on the 32-bit robot raspberry pi.

Our solution is not elegant, but it is effective. `main.py` contains the driver code and runs on the robot. When it needs to classify an image, it sends that image to the laptop over SSH. Meanwhile, `classify.py` is running on the laptop. It keeps checking whether a new image has arrived. When it finds one, it classifies it (using the pytorch model that doesn't work on the robot) and stores the results in `classfile.json`. `main.py` keeps checking `classfile.json` until it changes, then uses the results.

## `YB_Pcb_Car.py` and `avoidance.py`
`YB_Pcb_Car.py` is an interface of basic commands for the robot. It was provided by the robot manufacturers. 

`avoidance.py` has some basic and completely unreliable obstacle avoidance, which *usually* keeps the robot from crashing into things. At a minimum, it keeps the robot from continuing to spin its wheels after it has hit a wall. In the demonstration video, this can be observed when the robot gets too close to the demonstrator's foot. This code has its roots in `Ultrasonic+IR avoid.ipynb`, also provided by the manufacturers, although it has been copied over to a python file and modified extensively to meet our needs.
