import os 
import shutil
from PIL import Image
import torchvision.transforms as T
import torchvision.transforms.functional as TF
import torch


directory_path = "/Users/ruipedro/Desktop/Dataset_Final/0"
dest_path = "/Users/ruipedro/Desktop/Dataset_Final_Augmentation/0"

# transform 1 - Grey Scale (use)

'''
transform = T.Compose([
    T.Grayscale()
])
'''

# transform 2 - Rotation (use)

'''
transform = T.Compose([
    T.RandomRotation(20)
]) '''

'''
#Hue - refers to the color of an object or pixel, which can be described in terms of its position on a color wheel.
transform = T.Compose([
    T.ColorJitter(brightness=0.5, contrast=0.3, saturation=0.4, hue=0.03)
    # T.ColorJitter(brightness=0.6, contrast=0, saturation=0.2, hue=0.05)
])'''


#https://towardsdatascience.com/complete-guide-to-data-augmentation-for-computer-vision-1abe4063ad07
# Cutout - Cut regiof of the image
'''
parametes of function:
scale -  the height and width of the erased rectangle are randomly chosen to be between s_min and s_max
ratio -  the aspect ratio of the erased rectangle is randomly chosen to be between r_min and r_max. 
'''

'''
#combine drop 2
transform = T.Compose([
    T.ToTensor(),
    T.RandomErasing(p=0.8, scale=(0.01, 0.04), ratio=(0.3, 3.3)),
    T.RandomErasing(p=1, scale=(0.01, 0.05), ratio=(0.3, 3.3)),
    T.ToPILImage()
])'''

'''
#single cutout
transform = T.Compose([
    T.ToTensor(),
    T.RandomErasing(p=1, scale=(0.01, 0.05), ratio=(0.3, 3.3)),
    T.ToPILImage()
])'''


# transform grey + rotation 
'''
transform = T.Compose([
    T.Grayscale(),
    T.RandomRotation(30)
])'''

# transform 7
'''
transform = T.Compose([
    T.ToTensor(),
    T.RandomErasing(p=0.8, scale=(0.01, 0.03), ratio=(0.3, 3.3)),
    T.RandomRotation(15),
    T.ColorJitter(brightness=0.6, contrast=0.1, saturation=0.1, hue=0.01),
    T.ToPILImage()
])'''

#transform 8
transform = T.Compose([
    T.RandomRotation(30),
    T.ColorJitter(brightness=0.2, contrast=0.4, saturation=0.1, hue=0.02),
])

#transform 9
transform = T.Compose([
    T.ToTensor(),
    T.RandomErasing(p=0.75, scale=(0.01, 0.02), ratio=(0.3, 3.3)),
    T.ColorJitter(brightness=0.5, contrast=0.0, saturation=0.3, hue=0.03),
    T.ToPILImage()
    
])



folder_count = 45
prefix_previous = 0
aux_count = 1351

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
            class_name = name.split('_')[0]
            #aux = file_name.split('_')[-1].split('.')[0]
            imgpath = os.path.join(root, file_name)
            img = Image.open(imgpath)
            img = transform(img)
            dest_imgpath = os.path.join(new_folder_path, f"{class_name}_{aux_count}_a.jpg")
            img.save(dest_imgpath)
            aux_count += 1
    
    prefix_previous = prefix
    #aux_count += 1
    
        

