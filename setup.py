import os

os.environ['DJANGO_SETTINGS_MODULE'] = \
    'tests.settings'

from setuptools import setup

setup(
    name='wossname',
    version='0.140804',
    author='http://www.aptivate.org/',
    author_email='support+wossname@aptivate.org',
    packages=['wossname'],
    include_package_data=True,
    url='https://github.com/aptivate/wossname',
    license='LICENSE',
    description='Anything with a name',
    #long_description=open('README.md').read(),
    setup_requires = [ "setuptools_git >= 0.3", ],
    install_requires=[
        "Django", # 1.5 or 1.6
        "south >= 0.8.4",
    ],
    tests_require=[
    ],
    test_suite = "tests",
)
