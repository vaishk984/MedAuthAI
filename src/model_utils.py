from ultralytics import YOLO

def load_model(weights_path):
    return YOLO(weights_path)

def evaluate_model(model, data_path):
    metrics = model.val(data=data_path)
    print(metrics)