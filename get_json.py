import requests
from lxml import etree
import os
import json
import re

def check_edition():
    url = "https://www.streetfighter.com/6/buckler/zh-hans/stats/usagerate_master"
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'Connection' : 'close'
    }
    response = requests.get(url=url, headers= headers, timeout=10)
    text = response.text
    tree = etree.HTML(text)
    ele = tree.xpath('/html/body/div[1]/div/article[2]/aside[1]/div/section/select/option')
    date = [i.text.replace(".", "") for i in ele]
    return date

def get_json_by_web(edition):
    url = "https://www.streetfighter.com/6/buckler/api/zh-hans/stats/usagerate_master/" + edition
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'Connection' : 'close'
    }
    response = requests.get(url, headers=headers , timeout=10)
    data = response.json()
    return data

def check_json_file(edition):
    path = os.path.abspath(__file__)
    pattern = r'.*(?=\\[^\\]+$)'
    path_dir = re.search(pattern, path).group()
    path_json = path_dir + '\\\\json\\\\' + 'usagerate_master' + '_' + edition + '.json'
    if os.path.exists(path_json):
        with open(path_json, 'r', encoding='utf-8') as j:
            data = json.load(j)
        return data
    else:
        data = get_json_by_web(edition)
        with open(path_json, 'w', encoding='utf-8') as j:
            json.dump(data, j, ensure_ascii=False)
        return data
    
def main():
    date = check_edition()
    url_usagerate_master = 'https://www.streetfighter.com/6/buckler/api/zh-hans/stats/usagerate_master/'
    url_usagerate_all = 'https://www.streetfighter.com/6/buckler/api/zh-hans/stats/usagerate/'
    