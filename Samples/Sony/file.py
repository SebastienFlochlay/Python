#!/usr/bin/python

import os
import re
import pathlib
import pdb

# os.rename(current_file_name, new_file_name)
# os.remove(file_name)
# os.mkdir("newdir")
# os.getcwd()
# os.rmdir('dirname')

# name : the entry's filename, relative to the scandir path argument (corresponds to the return values of os.listdir )
# path : the entry's full path name (not necessarily an absolute path) -- the equivalent of os.path.join(scandir_path, entry.name)
# inode() : return the inode number of the entry. The result is cached on the DirEntry object, use os.stat(entry.path, follow_symlinks=False).st_ino to fetch up-to-date information. On Unix, no system call is required.
# is_dir(*, follow_symlinks=True) : similar to pathlib.Path.is_dir() , but the return value is cached on the DirEntry object; doesn't require a system call in most cases; don't follow symbolic links if follow_symlinks is False
# is_file(*, follow_symlinks=True) : similar to pathlib.Path.is_file() , but the return value is cached on the DirEntry object; doesn't require a system call in most cases; don't follow symbolic links if follow_symlinks is False
# is_symlink() : similar to pathlib.Path.is_symlink() , but the return value is cached on the DirEntry object; doesn't require a system call in most cases
# stat(*, follow_symlinks=True) : like os.stat() , but the return value is cached on the DirEntry object; does not require a system call on Windows (except for symlinks); don't follow symbolic links (like os.lstat() ) if follow_symlinks is False







path = "D:\Python\Sony\sample"
os.chdir(path)
# pdb.set_trace()

# filenames = os.listdir(path)
# for filename in filenames:
#     # os.rename(filename, filename.replace(" ", "-").lower())
#     print (filename)

# dossier = pathlib.Path(path)

# on créé un dictionnaire qui va contenir le compte
# de chaque mot que nous allons rencontrer
stats = {}

help(demo)
result = demo(14, 6)
print(result)


# on itère sur tous les fichiers présents dans ce dossier
# for chemin in dossier.iterdir():
#     print(chemin)
#     print("\t", chemin.name)
#     print("\t", chemin.stem)

folders = []
files = []
regex = re.compile('(\\d{2})-(\\d{2})-(\\d{4})')

for entry in os.scandir(path):
    if entry.is_dir():
        # print("\t", entry.name)
        # print("\t\t-", entry.path)
        result = regex.search(entry.name)
        os.rename(entry.name, "{0}-{1}-{2}".format(result.group(3), result.group(2), result.group(1)))
        folders.append(entry.path)
    elif entry.is_file():
        files.append(entry.path)
 
print('Folders:')
print(folders)
print('Files:')
print(files)

# os.rename(current_file_name, new_file_name)

