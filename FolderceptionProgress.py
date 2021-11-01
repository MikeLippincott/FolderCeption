#!/usr/bin/env python
# coding: utf-8
import os
from tkinter.filedialog import askdirectory


def progress(path, subpath):
    subpath = str(subpath).split('/')[-1]
    paths = [f.path for f in os.scandir(path) if f.is_dir()]
    lst = []
    done = 0
    notdone = 0
    for i in paths:
        i = i+f'{subpath}'#Files within folders of folder
        paths1 = [f.path for f in os.scandir(i) if f.is_dir()]
        for j in paths1:
            lst.append(j)
            dircont = os.listdir(j)
            if len(dircont) < 1:
                notdone += 1
            else:
                done += 1
        per = f'{round((done/(done+notdone)*100),2)} % Complete' #done/total
    print(f'{done} complete')
    print(f'{notdone} not complete')
    print(per)


def main():
    destination = askdirectory() #get directory of parent folder
    subdestination = askdirectory() #get directory of folder within parent folder which contains folders of interst #folderception
    progress(destination, subdestination)


if __name__ == "__main__":
    main()
