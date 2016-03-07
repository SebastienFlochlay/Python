#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
import time
from PIL import Image
 
def compfichiers(nfc1, nfc2, lgbuf=32*1024):
    """Compare les 2 fichiers et renvoie True seulement s'ils ont un contenu identique"""
    f1 = f2 = None
    result = False
    try:
        if os.path.getsize(nfc1) == os.path.getsize(nfc2):
            with open(nfc1, "rb") as f1, open(nfc2, "rb") as f2:
                while True:
                    buf1 = f1.read(lgbuf)
                    if len(buf1) == 0:
                        result = True
                        break
                    buf2 = f2.read(lgbuf)
                    if buf1 != buf2:
                        break
    except:
        if f1 != None: f1.close()
        if f2 != None: f2.close()
        raise IOError
    return result

def compimages(nfc1, nfc2):
    """Compare les 2 fichiers et renvoie True seulement s'ils ont un contenu identique"""
    im1 = im2 = None
    result = False
    try:
        if os.path.getsize(nfc1) == os.path.getsize(nfc2):
            with Image.open(nfc1) as im1, Image.open(nfc2) as im2:
                print("\t", nfc1, im1.format, "%dx%d" % im1.size, im1.mode)
                print("\t", nfc2, im2.format, "%dx%d" % im2.size, im2.mode)
                if list(im1.getdata()) == list(im2.getdata()):
                    result = True
    except:
        if f1 != None: f1.close()
        if f2 != None: f2.close()
        raise IOError
    return result

# 1er cas: les 2 fichiers sont identiques 
nf1 = r"C:/Python/Exemple/006.png"
nf2 = r"C:/Python/Exemple/007.png"

try:
    t = time.clock()
    result = compfichiers(nf1, nf2)
    t = time.clock()-t
    print("Résultat: \t", result, " %.3f s" % t)


    t = time.clock()
    result = compimages(nf1, nf2)
    t = time.clock()-t
    print("Résultat PIL: \t", result, " %.3f s" % t)

except:
    t = time.clock()-t
    print("Résultat: Erreur", " %.3f s" % t)


# # 2ème cas: les 2 fichiers sont différents 
# nf1 = r"C:\Python25\DLLs\tk84.dll"
# nf2 = r"C:\Python25\DLLs\unicodedata.pyd"
# try:
#     t = time.clock()
#     result = compfichiers(nf1, nf2)
#     t = time.clock()-t
#     print u"Résultat:", result, "%.3f s" % t
# except:
#     t = time.clock()-t
#     print u"Résultat: Erreur", "%.3f s" % t

# # 3ème cas: le second fichier n'existe pas
# nf1 = r"C:\Python25\DLLs\tk84.dll"
# nf2 = r"C:\Python25\DLLs\cefichiernexistepas.$$$"
# try:
#     t = time.clock()
#     result = compfichiers(nf1, nf2)
#     t = time.clock()-t
#     print u"Résultat:", result, "%.3f s" % t
# except:
#     t = time.clock()-t
#     print u"Résultat: Erreur", "%.3f s" % t