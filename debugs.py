import re
import requests
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
        }
def get_web_site_url():
    web_site_url = []
    wei_site_url = 'http://www.caoliu2068.com/thread0806.php?fid=16&search=&page='
    for i in range(1,167):
        web_site_url.append(wei_site_url+str(i))
    return web_site_url
def get_page_list(wei_site_url):
    data = requests.get(wei_site_url,headers=headers,timeout=30).content.decode('gbk')
    name_and_url = re.findall('<a.*html[ a-z_="><]*[\u4E00-\u9FA5]+',data)
    res = []
    for i in name_and_url:
        res.append([re.findall('[a-z0-9/.]+html',i)[0],re.findall('[\u4E00-\u9FA5]+',i)[0]])
    for i,v in enumerate(res):
        res[i][0] = 'http://www.caoliu2068.com/'+res[i][0]
    return res
def all_page_list():
    web_site_url = get_web_site_url()
    page_list = []
    for i in web_site_url:
        page_list.extend(get_page_list(i))
    return page_list