import codecs
import os
from setuptools import setup, find_packages

# these things are needed for the README.md show on pypi (if you dont need delete it)
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# you need to change all these
VERSION = '1.0.0'
DESCRIPTION = 'lightspeed is a shortcut based tool for windows '
LONG_DESCRIPTION = 'lightspeed is a `hotkey launcher` written in python'

setup(
    name="lightspeed",
    version=VERSION,
    author="clever chen",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'lightspeed','windows','quick','shortcut','hotkey','folder','open','explorer'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        "console_scripts": ["lsp=lightspeed.commandline:main"]
    }
)
