import os

# Specify the directory path where your files are located
directory_path = "/Users/ruipedro/Desktop/GTSRB"

# Initialize a dictionary to store the counts for each prefix
counts = {}

# Iterate over the files in the directory
for filename in os.listdir(directory_path):
    # Get the prefix of the current file
    prefix = filename.split("_")[0]
    # If the prefix isn't in the dictionary, initialize the count to 0
    if prefix not in counts:
        counts[prefix] = 0
    # Increment the count for the current prefix
    counts[prefix] += 1

# Print the counts for each prefix
for prefix, count in counts.items():
    print("Number of files with prefix '{}': {}".format(prefix, count))