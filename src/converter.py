import json
import os
from pathlib import Path

import cv2

# Define class names
class_names = ["emptybox", "fullbox", "object"]  # Update with your actual class names

def convert_to_yolo(json_file, img_width, img_height):
    with open(json_file) as f:
        data = json.load(f)

    annotations = []
    for shape in data['shapes']:
        label = shape['label']
        points = shape['points']
        xmin = min(points[0][0], points[1][0])
        xmax = max(points[0][0], points[1][0])
        ymin = min(points[0][1], points[1][1])
        ymax = max(points[0][1], points[1][1])

        x_center = (xmin + xmax) / 2 / img_width
        y_center = (ymin + ymax) / 2 / img_height
        width = (xmax - xmin) / img_width
        height = (ymax - ymin) / img_height

        class_index = class_names.index(label)
        annotations.append(f"{class_index} {x_center} {y_center} {width} {height}\n")

    return annotations

def convert_directory(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for json_file in Path(input_dir).glob("*.json"):
        img_path = json_file.with_suffix('.jpg')  # Assuming image extension is .jpg
        img = cv2.imread(str(img_path))
        if img is None:
            continue

        height, width, _ = img.shape
        annotations = convert_to_yolo(json_file, width, height)
        
        output_file = Path(output_dir) / f"{json_file.stem}.txt"
        with open(output_file, 'w') as f:
            f.writelines(annotations)

input_dir = 'd:\\KIT\\HackAThonWBK24\\dataset\\images\\train\\emptybox'
output_dir = 'd:\\KIT\\HackAThonWBK24\\dataset\\labels\\train\\emptybox'
convert_directory(input_dir, output_dir)
