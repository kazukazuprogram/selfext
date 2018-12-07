#!/usr/bin/env python3
#coding: utf-8

from base64 import b85decode
from zipfile import ZipFile
from os import remove

fn = "FILENAME"

def main(DATA):
    with open(fn, "wb") as fp:
        fp.write(b85decode(DATA.replace(b"\n", b"")))
    with ZipFile(fn) as zip:
        zip.extractall(".")
    remove(fn)

DATA = b"""
ENCODED_DATA
"""

if __name__ == "__main__":
    main(DATA)
