import os
import shutil

for i in range(5):
    try:
        directory = '\\\\10.180.32.'+str(i)+'\c$\\Users' #Добавить \\Data
        dir = []
        files = os.listdir(directory)
        for dir in files:
            if "-" in dir:
                path = directory + "\\" + dir + "\\AppData\\Local\\Lotus\\Notes\\"
                if os.path.isdir(path):
                    shutil.copyfile(r"test.ini", path + r"test.ini")
                    os.rename(path + r"test.ini", path + r"test_old.ini")
                    print(path)
    except:
        print("Connection failed")
        file = open("Connection_failed.txt", "w")
        file.write(directory)
        file.close()
        continue