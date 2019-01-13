import platform
from setuptools import setup, find_packages

from binding_version import binding_version

long_description = open('README.rst').read()

setup(
    name='h3',
    version=binding_version,
    description=
    'Python bindings for H3, a hierarchical hexagonal geospatial indexing system developed by Uber Technologies',
    long_description=long_description,
    author='Uber Technologies',
    author_email='Niel Hu <hu.niel92@gmail.com>',
    url='https://github.com/uber/h3-py.git',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[],
    package_data={
        'h-py':
        ['out/*.dylib' if platform.system() == 'Darwin' else 'out/*.so.*']
    },
    license='Apache License 2.0',
)
