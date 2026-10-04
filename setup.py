from setuptools import setup

from mypyc.build import mypycify


setup(
    name= "gameboy",
    packages= ["gameboy"],
    ext_modules= mypycify(["C:\\Users\\oloke\\Downloads\\New folder (3) - Copy\\CPU.py"])
)