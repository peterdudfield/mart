""" Usual setup file for package """
from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
install_requires = (this_directory / "requirements.txt").read_text().splitlines()

setup(
    name="mart",
    version="0.0.1",
    license="MIT",
    description="Mart",
    author="Peter Dudfield",
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
)
