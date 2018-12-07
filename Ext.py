
#!/usr/bin/env python3
#coding: utf-8

from base64 import b85decode
from zipfile import ZipFile
from os import remove

fn = "tmpkdo52npc.zip"

def main(DATA):
    with open(fn, "wb") as fp:
        fp.write(b85decode(DATA.replace(b"
", b"")))
    with ZipFile(fn) as zip:
        zip.extractall(".")
    remove(fn)

DATA = b"""
P)h>@6aWAK008I-h)n<h0000000000000F5003lfV{<Q1O9KQH0000007VLjO#lD@000000000000;m8
0CQz*W@UJEFHlPZ1QY-O0002235ZP$#y@2S0RR970RR990001UWps6LE^v7xA$4<dFJftKFJ*3aAaHqf
Xm4%}3L|50WNB_^Iv{m)W-T}k3JnToa&K)Qb7gdOaCC2PY;z!KZE$aLbRctObaiknAZBT9WM6P$V{2h&
WpfP*4GME*baikjZeeX@JtA{uY-VM6bRsMb3JG>)a&u{KZapF}E-)@IA}kFG31nq+V{&P5bZKvHJt9YC
Ze?;|bY&oOWo%|GWq5RQVPkY@Zf78KV{&P5bS@$+4GIZ$a%?>!XmoUNb2=|CXK8e3bz&}KZ*4DYVS06I
VS06Na&KpHVQnvSWo%|;cyuBx4GIZxVPk7yXJvCeW@&C@UvOb#Yhh<)b0{e+4GJj@3Q$V{0u%rg00000
0O$#bO#lD@000000000000jU5000000000G0RKS%0001FZ)0;WP)h*<6aW+e00000MGA;b0000000000
000002mk;800000000mG|3M=F0047kY-VM6bT3d#0Rj{N6aWAK0068Bh)oQ}KV=31000I7000O800000
00000006duNdN!<b7gdOa4v9pP)h{{000000{{a6p8x;=bpZeX000
"""

if __name__ == "__main__":
    main(DATA)
