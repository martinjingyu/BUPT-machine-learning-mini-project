import os
import tarfile
def un_tar(file_name,new_name):  
    tar = tarfile.open(file_name)  
    names = tar.getnames()  
    if os.path.isdir(new_name + "_files"):  
        pass  
    else:  
        os.mkdir(new_name + "_files")  
    #由于解压后是许多文件，预先建立同名文件夹  
    for name in names:  
        tar.extract(name, new_name + "_files/")  
    tar.close()  