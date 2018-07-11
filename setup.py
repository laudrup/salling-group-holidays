from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


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
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
        'wheel',
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose'],
)
