# SelfExt
[![Build](https://api.travis-ci.org/kazukazuprogram/selfext.svg?branch=master)](https://travis-ci.org/kazukazuprogram/selfext/)
## A Python library that generates self-extracting Python script.

 - ### How to Use
  - Install
     ```
     pip install git+https://github.com/kazukazuprogram/selfext
     ```
  - To generate a self-extracting script,
    ```
    import selfext
    selfext.gen(compdir, outfile)
    ```
    compdir : Compression source directory
    outfile : Name of generated file