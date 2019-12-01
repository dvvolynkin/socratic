#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Socratic - very simple question-answer dialogue system based on python generators.
#
# Daniil Volynkin
# foxezzz@gmail.com
#
# License: MIT
#

import os
import sys
from os.path import join as pjoin
from setuptools import setup, find_packages, Command

meta = {}
with open(pjoin('socratic', '__version__.py')) as f:
    exec(f.read(), meta)

with open('README.md') as readme_file:
    readme = readme_file.read()


class Publish(Command):
    """Publish to PyPI with twine."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('python setup.py sdist bdist_wheel')

        sdist = 'dist/socratic-%s.tar.gz' % meta['__version__']
        wheel = 'dist/socratic-%s-py3-none-any.whl' % meta['__version__']
        rc = os.system(
            'twine upload --verbose --repository-url=https://upload.pypi.org/legacy/ "%s" "%s"' % (sdist, wheel)
        )

        sys.exit(rc)


setup(
    name=meta['__title__'],
    license=meta['__license__'],
    version=meta['__version__'],
    author=meta['__author__'],
    author_email=meta['__contact__'],
    url=meta['__url__'],
    description=meta['__description__'],
    long_description_content_type='text/markdown',
    long_description=readme,
    platforms=['any'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[],
    python_requires='>=3.7',
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    cmdclass={
        'publish': Publish,
    },
)
