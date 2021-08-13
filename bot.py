from jade import profile
import requests
from datetime import datetime
import botactions as actions
import json

if __name__ == '__main__':
    jade=profile()
    jade_res = actions.login(jade.uid,jade.pwd)
    #page=requests.get('https://www.instagram.com/jade_emperror/',cookies=jade_res['cookie_jar'])
    headers={
        'authority':'www.instagram.com',
        'method':'POST',
        'path':'/fxcal/ig_sso_users/',
        'scheme':'https',
        'accept':'*/*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'en-US,en;q=0.9',
        'content-length':'0',
        'content-type':'application/x-www-form-urlencoded',
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com',
        'sec-ch-ua':'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile':'?0',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "x-csrftoken":jade_res['cookie_jar']['csrftoken']





    }
    res=requests.post('https://www.instagram.com/fxcal/ig_sso_users/',cookies=jade_res['cookie_jar'],headers=headers)
    page=requests.get('https://www.instagram.com/jade_emperror/',cookies=jade_res['cookie_jar'])
    with open('index.html','a') as f:
        f.write(page.text)