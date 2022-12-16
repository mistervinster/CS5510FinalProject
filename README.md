# Traffic Sign Detection
## CS5510 Final Project by Sleep Deprived Coders

## Setup Instructions
*Note: Setup is non-trivial. If possible, use a laptop and robot that are already set up.*

*Another note:  The laptop portion of this program currently works only with a Windows computer. It has been tested on Windows 11, although earlier versions may also work.*

1. Set up SSH between the laptop and the robot as demonstrated [here](https://www.youtube.com/watch?v=Wx7WPDnwcDg).
1. Edit `~/.ssh/config` on the robot as needed. 
    - As an example:
        ```
        Host 10.9.0.18
            User "direct lab"
        ```
    - This is necessary because the username on the laptop, "direct lab", contains a space, which can cause problems with SSH.
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
1. Install pytorch, pandas and pillow on the laptop, if needed.


## Running the Program

1. On the laptop, navigate into the project directory and run `python classify.py`.
1. In a separate tereminal, `ssh` into the robot and run `python3 main.py`.
1. To end the program, Ctrl-C on `main.py`, then on `classify.py`.
1. Images taken by the robot are saved to `project/data/` on the laptop and on the robot. Images with bounding boxes and classifications are `project/data/classified/`.


## Links to Report and Video
Report: https://docs.google.com/document/d/1IBrOtn7q5k-dPKCCHpDdFXyT7Bcg1vtqkQpHgRrh0Ho/edit?usp=sharing
Video: https://photos.app.goo.gl/B1FpUDQi5MjWjVG36
