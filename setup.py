# !/usr/bin/env python3
from sys import exit

try:
  from flask import Flask
except ImportError as e:
  print(e)
  print("Could not import Flask:")
  print("Run '$ pip3 install flask' to install Flask framework")
  exit(1)

try:
  from bs4 import BeautifulSoup
except ImportError as e:
  print(e)
  print("Could not import BeautifulSoup:")
  print("Run '$ pip3 install beatuifulsoup4' to install BeatifulSoup4 library")
  exit(1)


import os
from persistence import setup

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
SCRAPER_PATH = os.path.join(DIRECTORY, 'scraper.py')

setup()
exec(open(SCRAPER_PATH).read())