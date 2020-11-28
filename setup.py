from setuptools import setup, find_packages

setup (
    author='geremachek',
    author_email='gmk@airmail.cc',
    name='rho',
    long_description='Add some zen to your terminal',
    packages=find_packages(),
    entry_points={'console_scripts': ['rho = rho.__main__:main']},
    package_dir={'rho': 'rho'},
)
