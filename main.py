#!/usr/bin/env python3
#coding: utf-8

from Lib.base64 import b85encode
from Lib.glob import glob
from Lib.zipfile import ZipFile
from Lib.random import choice

from tempfile import mkdtemp
from os.path import join, basename
from os import remove

samplefilepath = "./sample.py"
compdir = "./Comp/"

def encode(path):
    with open(path, "rb") as f:
        DATA = f.read()
    DATA = b85encode(DATA)
    DATA = str(DATA)[2:-1]
    DATA = '\n'.join([DATA[i: i+80] for i in range(0, len(DATA), 80)])
    return DATA

def make_extfile(path, output_fn="Ext.py"):
    DATA = encode(path)
    with open(samplefilepath) as f:
        r = f.read()
    r = r.replace("ENCODED_DATA", DATA)
    r = r.replace("FILENAME", basename(path[2:]))
    with open(output_fn, "w") as f:
        f.write(r)

def make_zip():
    global zippath
    zippath = mkdtemp()+".zip"
    with ZipFile(zippath, 'w') as new_zip:
        for x in glob(compdir+"*"):
            new_zip.write(x, arcname=x)

def main():
    make_zip()
    make_extfile(path=zippath)
    remove(zippath)

if __name__ == "__main__":
    main()
