from setuptools import setup, find_packages

setup(name = 'django_addexampledata',
      description = 'Easily bundle example data with your django apps.',
      version = '1.0',
      url = 'https://github.com/espenak/django_addexampledata',
      author = 'Espen Angell Kristiansen',
      packages=find_packages(exclude=['ez_setup']),
      install_requires = ['setuptools', 'Django'],
      license = 'BSD',
      zip_safe = False,
      include_package_data=True,
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                  ]
)
