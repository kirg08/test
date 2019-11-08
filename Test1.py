import os
import shutil
directory = '\\\\10.180.32.1\c$\\Users'
dir_user = []
files = os.listdir(directory)
for dir in files:
    if "-" in dir:
        path = directory + "\\" + dir + "\\AppData\\Local\\Lotus\\Notes\\"
        if os.path.isdir(path):
            shutil.copyfile(r"test.ini", path + r"test.ini")
            os.rename(path + r"test.ini", path + r"test_old.ini")
            print(path)


#except:
    #print("Connection failed")
