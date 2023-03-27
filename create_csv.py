import os 
import shutil
from random import uniform
import csv
import random
from random import uniform

directory = "Dataset_Final_Augmentation/"
output_csv_train = "train.csv"
output_csv_test = "test.csv"
output_csv_validation = "validation.csv"

learning_set = 0.8
validation_set = 0.1

def get_sub_folders(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

def get_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]  

def write_csv(csv_file, label, list_of_files):
    with open(csv_file, 'a+') as f:
        for file_name in list_of_files:
            f.write("{},{}\n".format(file_name,label))

if __name__ == "__main__":

    subfolders = get_sub_folders(directory)
        # List all sub-folders in the parent director
    
    for name_fold in subfolders:
        label = name_fold.split('/')[-1]
        sub_sub_folders = get_sub_folders(name_fold)

        for folder in sub_sub_folders:
            #print(folder)
            randvalue = random.uniform(0,1)

            if randvalue < learning_set:
                outputcsv = output_csv_train
            elif learning_set < randvalue < learning_set + validation_set:
                outputcsv = output_csv_validation
            else:
                outputcsv = output_csv_test

            '''
            if (randvalue < learning_set):
                outputcsv = output_csv_train
            else:
                outputcsv = output_csv_test
            '''
            
            sub_sub_folders_files = get_files(folder)
            #print(sub_sub_folders_files, outputcsv)
            write_csv(outputcsv, label, sub_sub_folders_files)
            