from datetime import datetime
import requests,json

from requests import cookies
def login(username,password):
    link = 'https://www.instagram.com/accounts/login/'
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    time = int(datetime.now().timestamp())
    response = requests.get(link,headers = {'User-agent': 'I serve the JADE EMPERROR'})
    csrf = response.cookies['csrftoken']
    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }
    login_response = requests.post(login_url, data=payload, headers=login_header)
    json_data = json.loads(login_response.text)
    if json_data["authenticated"]:
        print("login successful")
        cookie_jar = cookies.get_dict()
        return {'cookies':cookies,'coolie_jar':cookie_jar,'csrf_token':cookie_jar['csrftoken'],'session_id':cookie_jar['sessionid']}
    else:
        print("login failed ", login_response.text)