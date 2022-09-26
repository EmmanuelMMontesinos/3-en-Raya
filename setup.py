from distutils.core import setup
import zipfile
import py2exe
import PySimpleGUI as pysg
from time import sleep
import random


setup(zipfile=None,
      options={"py2exe" : {"bundle_files" : 1}},
      console={"tres_r.py"})