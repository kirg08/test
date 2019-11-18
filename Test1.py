import os
import shutil

for i in range(5): #range(5) - до какого IP производить копирование, последний IP не попадпет
    try:
        directory = '\\\\10.180.32.'+str(i)+'\c$\\Users'
        dir = []
        f = []
        files = os.listdir(directory)
        for dir in files:
            if "-" in dir:
                path = directory + "\\" + dir + "\\AppData\\Local\\Lotus\\Notes\\Data\\"
                if os.path.isdir(path):
                    for id_file in os.listdir(path):
                        if id_file.endswith(".id"):
                            os.rename(path + id_file, path + id_file + ".old")
                    os.rename(path + r"names.nsf", path + r"names_old.nsf")
                    os.rename(path + r"notes.ini", path + r"notes_old.ini")
                    notesini = open(path + r"notes.ini", "w")
                    notesini.write("[Notes]\nKitType=1\nDirectory=C:\\Users\\" + dir + "\\Lotus\\Notes\\data\nUserInterface=ru\nInstallType=6\nMailServer=CN=S5200-LT01/O=Saratov")
                   # shutil.copyfile(r"test.ini", path + r"test.ini")
                   # os.rename(path + r"test.ini", path + r"test_old.ini")
                    print(path)
    except:
        print("Connection failed")
        file = open("Connection_failed.txt", "w")
        file.write(directory)
        file.close()
        continue