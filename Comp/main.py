#!/usr/bin/env python3
#coding: utf-8

from base64 import b85encode
from glob import glob
from tempfile import mkdtemp
from os.path import join
from ZipFile import write, setpassword
from random import choice

samplefilepath = "./sample.py"
compdir = "./Comp/"

def mkrand():
    r = ""
    s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
    for x in range(64):
        r += choice(s)
    return r

def encode(path):
    with open(path, "rb") as f:
        DATA = f.read()
    DATA = b85encode(DATA)
    DATA = str(DATA)[2:-1]
    DATA = '\n'.join([DATA[i: i+80] for i in range(0, len(DATA), 80)])
    return DATA

def make_extfile(path, output_fn="Ext_fn.py"):
    if len(path) == 0:
        raise FileNotFoundError('Compressed file not found.')
    else:
        path = path[0]
    DATA = encode(path)
    with open(samplefilepath) as f:
        r = f.read()
    r = r.replace("ENCODED_DATA", DATA)
    r = r.replace("FILENAME", path[2:])
    with open(output_fn.replace("fn", path.split('.')[0]), "w") as f:
        f.write(r)

def make_zip():
    setpassword(mkrand())
    path = mkdtemp()+".zip"
    write(path, mode='w')

make_zip()
exit()
if __name__ == "__main__":
    main()
