# SelfExt
[![Build](https://api.travis-ci.org/kazukazuprogram/selfext.svg?branch=master)](https://travis-ci.org/kazukazuprogram/selfext/)[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)[![Coverage Status](https://coveralls.io/repos/github/kazukazuprogram/selfext/badge.svg?branch=master)](https://coveralls.io/github/kazukazuprogram/selfext?branch=master)[![Maintainability](https://api.codeclimate.com/v1/badges/472109fcd9cbb14245b9/maintainability)](https://codeclimate.com/github/kazukazuprogram/selfext/maintainability)[![Test Coverage](https://api.codeclimate.com/v1/badges/472109fcd9cbb14245b9/test_coverage)](https://codeclimate.com/github/kazukazuprogram/selfext/test_coverage)
## A Python library that generates self-extracting Python script.

 - ### How to Use
  - Install
     ```
     pip install selfext
     ```
     OR
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