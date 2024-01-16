import os
import shutil

# Get file location from the user
path = input("Enter the file location: ").strip('"')

# Check if the provided path is valid
if not os.path.exists(path):
    print("Invalid path. Please provide a valid path.")
    exit()

# List files in the specified path
list_of_files = os.listdir(path)

# Organize files based on their extensions
for file in list_of_files:
    name, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(os.path.join(path, extension)):
        shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
    else:
        os.makedirs(os.path.join(path, extension))
        shutil.move(os.path.join(path, file), os.path.join(path, extension, file))

print("Files organized!")
