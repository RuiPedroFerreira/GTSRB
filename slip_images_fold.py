import os
import shutil

# Specify the directory path where your files are located
directory_path = "/Users/ruipedro/Desktop/GTSRB"

dest_path = "/Users/ruipedro/Desktop/Dataset_Final"

# Initialize a dictionary to store the counts for each prefix
file_dict = {}

files_per_fold = 30 
file_count = 0
folder_count = 0
auxPrefix = 0


# Iterate over the files in the directory
for file_name in os.listdir(directory_path):
    # Get the prefix of the current file
    prefix = file_name.split("_")[0]
    # If the prefix isn't in the dictionary, initialize the count to 0
    # if the class is not already a key in the dictionary, create a new key-value pair
    if prefix not in file_dict:
        file_dict[prefix] = []
    # add the file name to the list of file names for the class
    file_dict[prefix].append(file_name)

# sort the files in each class by the integer value in the file name
for class_name in file_dict:
    #print(class_name)
    file_dict[class_name] = sorted(file_dict[class_name], key=lambda x: int(x.split('_')[1].split('.')[0]))

        
# concatenate the sorted files into a single list in the order of the class keys
ordered_files = [file_name for class_name in sorted(file_dict.keys()) for file_name in file_dict[class_name]]

# print the ordered list of file names
#print(ordered_files)

previous_prefix = None
for file_name in ordered_files:
    
    print(file_name)
    file_path = os.path.join(directory_path, file_name)
   
    # Get the prefix of the current file
    prefix = file_name.split("_")[0]

    if prefix != previous_prefix:
        folder_count = 0

    if file_count % files_per_fold == 0:
        folder_count += 1
        new_folder_path = os.path.join(dest_path, f"{prefix}//{prefix}_{folder_count}")
        os.makedirs(new_folder_path)
    
    #copy the file to new folder
    new_file_path = os.path.join(new_folder_path, file_name)
    shutil.copy2(file_path, new_file_path)
        
    # Increment the file count
    file_count += 1
    previous_prefix = prefix
