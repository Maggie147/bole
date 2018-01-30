# -*- coding: utf-8 -*-
'''
bole login [requests.Session keep cookie]
update on 2018-01-25
@author: tx
'''
import os
import sys
import json
import requests
from requests import Session
from lxml import html
import time
import pprint
reload(sys)
sys.setdefaultencoding('utf8')


def write_date_2file(path, fname, data,):
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        with open(path+fname, "wb") as fp:
            fp.write(data)
    except Exception as e:
        print e
        return False
    return True


def is_login():
    url_login = '''http://www.jobbole.com/wp-admin/admin-ajax.php'''

    login_data = {
                'action': 'user_login',
                'user_login': 'helloworld_123',
                'user_pass': 'test123456'}

    headers_login = {
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'
            }

    login_session = requests.Session()

    # #get code_request
    # response = login_session.get(url_login, verify=False)
    # soup = BeautifulSoup(response.content, "html.parser")
    # captcha_id = soup.find('input',{'name':'captcha-id'})['value']

    # #get code
    # codeurl = "https://www.douban.com/misc/captcha?id=%s&size=s"%captcha_id
    # valcode = login_session.get(codeurl)
    # f = open('valcode.png', 'wb')
    # f.write(valcode.content)
    # f.close()

    # code = input('please input code:')
    # print "^^^"*10
    # print code
    # print captcha_id
    # login_data['captcha-id'] = str(captcha_id)
    # login_data['captcha-solution'] = code

    # response = login_session.post(url_login, data = login_data, headers = headers_login, verify=False)
    login_page = login_session.post(url_login, data = login_data, headers = headers_login)

    if login_page.status_code != 200:
        print "response status_code: ", login_page.status_code, type(login_page.status_code)
        return None

    try:
        login_result = json.loads(login_page.content)
        if login_result['jb_result'] != 0:
            print "login failed!!!"
            print login_result['jb_result'], type(login_result['jb_result'])
            return None
        else:
            print "login success"
            return login_session
    except Exception as e:
        print e
        return None

def get_request(is_session, url=None):
    print "get mew request"

    get_url = 'http://hao.jobbole.com/'
    response = is_session.get(get_url)
    ret = write_date_2file('./html/', 'hao.html', response.text)
    if ret:
        print "write html success"
    else:
        print "write html failed!!"

    tree = html.fromstring(response.text)

    if not tree.xpath('//div[@class="list-rs"]//h2/a[@href]/text()'):
        return None
    str1 = tree.xpath('//div[@class="list-rs"]//h2/a[@href]/text()')
    print str1

def main():
    my_session = is_login()

    if not my_session:
        print "no login session"
        return

    get_request(my_session)


if __name__ == "__main__":
    main()
