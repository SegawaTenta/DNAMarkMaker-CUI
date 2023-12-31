#!/usr/bin/env python3




from setuptools import setup, find_packages
from dnamarkmaker.__init__ import __version__

setup(
    name="DNAMarkMaker",
    version='{}'.format(__version__),
    description='DNAMarkMaker: pipline to develop ARMS and CAPS marker',
    url='https://github.com/SegawaTenta/DNAMarkMaker-CUI',
    author='Tenta Segawa',
    packages=['dnamarkmaker'],
    install_requires=[
        "primer3-py"
    ],
    entry_points={
        'console_scripts': [
            'DNAMarkMaker=dnamarkmaker.DNAMarkMaker:main'
        ]
    }
)
