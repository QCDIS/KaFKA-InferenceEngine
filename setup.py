#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = [
    'pytest',
    'numpy',
    'scipy',
    'gdal',
    'BRDF_descriptors @ https://github.com/QCDIS/BRDF_descriptors.git',
    'matplotlib'
]

setup(name='KaFKA',
      description='MULTIPLY KaFKA inference engine',
      author='MULTIPLY Team',
      packages=find_packages(),
      install_requires=requirements
)
