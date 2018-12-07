#!/usr/bin/env python3
#coding: utf-8

from base64 import b85decode

def main(DATA):
    with open("sample.py", "wb") as fp:
        fp.write(b85decode(DATA.replace(b"\n", b"")))

DATA = b"""
BOxz!b8;_YX>KoNZgwDWd30!RZZi!EBV%u5X>MmaAa!(REjSGd4GLy*Z*3rAVRL0RG$3hhaBp&SAYwQ*
WMyM-WMvHs4GLssW*}{0X>KS)K~zC0It>aSARr)jX>@2HZ*XO9C?Z8pR7Fx>MoCOXPC-pYUr0q#MItO9
B6ngUDIj5UAZBnn4GJJ2ARr(hARuONE_ZTibY&=FI5lKtV{c?-C`3V2K`wG-aBN{?Whi1ITy7#PAYvjS
DJdxp3JnTGK~zB?Js@HtA|ee6MNU*jQeQ<*Lr+9SL|;TfR6$=zMN&l#3L+vR4GIkkX=Wf_Uv6P-WnW()
Jv|^IUteuuX>MO%B03EUARr(hZDDC{C`3V2K`9Li
"""

if __name__ == "__main__":
    main(DATA)
