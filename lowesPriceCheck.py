#!/usr/bin/env python3

from lxml import html
import requests
import os

print("Enter store number: ")
storeNum = input()


if storeNum.isdecimal():
    shoppingListFile = open('list.txt')
    shoppingListList = shoppingListFile.read().split(',')
    cookies = dict(sn=storeNum)

    for x in shoppingListList:
        page = requests.get(r'https://www.lowes.com/search?searchTerm={}'.format(x), cookies=cookies)
        tree = html.fromstring(page.content)

        price = tree.xpath('//span[@class="primary-font jumbo strong"]/text()')
        print('SKU: %s' % x, '\tPrice: %s' % price)

else:
    print("Please enter a valid store number. ie- ####")
