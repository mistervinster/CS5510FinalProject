# CS 5510 Final Project

## Pseudocode
`main.py`
```
speed = 25 // Between 0 and 100
dt = 0.1
while true
    take picture
    signs = classify(picture)
    if stop in signs
        drive(0)
        sleep(1)
        drive(speed)
        sleep(dt)
    elif speed limit in signs
        speed = speedlimit['speed']
        drive(speed)
        sleep(dt)
    elif crosswalk in signs
        drive(20)
        sleep(1)
    else
        drive(speed)
        sleep(dt)
```

## Why two different programs on two different computers? 
Several high-level designs were proposed during the creation of this project. Since there is no known interface with this robot for controlling it on a laptop, we hoped to run all the code on the robot itself. This would be the most elegant software design. However, after training and testing our pytorch model we ran into a major hurdle, eventually discovering that pytorch could not be installed on the 32-bit robot raspberry pi.

Our solution is not elegant, but it is effective. `main.py` contains the driver code and runs on the robot. When it needs to classify an image, it sends that image to the laptop over SSH. Meanwhile, `classify.py` is running on the laptop. It keeps checking whether a new image has arrived. When it finds one, it classifies it (using the pytorch model that doesn't work on the robot) and stores the results in `classfile.json`. `main.py` keeps checking `classfile.json` until it changes, then uses the results.
