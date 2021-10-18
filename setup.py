import re
import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent

NAME = "my_package"

try:
    long_description = (here / "README.md").read_text("utf-8")
except FileNotFoundError:
    long_description = ''

txt = (here / NAME / "__init__.py").read_text("utf-8")
try:
    version = re.findall(r'^__version__ = "([^"]+)"\r?$', txt, re.MULTILINE)[0]
except IndexError:
    raise RuntimeError("Version not set.")

classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
]

setup(
    name=NAME,
    version=str(version),
    description="A cool module",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sengolda',
    python_requires=">=3.6",
    packages=[NAME],
    include_package_data=True,
    license='MIT',
    classifiers=classifiers
)
