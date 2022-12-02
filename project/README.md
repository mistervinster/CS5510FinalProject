# CS 5510 Final Project

## Pseudocode
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

Transfer image: `scp image11.jpg 144.39.54.141:gabe/`. Edit `~/.ssh/config` as needed.
