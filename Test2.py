import os
try:
    directory = '\\\\10.180.40.57\\d$\\Users\\'
    dir = ()
    f = []
    files = os.listdir(directory)
    for dir in files:
        if "-" in dir and "V2" not in dir:
            path = directory + "\\" + dir + "\\Lotus\\Data\\"
            if os.path.isdir(path):
                for id_file in os.listdir(path):
                    if id_file.endswith(".id"):
                        os.rename(path + id_file, path + id_file + ".old")
            os.rename(path + r"names.nsf", path + r"names_old.nsf")
            path2 = directory + "\\" + dir + "\\Lotus\\"
            if os.path.isdir(path2):
                os.rename(path2 + r"notes.ini", path + r"notes_old.ini")
                notesini = open(path2 + r"notes.ini", "w")
                notesini.write("[Notes]\nKitType=1\nDirectory=\\\\S5200-TS03\\users\\" + dir + "\\Lotus\\data\nUserInterface=ru\nInstallType=6\nMailServer=CN=V5200-LT01/O=Saratov")

except:
    print("Connection failed")
    file = open("Connection_failed.txt", "w")
    file.write(directory)
    file.close()