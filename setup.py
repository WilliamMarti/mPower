#!/usr/bin/env python

from setuptools import setup

setup(
      name='mpower',
      description='Scripted control of mPower Pro ports',
      url='https://github.com/WilliamMarti/mPower',
      
      #Author Info
      author='William Marti',
      author_email='William.b.marti@gmail.com',
      
      license='GNU',
      
      version='1.0',
      
      install_requires = ['paramiko'], 

      py_modules=['mpower'],
)

