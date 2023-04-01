import os 
import shutil
from PIL import Image
import torchvision.transforms as T
import torchvision.transforms.functional as TF
import torch
import random


def random_transform():
    transforms = [
        T.Compose([
            T.ToTensor(),
            T.RandomErasing(p=1, scale=(0.01, 0.04), ratio=(0.3, 3.3)),
            T.ToPILImage()
        ]),
        T.Compose([
            T.GaussianBlur(3, sigma=(0.2, 1.0))
        ]),
        T.Compose([
            T.ToTensor(),
            T.RandomErasing(p=0.8, scale=(0.01, 0.03), ratio=(0.3, 3.3)),
            T.RandomErasing(p=1, scale=(0.01, 0.03), ratio=(0.3, 3.3)),
            T.ToPILImage()
        ]),
        T.Compose([
            T.ColorJitter(brightness=0.6, contrast=0.0, saturation=0.0, hue=0.0),
            T.RandomRotation(20) #8
        ]),
        T.Compose([
            T.ToTensor(),
            T.RandomErasing(p=1, scale=(0.01, 0.03), ratio=(0.3, 3.3)),
            T.RandomRotation(10),
            T.ToPILImage()
        ]),
        T.Compose([
            T.ColorJitter(brightness= 0.25, contrast= 0.0, saturation= 0.0, hue=(0.01,0.02))
        ]),
        T.Compose([
            T.RandomPerspective(p=1, distortion_scale=0.2)
        ]),
         T.Compose([
            T.RandomPerspective(p=1, distortion_scale=0.2),
            T.RandomRotation(5),
        ]),
          T.Compose([
            T.ColorJitter(brightness=0.5, contrast=0.7, saturation=0.1, hue=0.05)
        ])
    ]
    return random.choice(transforms)


if __name__ == "__main__":

    directory = '/Users/ruipedro/Desktop/Dataset_Final/9'
    dest_path = '/Users/ruipedro/Desktop/Dataset_Final_v2/9'
    #dest_path = '/Users/ruipedro/Desktop/teste_data'

    k = 17 # Set the number of sub-folders to select

    subfolders = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    # List all sub-folders in the parent directory

    k_subfolders = random.sample(subfolders, k)  # Select k random sub-folders

    #number folder initialize
    folder_count = 33

    # numero da classe
    number_class = 9
    prefix_previous = 9

    # number image initialize
    aux_count = 991
    
    #lastTransform = None

    #auxTransformList = []

    for subfolder in k_subfolders:
        
        prefix = subfolder.split('/')[-1].split('_')[-1]
        print(prefix)

        if prefix != prefix_previous:
            folder_count += 1
        
        new_folder_path = os.path.join(dest_path, f"{number_class}_{folder_count}")
        os.makedirs(new_folder_path, exist_ok=True)


        for file in os.listdir(subfolder):
            name = file.split('.')[0]
            class_name = name.split('_')[0]
            imgpath = os.path.join(subfolder, file)
            img = Image.open(imgpath)
            transform = random_transform()
            print(transform)
            img = transform(img)
            dest_imgpath = os.path.join(new_folder_path, f"{class_name}_{aux_count}.jpg")
            img.save(dest_imgpath)
            aux_count += 1
        
        prefix_previous = prefix