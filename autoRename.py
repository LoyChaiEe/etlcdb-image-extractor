import os
import shutil

# Define the path to the ETL4 directory
etl4_path = 'etl_data/images/ETL4'

# Loop over each subdirectory in the ETL4 directory
for subdir_name in os.listdir(etl4_path):
    subdir_path = os.path.join(etl4_path, subdir_name)

    # Check if the subdirectory is actually a directory and not a file
    if os.path.isdir(subdir_path):

        # Read the character from the .char.txt file
        char_file_path = os.path.join(subdir_path, '.char.txt')
        try:
            with open(char_file_path, 'r') as f:
                char = f.read().strip()
        except FileNotFoundError:
            print(f"Warning: {char_file_path} does not exist")
            continue

        # Rename the subdirectory to the character
        new_subdir_path = os.path.join(etl4_path, char)
        shutil.move(subdir_path, new_subdir_path)

        # Loop over each image in the subdirectory
        i = 1
        for img_name in sorted(os.listdir(new_subdir_path)):
            img_path = os.path.join(new_subdir_path, img_name)

            # Rename the image to the character followed by an index
            new_img_name = f"{char}_{i:02}.png"
            new_img_path = os.path.join(new_subdir_path, new_img_name)
            shutil.move(img_path, new_img_path)

            i += 1
