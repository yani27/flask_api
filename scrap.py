
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

result_list = []
result_dict = {}

req2 = requests.get(url)
soup2 = BeautifulSoup(req2.text, 'html.parser')

container = soup2.findAll("div", {"class": "qa-match-block"})


for item in range(len(container)):
    print('--| item : {} |--'.format(item))

    league_title = container[item].find(
        "h3", {"class": "gel-minion sp-c-match-list-heading"})

    print("leaque {} : {}".format(item, league_title.text))

    adv = container[item].findAll("span", {
        "class": "gs-u-display-none gs-u-display-block@m qa-full-team-name sp-c-fixture__team-name-trunc"})

    time = container[item].find(
        "span", {"class": "sp-c-fixture__number sp-c-fixture__number--time"})

    k = 0
    for i in range(len(adv)):
        print("adv {} : {}".format(i, adv[i].text.encode('utf-8')))
        result_dict['adv{}'.format(i)] = adv[i].text.encode('utf-8')
        k += 1

        if k == 2:
            try:
                print("in time = {}".format(time.text.encode('utf-8')))
                result_dict['time'] = time.text.encode('utf-8')
            except:
                pass
            finally:
                k = 0

    result_list.append(result_dict)
    break
print("result_list : ", result_list)
print('result dict ', result_dict)
