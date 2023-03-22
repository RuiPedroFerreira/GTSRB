
import os 
import shutil


directory = '/Users/ruipedro/Desktop/Dataset_Final_v2'

subfolders = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

aux_name = None

repeat_list = []
for subfolder in subfolders:
    for file in os.listdir(subfolder):
        if file == aux_name:
            repeat_list.append(file)
        aux_name = file # Update aux_name for the next iteration

print(len(repeat_list))
