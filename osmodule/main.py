import os
if(not os.path.exists("song")):
 os.mkdir("song")
# for i in range(0,10):
#  os.mkdir(f"song/fav{i}")
folders=os.listdir("song")
for folder in folders:
  print(folder)

