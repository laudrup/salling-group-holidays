from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='salling-group-holidays',
    version='0.3',
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
        'nose'
    ],
    keywords='holidays, calendar, salling, denmark, danish',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
    ],
)
