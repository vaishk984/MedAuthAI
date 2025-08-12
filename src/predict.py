from ultralytics import YOLO

def run_predictions():
    model = YOLO("runs/detect/train10/weights/best.pt") 
    results = model.predict(source="/content/data/test", save=True, conf=0.5)
    print("Predictions saved.")

if __name__ == "__main__":
    run_predictions()