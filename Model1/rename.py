import glob;
import os
import shutil
k=1
f=[]
for i in glob.glob(os.getcwd()+"/train/*"):
    f.append(i)
for i in f:    
    print(k)
    src = i;
    dst = i.split(".")[0]+"."+i.split(".")[-1];
    shutil.move(src,dst)
    k+=1
    # print(src,"-------",dst)