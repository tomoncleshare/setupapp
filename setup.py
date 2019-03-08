#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-5-12 下午1:33
# @Author         : Tom.Lee
# @Description    : 
# @File           : setup.py
# @Product        : PyCharm
from setuptools import setup, find_packages

setup(
    name='setupapp',
    version='0.0.1',
    author='tomoncle',
    author_email='1123431949@qq.com',
    url='https://github.com/tomoncleshare/setupapp',
    description='simple demo for python setup, author tom',
    long_description=open("README.rst").read(),
    license="MIT",
    install_requires=[
        'docopt'
    ],
    packages=find_packages(),
    entry_points={
        # console_scripts  输出脚本文件
        # setupapp         输出脚本文件名称
        # applib.bin:run   模块名:函数名　
        'console_scripts': ['setupapp = applib.bin:run']
    },
)
