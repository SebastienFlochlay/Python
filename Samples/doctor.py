import pathlib
import os
import os.path
import fnmatch
import shutil
import zipfile
import re
import pdb

from datetime import datetime
# http://www.python-simple.com/
# pdb.set_trace()

def getConfig():
    """Get config"""
    return


def createResultFile(path):
    """Create result file"""

    viewLineType = "*"
    viewLineNumber = 50

    with open(path, 'w') as result:
        result.write ("\n\t\t" + viewLineType * viewLineNumber + "\n")
        result.write("\t\t" + "Doctor CRE report".center(viewLineNumber) + "\n")
        result.write("\t\t" + viewLineType * viewLineNumber + "\n\n\n")
    return


def log(path, message):
    """Log information in result file"""
    print("Log : " + message)
    with open(path, 'a') as result:
        result.write (message + "\n")
    return


def dezip(filezip, pathdst = ''): 
    if pathdst == '': pathdst = os.getcwd()  ## on dezippe dans le repertoire locale 
    # zfile = zipfile.ZipFile(filezip, 'r')
    # for i in zfile.namelist():  ## On parcourt l'ensemble des fichiers de l'archive 
    #     print(i)
        # if os.path.isdir(i):   ## S'il s'agit d'un repertoire, on se contente de creer le dossier 
        #     try: os.makedirs(pathdst + os.sep + i) 
        #     except: pass 
        # else: 
        #     try: os.makedirs(pathdst + os.sep + os.path.dirname(i)) 
        #     except: pass 
        #     data = zfile.read(i)                   ## lecture du fichier compresse 
        #     fp = open(pathdst + os.sep + i, "wb")  ## creation en local du nouveau fichier 
        #     fp.write(data)                         ## ajout des donnees du fichier compresse dans le fichier local 
        #     fp.close()
    # zfile.close() 

    # Clean previous unzip
    try:
        targetDirectory = os.path.splitext(filezip)[0]
        if os.path.exists(targetDirectory):
            shutil.rmtree(targetDirectory)
    except Exception as ex:
        print("Error during unzip phase : ", ex)
        exit()

    with zipfile.ZipFile(filezip, 'r') as zfile:
        for i in zfile.namelist():
            path = pathdst + os.sep + i
            print(path)
            if os.path.isdir(path):
                print("    -> Is a directory")
                try: os.makedirs(pathdst + os.sep + i)
                except: pass
            else:
                print("    -> Is a file")
                try: os.makedirs(pathdst + os.sep + os.path.dirname(i))
                except: pass 
            #     data = zfile.read(i)
            #     newFile = os.path.join(pathdst, i)
            #     print(i)
            #     pdb.set_trace()
            #     fp = open("C:\Ticket\Basis\demo.txt", "wb")  ## creation en local du nouveau fichier 
            #     fp.write(data)                         ## ajout des donnees du fichier compresse dans le fichier local 
            #     fp.close()
            #     exit()
                # pdb.set_trace()
                # with open(newFile, "w") as tmpFile:
                #     tmpFile.write(data)


def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)


# Define static
ietpDirectory ="C:/TURBOMECA/TURBOMECA_IETP"

# Get result file path
# resultFilePath = os.path.join(os.getcwd(), "IETP_Doctor_" + datetime.now().strftime('%Y%m%d_%H%M%S.cre'))
resultFilePath = os.path.join(os.getcwd(), "doctor.txt")

# Create the result file path
createResultFile(resultFilePath)

# Get config file path
configFilePath = os.path.join(os.getcwd(), "doctor.properties")

# Check config file existance
if not os.path.exists(configFilePath):
    log(resultFilePath, "Config file doesn't exist. Please check if 'doctore.properties' really exist.")
    exit()

# Check config file conformity


# Check viewer installation directory
if not os.path.exists(os.path.join(ietpDirectory, "viewer/logs/compliance.log")):
    log(resultFilePath, "Viewer installation directory does not contain the 'compliance.log' file.")
    exit()
if not os.path.exists(os.path.join(ietpDirectory, "viewer/logs/doctor.log")):
    log(resultFilePath, "Viewer installation directory does not contain the 'doctor.log' file.")
    exit()

# Clean all previous unziped doctor zip file
doctorElementList = fnmatch.filter(os.listdir(ietpDirectory), 'IETP_Doctor_*')
print(doctorElementList)
for doctorElement in doctorElementList:    
    elementPath = os.path.join(ietpDirectory, doctorElement)
    if os.path.isdir(elementPath):
            shutil.rmtree(elementPath)

# Get all doctor zip file
doctorZipFile = fnmatch.filter(os.listdir(ietpDirectory), 'IETP_Doctor_*.zip')

# Verify expected number of doctor zip file
# if len(doctorZipFile) != 3:
#     log(resultFilePath, "Not enought zip file.")
#     exit();

regex = re.compile('IETP_Doctor_(\\d{4})(\\d{2})(\\d{2})_(\\d{2})(\\d{4})')

# Unzip all doctor zip file
for zipFile in doctorZipFile:
    result = regex.search(zipFile)
    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    day = datetime.now().strftime('%d')
    # datetime.now().strftime('%Y%m%d_%H%M%S')
    if result:
        print("OK -> " + zipFile + "\t" + year + "/" + month + "/" + day)
    else:
        print("KO -> " + zipFile)

    zipFilePath = os.path.join(ietpDirectory, zipFile)
    unzip(zipFilePath, ietpDirectory)

# 
exit()
doctorElementList = fnmatch.filter(os.listdir(ietpDirectory), 'IETP_Doctor_*[!zip]')
doctorElementList.sort()
print(doctorElementList)


# Check ietp viewer logs \viewer\logs





exit()

print(configFilePath)
print(resultFilePath)

try:
    # Get config
    with open(configFilePath) as properties:
        for ligne in properties:
            if "#" not in ligne and ligne != "" and "=" in ligne:
                print(ligne)

    with open(resultFilePath, 'w') as result:
        result.write("Test")

except EnvironmentError as e:
    print("Unable to open properties file:", e)