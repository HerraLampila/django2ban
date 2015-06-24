from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django2ban',
    version='0.1',
    description='django2ban',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/HerraLampila/django2ban',

    author='Otto Lampila',
    author_email='otto.lampila@gmail.com',

    license='MIT',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: System :: Logging',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='django logging security',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['django'],
)
