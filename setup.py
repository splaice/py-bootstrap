from distutils.core import setup

setup(
    name='bootstrap',
    version='0.0.1',
    packages=['bootstrap',],
    license='GPLv2',
    long_description=open('README.txt').read(),
    test_suite = "bootstrap.test.test_all"
)
