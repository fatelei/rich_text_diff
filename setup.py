# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='diff',
    version='0.0.1',
    author='liukai',
    author_email='liukai@zhihu.com',
    packages=['diff'],
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=[
        'lxml',
        'diff_match_patch',
        'bidict',
    ]
)
