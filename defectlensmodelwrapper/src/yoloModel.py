import cv2
import numpy as np
from ultralytics import YOLO

# Функция для получения предсказаний из модели YOLOv11x
model = YOLO('yolov11x_custom_model_200.pt')  

def get_yolo_predictions(image_path):
    image = cv2.imread(image_path)
    results = model.predict(source=image, conf=0.01)
    predictions = []

    for result in results:
        for box in result.boxes:
            x_min, y_min, x_max, y_max = box.xyxy[0].tolist()
            class_id = int(box.cls[0]) 
            confidence = box.conf[0].item() 

            predictions.append([x_min, y_min, x_max, y_max, class_id, confidence])
    
    return predictions

imgs = ['PATH/TO/IMAGE1', 'PATH/TO/IMAGE2']
for img in imgs:
  pred = get_yolo_predictions(img)
  if len(pred) != 0:
      print(f'Координаты рамки:', {pred[0], pred[1], pred[2], pred[3]})
      print(f'ID класса:', {pred[4]})
      print(f'Уверенность модели:', {pred[5]})
  else:
      print('Проблем не обнаружено')
