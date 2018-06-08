# SPDX-License-Identifier: GPL-2.0+
from setuptools import setup, find_packages

setup(
    name='blogify',
    version='0.1',
    description='Blogify is a web app to view and post blogs',
    author='Yashvardhan Nanavati',
    author_email='yashn@bu.edu',
    license='GPLv3+',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
)