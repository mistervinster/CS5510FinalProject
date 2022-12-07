# Traffic Sign Detection
## CS5510 Final Project by Sleep Deprived Coders

## Setup Instructions
*Note: Setup is non-trivial. Try using a laptop and robot that are already set up, if possible.*

*Another note: this program currently works only with a Windows laptop. It has been tested on Windows 11, although earlier versions may also work.*

1. Set up SSH between the laptop and the robot as demonstrated [here](https://www.youtube.com/watch?v=Wx7WPDnwcDg).
1. Edit `~/.ssh/config` on the robot as needed.
    - This is necessary because the username on the laptop, "direct lab," contains a space, which can cause unexpected results with SSH.
        - Yes, it took way too much work to figure this out.
1. Clone or copy this repo onto the robot's root directory. The robot needs `project/main.py`, `project/YB_Pcb_Car.py`, `project/avoidance.py` and `project/data/`.
1. Install 3rd party libraries onto the robot as necessary:
    ```
    pip3 install fabric
    pip3 install picamera
    pip3 install opencv-python
    ```
1. If necessary, update the hard-coded values at the beginning of `main.py`.
1. Clone or copy this repo onto the laptop. Needed: `project/classify.py`, `project/modelVersion2.pt`, `project/classfile.json`, `project/data`.
1. Install pytorch and pandas on the laptop, if needed.


## Running the Program

1. On the laptop, navigate into the project directory and run `python classify.py`.
1. In a separate tereminal, `ssh` into the robot and run `main.py`.
1. To end the program, Ctrl-C on `main.py`, then on `classify.py`.
