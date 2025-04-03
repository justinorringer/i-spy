import os
from ultralytics import YOLO
from PIL import Image

model = None

def train():
    # Load the model
    model = YOLO("yolov8l.pt")  # Load a pretrained YOLOv8 model

    # Train the model on the dataset
    results = model.train(data='data.yaml', epochs=1, imgsz=640)  # Adjust epochs and imgsz as needed

    # Save the trained model
    model.save("yolov8l_trained.pt")

train()

for item in os.listdir("animals"):
    print("Processing file:", item)
    results = model.predict("animals/" + item)[0]
    print("Length of boxes: ", len(results.boxes))
    for box in results.boxes:
        cords = box.xyxy[0].tolist()
        cords = [round(x) for x in cords]
        class_id = results.names[box.cls[0].item()]
        conf = round(box.conf[0].item(), 2)
        print("Object type:", class_id)
        print("Coordinates:", cords)
        print("Probability:", conf)

    Image.fromarray(results.plot()[:,:,::-1]).save("animals/output-" + item)
