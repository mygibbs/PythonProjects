try:
    from setuptools import setup
except ImportError:
    from distuils.core import setup

config = {
    'description': 'My Project',
    'author': 'Matthew Gibbs',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'mygibbs@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)