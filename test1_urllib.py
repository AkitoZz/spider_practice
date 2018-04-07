import requests
import re
import urllib.request

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


    def saveFile(self,pic_src,number):
        #pic = requests.get(pic_src)
        webheader = {
        'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Host':'i.meizitu.net',
        'Referer':'http://www.mzitu.com/127621',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
        req = urllib.request.Request(url=pic_src,headers=webheader)
        webpage = urllib.request.urlopen(req)
        f = open('pic1\\'+str(number)+'.jpg','wb')
        f.write(webpage.read())
        f.close()


#    def saveFile(self,pic_src,number):        #遇到反爬虫了
#        request.urlretrieve(pic_src,'pic1\\'+str(number)+'.jpg')
        

if __name__ == '__main__':
    '''
    m = 1
    meizi = spider()
    urls = meizi.geturl(url,1,1)
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
                    print('spidering: ',img)
                    meizi.saveFile(img,m)
                    m += 1
'''
  

    
    
    
    meizi = spider()
    weburl = 'http://i.meizitu.net/thumbs/2013/08/9551_img1_src_6943668_158.jpg'
    meizi.saveFile(weburl,1)


#    meizi = spider()
#    meizi.saveFile('http://i.meizitu.net/2018/03/30b01.jpg',1)

#print(urls)
#for i in urls:
#    links = meizi.getlink(i)
#    print(links)


#num = meizi.get_pic_num('http://www.mzitu.com/127368')
#print(num)


