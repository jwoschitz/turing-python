# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='turing',
    version='0.0.1',
    description='Universal turing machine implemented in Python',
    long_description=readme,
    author='Janosch Woschitz',
    author_email='janosch.woschitz@gmail.com',
    url='https://github.com/jwoschitz/turing-python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
