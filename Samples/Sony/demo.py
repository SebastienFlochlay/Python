import os
import re
import pdb


path = "D:\Photographie\DSC-HX100V"
os.chdir(path)

def renameFiles(path, prefix):
    """Rename files"""
    currentPath = os.getcwd()
    os.chdir(path)
    for fileEntry in os.scandir(path):
        if fileEntry.is_file():
            print(" ", fileEntry.name)
            newName = prefix + " - " + fileEntry.name
            os.rename(fileEntry.name, newName)
            # print("\t\t  ",fileEntry.name)
    os.chdir(currentPath)
    return

regex = re.compile('(\\d{2})-(\\d{2})-(\\d{4})')

try:
    with open("../demo.txt", 'w') as dest:
        for entry in os.scandir(path):
            if entry.is_dir():
                result = regex.search(entry.name)
                print(entry.name)
                log = entry.name
                if result:
                    cleanName = "{0}-{1}-{2}".format(result.group(3), result.group(2), result.group(1))
                    # print(" ", cleanName)
                    renameFiles(entry.path, cleanName)
                    os.rename(entry.name, cleanName)
                    # log += " -> " + cleanName
                dest.write(log + "\n")
            elif entry.is_file():
                dest.write("\t" + entry.name + "\n")

except EnvironmentError as e:
    print("Unable to open the destination file: ", e)