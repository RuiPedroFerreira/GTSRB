import os 
import shutil
from PIL import Image
import torchvision.transforms as T
import torchvision.transforms.functional as TF
import torch
import random



if __name__ == "__main__":
     
    directory_path = "/Users/ruipedro/Desktop/Dataset_Final/36"
    dest_path = "/Users/ruipedro/Desktop/Dataset_Final_Augmentation/36" 
    
    number_class = 36
    folder_count = 9
    prefix_previous = 36
    aux_count = 271

    '''
    transformsList = [
        T.Compose([
            T.ToTensor(),
            T.RandomErasing(p=1, scale=(0.01, 0.05), ratio=(0.3, 3.3)),
            T.ToPILImage()
        ]),
        T.Compose([
            T.Grayscale(),
            T.RandomRotation(30) #4
        ]),
        T.Compose([
            T.ToTensor(),
            T.RandomErasing(p=0.6, scale=(0.01, 0.04), ratio=(0.3, 3.3)),
            T.RandomErasing(p=1, scale=(0.01, 0.05), ratio=(0.3, 3.3)),
            T.ToPILImage()
        ]),
        T.Compose([
            T.ColorJitter(brightness=0.3, contrast=0, saturation=0.2, hue=0.035),
            T.RandomRotation(20) #8
        ]),
        T.Compose([
            T.ToTensor(),
            T.RandomErasing(p=1, scale=(0.01, 0.04), ratio=(0.3, 3.3)),
            T.RandomRotation(10),
            T.ColorJitter(brightness=0.4, contrast=0.0, saturation=0.0, hue=0.02),
            T.ToPILImage()
        ]),
        T.Compose([
            T.ColorJitter(brightness=0.5, contrast=0.3, saturation=0.3, hue=0.01)
        ]),
        T.Compose([
          T.ColorJitter(brightness=0.65, contrast=0.1, saturation=0.1, hue=0.0),
          T.RandomRotation(35) #5
        ]),
        T.Compose([
          T.Grayscale()
        ]),
         T.Compose([
          T.ColorJitter(brightness=0.2, contrast=0.3, saturation=0.2, hue=0.02),
        ])
    ]
    '''
    transformsList = [
        T.Compose([
            T.Grayscale(),
            T.RandomRotation(20) #4
        ]),
        T.Compose([
            T.ToTensor(),
            T.RandomErasing(p=0.6, scale=(0.01, 0.04), ratio=(0.3, 3.3)),
            T.RandomErasing(p=1, scale=(0.01, 0.05), ratio=(0.3, 3.3)),
            T.ToPILImage()
        ]),
        T.Compose([
            T.ColorJitter(brightness=0.5, contrast=0.3, saturation=0.3, hue=0.01)
        ]),
        T.Compose([
            T.ColorJitter(brightness=0.3, contrast=0, saturation=0.2, hue=0.035),
            T.RandomRotation(10) #8
        ]),
        T.Compose([
            T.ToTensor(),
            T.RandomErasing(p=1, scale=(0.01, 0.05), ratio=(0.3, 3.3)),
            T.ToPILImage()
        ])
    ]

    for i in range(len(transformsList)):  # use range(len()) to iterate over indexes
        
        transform = random.choice(transformsList)
        transformsList.remove(transform) 
         
        for root, dirs, files in os.walk(directory_path):
            prefix = root.split('/')[-1].split('_')[-1]
            #print(prefix)

            if prefix == "36":
                    continue
            
            if prefix != prefix_previous:
                
                folder_count += 1
            
                new_folder_path = os.path.join(dest_path, f"{number_class}_{folder_count}")
                os.makedirs(new_folder_path, exist_ok=True)
            
                for file_name in files:
                    name = file_name.split('.')[0]
                    class_name = name.split('_')[0]
                    #aux = file_name.split('_')[-1].split('.')[0]
                    imgpath = os.path.join(root, file_name)
                    img = Image.open(imgpath)
                    img = transform(img)
                    dest_imgpath = os.path.join(new_folder_path, f"{class_name}_{aux_count}.jpg")
                    img.save(dest_imgpath)
                    aux_count += 1
            
            prefix_previous = prefix
      

