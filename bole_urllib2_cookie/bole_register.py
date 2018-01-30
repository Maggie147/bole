#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'bole_register_2.7'
__author__ = 'xxxx'
__mtime__ = '2017-01-20'

"""

import urllib
import urllib2

import cookielib


def main():

	LOGIN_URL = 'http://www.jobbole.com/wp-admin/admin-ajax.php'
	get_url = 'http://www.jobbole.com/'  # 利用cookie请求访问另一个网址

	values = {'action': 'user_login', 'user_login': 'helloworld_123', 'user_pass': 'green931205'}
	postdata = urllib.urlencode(values).encode()
	user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'
	headers = {'User-Agent': user_agent}

	cookie_filename = './bole_cookie/cookie_bole.txt'
	cookie_bole = cookielib.MozillaCookieJar(cookie_filename)
	handler = urllib2.HTTPCookieProcessor(cookie_bole)
	opener = urllib2.build_opener(handler)

	request = urllib2.Request(LOGIN_URL, postdata, headers)

	try:

	    response = opener.open(request)

	    page = response.read().decode()

	    # print page

	except urllib.error.URLError as e:

	    print e.code, ':', e.reason


	cookie_bole.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中


	for item in cookie_bole:

	    print 'Name = ', item.name
	    print 'Value = ', item.value


	get_request = urllib2.Request(get_url, headers=headers)
	get_response = opener.open(get_request)
	print get_response.read()


if __name__ == "__main__":

    main()