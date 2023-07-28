import os
folders=os.listdir("song")
print(folders)
# for folder in folders:
#     print(folder)
#     # print(os.listdir(f"song/{folder}"))
os.rename("song","music")
