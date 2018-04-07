import requests
import re
from urllib import request
from threading import *


url = 'http://www.mzitu.com/page/1'

class spider(object):
    def geturl(self,target_url,start_page,page_num):
        all_urls = []
        for i in range(start_page,page_num+1):
            new_url = re.sub('/page/\d','/page/%d'%i,target_url,re.S)
            all_urls.append(new_url)
        return all_urls

    def getlink(self,page_link):
        page_html = requests.get(page_link)
        #all_pic_link = re.findall('<a target=\"_blank\" href="(.*?)">',page_html.text,re.S)
        #all_pic_link = re.findall('<a href="(.*?)" target=\"_blank\">',page_html.text,re.S)
        all_pic_link = re.findall('<a href=\"(http://www.mzitu.com/[\d]+)\" target=\"_blank\">',page_html.text,re.S)
        return all_pic_link

    def get_pic_num(self,page_url):
        pic_url = requests.get(page_url)
        pic_num = int(re.findall('%s/[\d]+'%page_url,pic_url.text,re.S)[-2].split('/')[-1])
        return pic_num

    def get_pic(self,pic_url,num):
        pic_urls = []
        for i in range(1,num):
            pic_urls.append(pic_url+'/%s'%str(i))
        return pic_urls    







  #  def saveFile(self,pic_src,number):        #遇到反爬虫了
 #       webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'} 
#        request.urlretrieve(pic_src,'pic1\\'+str(number)+'.jpg')
        

    def saveFile(self,pic_src,number):
        h = {
            'Host': 'i.meizitu.net',
            'Pragma': 'no-cache',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Referer': '{}'.format(pic_src),
        }
        
        pic = requests.get(pic_src,headers=h)
        f = open('pic\\'+str(number)+'.jpg','wb')
        f.write(pic.content)
        f.close()    

if __name__ == '__main__':
    
    m = 1
    meizi = spider()
    urls = meizi.geturl(url,1,2)
    print('urls: ',urls)
    for i in urls:
        links = meizi.getlink(i)
        for each_page in links:
            print('spidering: ',each_page)
            num = meizi.get_pic_num(each_page)
            each_page_url = meizi.get_pic(each_page,num)
            for i in each_page_url:
                each_page_src = requests.get(i)
                each_page_img = re.findall('<img src=\"(.*)\" alt=.*>',each_page_src.text,re.S)
                for img in each_page_img:
                    print('spidering(%d): ' %m,img)
                    try:
                        t = Thread(target = meizi.saveFile,args=(img,m))
                        t.start()
                        m += 1
                    except:
                        print('Error:',img,m)    

#    meizi = spider()
#    meizi.saveFile('http://i.meizitu.net/2018/03/30b01.jpg',1)

#print(urls)
#for i in urls:
#    links = meizi.getlink(i)
#    print(links)


#num = meizi.get_pic_num('http://www.mzitu.com/127368')
#print(num)


