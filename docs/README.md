# AI-Based Detection of Counterfeit Medicines

This project uses **YOLOv8** (Ultralytics) to detect and classify medicines as **authentic** or **counterfeit** from images.  
It leverages deep learning for object detection and can be deployed for real-world pharmaceutical verification.

---
## 🚀 Installation

1. **Clone the repository** (if using GitHub) or unzip the project.
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

---
## Dataset
Classes: authentic, counterfeit

Format: YOLOv8-compatible directory structure

Full dataset download link is available in AI-basedDetectionOfCounterfeitMedicines\data

---
## Training
```bash
   yolo detect train data=./data/data.yaml model=yolov8n.pt epochs=50 imgsz=640 batch=16
```

---
## Evaluation
```bash
    yolo detect val model=./models/best.pt data=./data/data.yaml
```