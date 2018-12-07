#!/usr/bin/env python3
#coding: utf-8

from base64 import b85decode

def main(DATA):
    with open("FILENAME", "wb") as fp:
        fp.write(b85decode(DATA.replace(b"\n", b"")))

DATA = b"""
ENCODED_DATA
"""

if __name__ == "__main__":
    main(DATA)
