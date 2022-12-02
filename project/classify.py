import os
from time import sleep
from PIL import Image
import torch
import pandas as pd


CLASSFILE_NAME = "classfile.json"

# Delete all .jpg files in /data
i = 1
while True:
    path = f"data/image{i}.jpg"
    if os.path.exists(path):
        os.remove(path)
        i += 1
    else:
        break

# Get model ready to classify
pathToModel = "../../5510ModelTrain/yolo5m6/modelVersion2.pt"
model = torch.hub.load('ultralytics/yolov5', 'custom', path=pathToModel)
image = 1
nextImage = f"data/image{image}.jpg"
print("READY!!!")
while True:
    # If new image exists
    if os.path.isfile(nextImage):
        sleep(0.5) # Make sure the file has been completely transferred - this may or may not be necessary

        im = Image.open(nextImage)
        resize = im.resize((960,960))
        results = model(resize)
        results.print()
        df = results.pandas().xyxy[0]
        results.save(labels=True, save_dir='data/trial14/img')
        if df.shape[0] == 0:
            df = pd.DataFrame({
                'name': ['nothing'],
                'image': [nextImage]
            })
        else:
            df = pd.DataFrame({
                'name': df['name'],
                'image': [nextImage for i in range(df.shape[0])]
            })
        labels = df.to_json(orient="records")
        with open(CLASSFILE_NAME, "w") as outfile:
            outfile.write(labels)
        image += 1
        nextImage = f"data/image{image}.jpg"
