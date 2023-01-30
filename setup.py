from setuptools import setup, find_packages
from setuptools.extension import Extension
import numpy

setup(name="emo_utils",
    version='1.0.0',
    url="https://gitlab.au.dk/au616397/python_teaching_2023",
    description="Utils for EMO course at AU.",
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    packages=find_packages(),
    )
