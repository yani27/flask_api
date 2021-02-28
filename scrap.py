
#!/usr/bin/python
# -*- coding: latin-1 -*-
import requests
import json
import os
from bs4 import BeautifulSoup

# pip install virtualenv
# source venv/bin/activate
# pip3 install -r requirements.txt

url = 'https://www.kooora.com/'


# BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
# CSV_FILE = os.path.join(BASE_DIRECTORY, 'data_csv.csv')
# JSON_FILE = os.path.join(BASE_DIRECTORY, 'data_json.json')
# STORE_URLS = os.path.join(BASE_DIRECTORY, 'store_urls.json')

req2 = requests.get(url)
soup2 = BeautifulSoup(req2.text, 'html.parser')

print(soup2)
