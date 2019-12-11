import os, shutil

x = os.listdir('./audio_dataset/')
"""get filename"""
names = []
for idx in x:
    x = idx.split("_")
    name = (x[0] + "_" + x[1])
    if(name in names):
        pass
    else:
        names.append(name)
# make new directorys accordingly
for i in names:
    os.mkdir("./%s/" % i)

y = os.listdir(".")

path = "./audio_dataset/"
files = os.listdir(path)
files.sort()

for f in files:
    src = path+f
    x = f.split("_")
    if(x[0] == "audio"):
        pass
    else:
        name = (x[0] + "_" + x[1])
        moveto = ("./%s/" % name )
        print(moveto+f) 
    
        dst = moveto+f
        shutil.move(src,dst)



# for i in names:
#     os.mkdir("./%s/" % i)


