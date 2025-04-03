from ultralytics import YOLO
from PIL import Image

model = YOLO("yolov8l.pt")

results = model.predict("books/riddles/mrzispy0012.jpg")[0]
print("Length of boxes: ", len(results.boxes))
for box in results.boxes:
    cords = box.xyxy[0].tolist()
    cords = [round(x) for x in cords]
    class_id = results.names[box.cls[0].item()]
    conf = round(box.conf[0].item(), 2)
    print("Object type:", class_id)
    print("Coordinates:", cords)
    print("Probability:", conf)

Image.fromarray(results.plot()[:,:,::-1]).save("output.jpg")
