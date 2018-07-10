from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='salling-group-holidays',
    version='0.1',
    author='Kasper Laudrup',
    author_email='laudrup@stacktrace.dk',
    packages=[
        'salling_group_holidays',
    ],
    license='MIT',
    description='Unofficial library for the Salling Group holidays API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose'],
)
