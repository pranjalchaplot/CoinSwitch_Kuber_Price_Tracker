from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import time

csk = requests.get('https://coinswitch.co/')
soup = BeautifulSoup(csk.content, 'html.parser')
