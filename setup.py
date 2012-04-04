from setuptools import setup, find_packages

setup(name = 'django_addexampledata',
      description = 'Provides addexampledata.',
      version = '1.0',
      url = 'http://espenak.net',
      author = 'Espen Angell Kristiansen',
      packages=find_packages(exclude=['ez_setup']),
      install_requires = ['setuptools', 'Django']
)
