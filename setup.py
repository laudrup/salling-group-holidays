from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='salling-group-holidays',
    version='0.2',
    author='Kasper Laudrup',
    author_email='laudrup@stacktrace.dk',
    url='https://github.com/laudrup/salling-group-holidays',
    packages=[
        'salling_group_holidays',
    ],
    license='MIT',
    description='Unofficial library for the Salling Group holidays API',
    long_description=readme(),
    long_description_content_type='text/x-rst',
    install_requires=[
        'requests',
        'wheel',
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose'],
)
