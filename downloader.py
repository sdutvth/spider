import requests
import os
import time
from debugs import *
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
        }
'''
获取链接中图片的URL
'''
def get_pic_url(url):
    try:
        res = requests.get(url, headers=headers,timeout=20)
    except Exception as e:
        return False
    ori_str = res.content.decode('gbk')
    src_list = []
    current_str = ''
    flag = True
    for i in ori_str: # 把所有标签读入src_list
        if flag and i == '<':
            current_str += i
            flag = False
        elif flag:
            continue
        elif i != '>':
            current_str += i
        else:
            current_str += i
            src_list.append(current_str)
            current_str = ''
            flag = True
    url_list = []
    for i in src_list:
        if '<input src=' in i:
            url_list.append(i.split('"')[1])
    return url_list
'''
下载图片至本地
'''
def download_pic(url_list,folder):
    if url_list == False:
        return
    new_dir = 'D:/setu/' + folder
    i = 0
    while os.path.exists(new_dir):
        new_dir += str(i)
    os.mkdir(new_dir)
    for i in url_list[:]:
        try:
            res = requests.get(i, headers=headers,timeout=30)
        except Exception as e:
            pass
        else:
            f = open('D:/setu/'+folder+'/'+i.split('/')[-1],'wb')
            f.write(res.content)
            f.close()
page_list = all_page_list()
for i in page_list:
    download_pic(get_pic_url(i[0]),i[1])