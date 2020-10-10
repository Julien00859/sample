from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

version = (here / 'VERSION').read_text().strip()
long_description = (here / 'README.md').read_text(encoding='utf-8')

NAME = ...
DESC = ...

setup(
    name=NAME,
    version=version,
    description=DESC,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/julien00859/{NAME}',
    author='Julien Castiaux',
    author_email='julien.castiaux@gmail.com',
    packages=find_packages(where=NAME),

    # https://pypi.org/classifiers/
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],

    python_requires='>=3.5, <4',

    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],
    extras_require={},
)
