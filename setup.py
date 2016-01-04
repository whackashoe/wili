#!/usr/bin/env python2.7

from setuptools import setup

setup(
    name="wili",
    version="0.0.1",
    url="https://github.com/whackashoe/wili",
    license="LICENSE.txt",

    author="whackashoe",
    author_email="whackashoe@gmail.com",

    packages=["wili"],
    include_package_data=True,
    description="Wireless Library",
    long_description=open("README.md").read(),

    install_requires=[
        "web.py",
    ],
)
