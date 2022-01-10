# -*- coding: UTF-8 -*-

import os

import requests
from lxml import etree

from utils.email_util import send_email


def get_last():
    xpath = '/html/body/div[6]/div[1]/div[2]/div/span[1]'
    resp = requests.get('http://huwailx.360jlb.cn/m/event?id=384902')
    if resp.status_code != 200:
        return
    text = resp.text
    html = etree.HTML(text)
    last = html.xpath(xpath)[0].text
    file_path = '/tmp/qijian'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            pre = f.read()
            if pre != last:
                return last
            else:
                print('skip')
    else:
        with open(file_path, 'w') as f:
            f.write(last)


def main():
    last = get_last()
    if last:
        send_email("beer5214@126.com", "空位 {}".format(last), "qijian")


if __name__ == '__main__':
    main()
