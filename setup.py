# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='liver-visualization',
    version='0.0.1',
    description='Automatic segmentation and visualization of liver and it\'s vessels from CT images',
    long_description=readme,
    author='Wang Chi',
    author_email='wanchi1995@gmail.com',
    url='https://github.com/moonfoam/liver-visualization',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

