
#!/usr/bin/python
# -*- coding: latin-1 -*-
import requests
import json
import os
from bs4 import BeautifulSoup

# pip install virtualenv
# source venv/bin/activate
# pip3 install -r requirements.txt

url = 'https://www.bbc.com/sport/football/scores-fixtures'


BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
JSON_FILE = os.path.join(BASE_DIRECTORY, 'data_json.json')

req2 = requests.get(url)
soup2 = BeautifulSoup(req2.text, 'html.parser')

container = soup2.findAll("div", {"class": "qa-match-block"})

print(len(container))

for item in range(len(container)):
    print('--| item : {} |--'.format(item))

    league_title = container[item].find(
        "h3", {"class": "gel-minion sp-c-match-list-heading"})

    adv1 = container[item].findAll("span", {
        "class": "gs-u-display-none gs-u-display-block@m qa-full-team-name sp-c-fixture__team-name-trunc"})

    print("leaque {} : {}".format(item, league_title.text))
    # print("adverss : ", adv1.text.encode('utf-8'))

    # for i in range(len(adv1)):
    #     print("adv {} : {}".format(i, adv1.text.encode('utf-8')))
