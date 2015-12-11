#!/usr/bin/env python2.7

from setuptools import setup

setup(
    name="mediaserver",
    version="0.0.1",
    url="https://github.com/whackashoe/mediaserver",
    license="LICENSE.txt",

    author="whackashoe",
    author_email="whackashoe@gmail.com",

    packages=["mediaserver"],
    include_package_data=True,
    description="Simple Media Server",
    long_description=open("README.txt").read(),

    install_requires=[
        "web.py",
    ],
)
