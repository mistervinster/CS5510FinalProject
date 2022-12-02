from YB_Pcb_Car import YB_Pcb_Car
from avoidance import Avoidance
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
import random
import os
import paramiko
import torch
import shutil
from PIL import Image

completedSigns = []
pathToModel = ""
model = torch.hub.load('ultralytics/yolov5', 'custom', path=pathToModel)

def classify():
    im = Image.open(remotepath)
    resize = im.resize((960,960))
    results = model(resize)
    df = results.pandas().xyxy[0]
    labels = set()
    for label in df['name']:
        labels.add(label)
    im.close()
    return labels

def main():
    try:
        global ssh
        global sftp
        ssh = paramiko.SSHClient() 
        ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
        ssh.connect(server, username=username, password=password)
        sftp = ssh.open_sftp()
        #Send inital code for robot to get it going
        sftp.put(localpath, remotepath)
        while True:
            #Get image sent by robot, save to local computer
            sftp.get(remotePath, "data/current.jpg")
            signs = classify()
            if 'Stop' in signs and 'Stop' not in completedSigns:
                print("Detected Stop Sign")
                completedSigns.append("Stop")
                #Send script
                sftp.put(localpath, remotepath)
            elif 'School' in signs and 'School' not in completedSigns:
                print("Detected School Zone")
                completedSigns.append('School')
                #Send script
                sftp.put(localpath, remotepath)
            elif 'Speed_limit_50' in signs and 'Speed_limit_50' not in completedSigns:
                print("Detected Speed Limit of 50")
                completedSigns.append('Speed_limit_50')
                #Send script
                sftp.put(localpath, remotepath)
            elif len(completedSigns) == 3:
                #Send script to stop
                sftp.put(localpath, remotepath)
                ssh.close()
                sftp.close()
                exit()
    except(KeyboardInterrupt):
        print("Ending program")
    finally:
        #Send script to stop
        sftp.put(localpath, remotepath)
        ssh.close()
        sftp.close()
        exit()
        
main()
