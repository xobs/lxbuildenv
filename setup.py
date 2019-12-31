#!/usr/bin/env python3

import sys
from setuptools import setup
from setuptools import find_packages


if sys.version_info[:3] < (3, 5):
    raise SystemExit("You need Python 3.5+")

print()

setup(
    name="lxbuildenv",
    description="Simplified build environment for LiteX",
    long_description=open("README.asciidoc").read(),
    author="Sean Cross",
    author_email="sean@xobs.io",
    url="http://xobs.io",
    download_url="https://github.com/xobs/lxbuildenv",
    license="BSD",
    platforms=["Any"],
    keywords="HDL ASIC FPGA hardware design",
    classifiers=[
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "Environment :: Console",
        "Development Status :: Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    py_modules=["lxbuildenv"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "lxbuildenv=lxbuildenv:main",
        ],
    },
)
