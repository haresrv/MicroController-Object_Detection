import glob;
# import os
# import shutil
# k=1
# f=[]
# for i in glob.glob(os.getcwd()+"/train/*"):
#     f.append(i)
# for i in f:    
#     print(k)
#     src = i;
#     dst = i.split(".")[0]+"."+i.split(".")[-1];
#     shutil.move(src,dst)
#     k+=1
#     # print(src,"-------",dst)


import xml.dom.minidom as md 
  
def main(): 
    k=0
    for i in glob.glob("data/images/train/*.xml"):
        
        file = md.parse(i) 
        fname = file.getElementsByTagName("filename")
        pathx = file.getElementsByTagName("path")
        rep = pathx[0].childNodes[0].nodeValue.split(".")[0]+"."+pathx[0].childNodes[0].nodeValue.split(".")[-1]
        
        pathx[0].childNodes[0].nodeValue = rep
        fname[0].childNodes[0].nodeValue = rep
        with open(i, "w" ) as fs:  
            fs.write( file.toxml() ) 
            fs.close()  
        print(k)
        k+=1
if __name__=="__main__": 
    main(); 
