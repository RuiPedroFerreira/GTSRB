import os 
import shutil
from PIL import Image
import torchvision.transforms as T

directory_path = "/Users/ruipedro/Desktop/Dataset_Final/0"
dest_path = "/Users/ruipedro/Desktop/teste_data"

# use 
# transform = T.Grayscale()

#use
transform = T.Compose([
    T.ColorJitter(brightness=0.6, contrast=0, saturation=0.2, hue=0)
])

#use
transform = T.Compose([
    T.RandomRotation(20)
])

transform = T.Compose([
    T.RandomCrop(size=(128,128), padding=4, pad_if_needed=True)
])



folder_count = 16
prefix_previous = 0

for root, dirs, files in os.walk(directory_path):
    prefix = root.split('/')[-1].split('_')[-1]
    
    if prefix == "0":
            continue
    
    if prefix != prefix_previous:
        
        folder_count += 1
    
        new_folder_path = os.path.join(dest_path, f"0_{folder_count}")
        os.makedirs(new_folder_path, exist_ok=True)
    
        for file_name in files:
            name = file_name.split('.')[0]
            aux = file_name.split('_')[-1].split('.')[0]
            imgpath = os.path.join(root, file_name)
            img = Image.open(imgpath)
            img = transform(img)
            dest_imgpath = os.path.join(new_folder_path, f"{name}_{aux}.jpg")
            img.save(dest_imgpath)
    
    prefix_previous = prefix
    
        

