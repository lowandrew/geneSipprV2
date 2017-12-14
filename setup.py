#!/usr/bin/env python
from setuptools import setup, find_packages
__author__ = 'adamkoziol'

setup(
    name="sipprverse",
    version="0.0.28",
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    author='Adam Koziol',
    author_email='adam.koziol@inspection.gc.ca',
    description='Object oriented raw read typing software',
    url='https://github.com/OLC-Bioinformatics/geneSipprV2/sipprverse',
    long_description=open('README.md').read(),
    install_requires=['OLCTools==0.3.19',
                      'sipprverse==0.0.24',
                      'biopython==1.70',
                      'pysam==0.13'
                      ]
)
