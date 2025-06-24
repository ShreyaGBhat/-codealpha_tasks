import os
import shutil
import re

source_folder = r'C:\Users\shrey\OneDrive\Desktop\OldPhotos'
destination_folder = r'C:\Users\shrey\OneDrive\Desktop\NewPhotos'
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):
    if re.search(r'\.jpeg$', filename, re.IGNORECASE):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")
