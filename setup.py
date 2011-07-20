#!/usr/bin/env python

from distutils.core import setup

setup(name='riot',
      version='0.0.1',
      description='A reusable Django application of best-practices.',
      author='Riot Inc.',
      author_email='info@riot.io',
      url='https://github.com/heartherumble/django-riot',
      packages=['riot'],
      package_dir={'riot': 'riot'},
)