import os, shutil
from variables_module import downloads, extensions

os.chdir(downloads)

files = os.listdir()

def sorting(file):
    keys = list(extensions.keys())
    for key in keys:
        for ext in extensions[key]:
            if file.endswith(ext):
                return key

for file in files:
    dist = sorting(file)
    if dist:
        try:
            shutil.move(file, "..\\download-sorting\\" + dist)
        except:
            print(file + " already exists.")
    
    else:
        try: 
            shutil.move(file, "..\\download-sorting\\others")
        except:
            print(file, " already exists.")
