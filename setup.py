# coding: utf-8

"""
    tpu-api

    The API for the TPU project.
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "tensor-processor"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["requests"]

setup(
    name=NAME,
    version=VERSION,
    description="TPU SDK",
    author_email="",
    url="",
    keywords=["tensor", "processor", "tpu-api"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The API for the TPU project.
    """
)
