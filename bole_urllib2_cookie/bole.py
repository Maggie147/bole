#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'bole_2.7'
__author__ = 'xxxx'
__mtime__ = '2017-01-20'

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

import urllib2
import cookielib


def main():
	cookie_filename = './bole_cookie/cookie_bole.txt'
	cookie = cookielib.MozillaCookieJar(cookie_filename)
	cookie.load(cookie_filename, ignore_discard=True, ignore_expires=True)
	# print cookie

	handler = urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(handler)

	get_url = 'http://www.jobbole.com/'  # 利用cookie请求访问另一个网址

	get_request = urllib2.Request(get_url)
	get_response = opener.open(get_request)

	print get_response.read()


if __name__ == "__main__":

    main()