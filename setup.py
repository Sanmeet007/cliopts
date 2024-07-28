from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "readme.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "1.1.3"
DESCRIPTION = "The cliopts package is a Python library for parsing command line arguments. It provides a simpler and more intuitive API with less code and easy cli argument parsing."

# Setting up
setup(
    name="cliopts",
    version=VERSION,
    license="GPL-3.0 license",
    url="https://github.com/Sanmeet007/cliopts.git",
    author="Sanmeet Singh",
    author_email="ssanmeet123@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=[
        "python",
        "command line",
        "command line arguments",
        "cli",
        "cli args",
        "cli opts",
        "command line options",
        "cliargs",
        "argparser",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.12",
        "Operating System :: POSIX :: Linux",
    ],
)
