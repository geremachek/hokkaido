from setuptools import setup, find_packages

setup (
    author='geremachek',
    author_email='joth@tuta.io',
    name='hokkaido',
    long_description='Add some zen to your terminal',
    packages=find_packages(),
    entry_points={'console_scripts': ['hokkaido = hokkaido.__main__:main']},
    package_dir={'hokkaido': 'hokkaido'},
    version="2.0.0"
)
