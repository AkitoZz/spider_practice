import requests
import re

#url = 'http://www.521609.com/daxuexiaohua/'

class spider(object):
    def getUrl(self,target_url,start_page,page_num):
        all_urls = []
        for i in range(start_page,page_num+1):
            new_urls = re.sub('/list_1_\d','/list_1_%d'%i,target_url,re.S)
            all_urls.append(new_urls)
        return all_urls

    def getLink(self,page_link):
        page_html = requests.get(page_link)
        all_pic_link = re.findall('<a target=\'_blank\' href="(.*?)">',page_html.text,re.S)
        return all_pic_link

    def getPic(self,page_url):
        pic_html = requests.get(page_url)
        all_pic_src = re.findall('<img alt=.*?src="(.*?)" /><br />',pic_html.text,re.S)
        return all_pic_src

    def saveFile(self,pic_src,num):
        pic = requests.get(pic_src)
        f = open('pic\\' + str(num) + '.jpg','wb')
        f.write(pic.content)
        f.close


if __name__ == '__main__':
    meizituSpider = spider()
    i = 1
    url = 'http://www.meizitu.com/a/list_1_1.html'
    all_link = meizituSpider.getUrl(url,7,89)
    for link in all_link:
        print('spidering:' + link)
        all_pic_link = meizituSpider.getLink(link)
        for pic_url in all_pic_link:
            print(pic_url)
            all_pic = meizituSpider.getPic(pic_url)
            for pic_src in all_pic:
                try:
                    meizituSpider.saveFile(pic_src,i)
                    print(i)
                    i += 1
                except:
                    pass   



#response = requests.get(url)
#html = response.text
