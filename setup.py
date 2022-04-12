# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['juan']
install_requires = \
['appdirs>=1.4.4,<2.0.0']

entry_points = \
{'console_scripts': ['juan = juan:main']}

setup_kwargs = {
    'name': 'juan',
    'version': '0.1.0',
    'description': 'Generate .gitignore files from the command line',
    'long_description': '# Juan\n\nJuan generates .gitignore files from the command line\n\nIt supports Python 3.9+.',
    'author': 'Juan Olvera',
    'author_email': 'juan@jolvera.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)

