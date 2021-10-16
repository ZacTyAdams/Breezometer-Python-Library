from setuptools import find_packages, setup

setup(
    name='breezometerlib',
    packages=find_packages(include=['breezometerlib']),
    version='0.2.1',
    description='Library for the Breezometer service',
    author='https://github.com/ZacTyAdams',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)