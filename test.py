import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(APP_ROOT, 'files/')
filelist = os.listdir(target)
files = []
for file in filelist:
    if not file.endswith("__preview.jpg") :
        files.append(file)
print(files)