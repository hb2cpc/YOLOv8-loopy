# 该文件夹下的jpg文件重命名，从001.jpg开始
import os

path = "labels"
files = os.listdir(path)
files.sort()
for i, file in enumerate(files):
    os.rename(
        os.path.join(path, file), os.path.join(path, str(i + 1).zfill(3) + ".txt")
    )
print("done")
