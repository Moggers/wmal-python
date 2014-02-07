#!/usr/bin/env python

from distutils.core import setup

setup(name='wMAL',
      version='0.3',
      description='Open multi-site list manager',
      author='z411/moggers',
      url='https://github.com/Moggers/wmal-python',
      packages=['wmal', 'wmal.lib', 'wmal.ui'],
      package_data={'wmal': ['data/*']},
      scripts=['bin/wmal', 'bin/wmal-curses', 'bin/wmal-gtk'],
      requires=[]
      )
