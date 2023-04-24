import os
from PIL import Image

# set the path to the parent folder containing subfolders with images
parent_folder = "etl_data/imagesCopy/ETL5"

# loop through each subfolder
for folder_name in os.listdir(parent_folder):
    folder_path = os.path.join(parent_folder, folder_name)
    
    # check if the subfolder is actually a folder (not a file)
    if os.path.isdir(folder_path):
        # initialize a counter to keep track of valid images
        count = 1
        
        # create a dictionary to store the original file names and their corresponding new names
        new_names = {}
        
        # loop through each file in the subfolder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            # check if the file is actually an image file
            if file_name.endswith(".png") or file_name.endswith(".jpg"):
                try:
                    # try to open the image file and check if it's valid
                    with Image.open(file_path) as img:
                        img.verify()
                    
                    # if the image file is valid, generate the new name and store it in the dictionary
                    new_file_name = folder_name + "_" + str(count) + ".png"
                    new_file_path = os.path.join(folder_path, new_file_name)
                    new_names[file_name] = new_file_name
                    
                    # increment the counter for valid images
                    count += 1
                
                # if the image file is invalid (i.e. can't be opened or parsed correctly), delete it
                except (OSError, Image.DecompressionBombError):
                    os.remove(file_path)
        
        # loop through the dictionary and rename the valid images with their new names
        for old_name, new_name in new_names.items():
            old_path = os.path.join(folder_path, old_name)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)

