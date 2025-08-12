import os
import shutil
import random

def split_dataset(source_folder, train_folder, valid_folder, split_ratio=0.8):
    images = [f for f in os.listdir(source_folder) if f.endswith((".jpg", ".png"))]
    random.shuffle(images)
    split_index = int(len(images) * split_ratio)
    
    for img in images[:split_index]:
        shutil.copy(os.path.join(source_folder, img), train_folder)
    for img in images[split_index:]:
        shutil.copy(os.path.join(source_folder, img), valid_folder)

if __name__ == "__main__":
    split_dataset("/content/data/all_images", "/content/data/train", "/content/data/test")