import os
import re
import time
import datetime
import requests
import urllib.request as url
from dateutil.parser import parse
from bs4 import BeautifulSoup as bs

######################################################
import input_warframe
######################################################

def image_crawling(item, path, path_0, etc):

    get_item = item.replace('_Prime', '')
    get_path = path
    get_path_0 = path_0
    
    if(etc == 'mod'):
        site = 'https://warframe.fandom.com/wiki/{get_item}'.format(get_item = get_item)
        res = requests.get(site)
    else:
        return

    html = res.text
    soup = bs(html, 'html.parser')
    soup = soup.find('img', class_= 'pi-image-thumbnail')
    soup_url = soup['src']
    
    def make_file(soup_url, path):
        get_path = path
        if os.path.isfile(get_path):
            print('현제 파일이 있습니다.')
        else:
            url.urlretrieve(soup_url, get_path)
            print('새로운 데이터를 저장했습니다.') 
    
    if os.path.isdir(get_path_0):
        make_file(soup_url, get_path)
    else:
        #print('폴더가 없음으로 새로 만들었습니다.')
        os.makedirs(get_path_0)
        make_file(soup_url, get_path)
    
    print(str(get_item) + ' 업데이트를 하였습니다.')
######################################################

startTime = time.time()

input_items = input_warframe.input_item('aura_mods')

for i, v in enumerate(input_items):
    item = v.replace('_prime', '/')
    item = item.title()
    item = item.replace('/', '_Prime')
    
    path = '/workspace/crawling/html/static/image/item_image/mod/' + item + '/' + item + '.png'
    path_0 = '/workspace/crawling/html/static/image/item_image/mod/' + item
    
    save_data = image_crawling(item, path, path_0, 'mod')
    endTime = time.time() - startTime
    print(str(round(i / len(input_items) * 100)) + "% 완료했습니다. 시간: " + str(round(endTime)) + "초")

input_items = input_warframe.input_item('warframe_mods')

for i, v in enumerate(input_items):
    item = v.replace('_prime', '/')
    item = item.title()
    item = item.replace('/', '_Prime')
    
    path = '/workspace/crawling/html/static/image/item_image/mod/' + item + '/' + item + '.png'
    path_0 = '/workspace/crawling/html/static/image/item_image/mod/' + item
    
    save_data = image_crawling(item, path, path_0, 'mod')
    endTime = time.time() - startTime
    print(str(round(i / len(input_items) * 100)) + "% 완료했습니다. 시간: " + str(round(endTime)) + "초")

input_items = input_warframe.input_item('weapon_mods')

for i, v in enumerate(input_items):
    item = v.replace('_prime', '/')
    item = item.title()
    item = item.replace('/', '_Prime')
    
    path = '/workspace/crawling/html/static/image/item_image/mod/' + item + '/' + item + '.png'
    path_0 = '/workspace/crawling/html/static/image/item_image/mod/' + item
    
    save_data = image_crawling(item, path, path_0, 'mod')
    endTime = time.time() - startTime
    print(str(round(i / len(input_items) * 100)) + "% 완료했습니다. 시간: " + str(round(endTime)) + "초")

print("업데이트가 모두 완료했습니다.")

######################################################