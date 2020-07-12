from setuptools import setup, find_packages

setup (
    author='geremachek',
    author_email='gmk@airmail.cc',
    name='kokyu',
    long_description='Add some zen to your terminal',
    packages=find_packages(),
    entry_points={'console_scripts': ['kokyu = kokyu.__main__:main']},
    package_dir={'kokyu': 'kokyu'},
)
