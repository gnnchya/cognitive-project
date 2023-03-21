import os

folder_path = "/Users/gnnchya/Documents/Bowl"  # Replace with the path to your folder
prefix = "Bowl"

# Get a list of all JPG and PNG files in the folder
file_list = [f for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png")]

# Rename each file with the prefix and a suffix number
for i, file_name in enumerate(file_list):
    # Get the file extension
    file_ext = os.path.splitext(file_name)[1]
    
    # Construct the new file name with prefix and suffix
    new_file_name = prefix + str(i + 1) + file_ext
    
    # Rename the file
    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))