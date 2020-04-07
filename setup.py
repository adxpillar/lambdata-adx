# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="obatala", # the name that you will install via pip
    version="1.0",
    author="Olofin",
    author_email="olofin@adimula.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/adxpillar/lambdata-adx",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)