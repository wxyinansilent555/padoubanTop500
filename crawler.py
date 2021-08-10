import requests
from lxml import etree
import csv
import codecs
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")
#创建csv文件，并写入表头信息
fp = codecs.open('C:\\Users\\此间兮若流年\\Desktop\\py\\paqudoubanTop500\\h.csv',"w+","utf-8-sig")
writer = csv.writer(fp)
writer.writerow(('书名','地址','作者','出版社','出版日期','价格','评分','评价'))
#构建所有url连接
urls = ['https://book.douban.com/top250?start={}'.format(str(i))for i in range(0,25)]
#添加请求头
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
#循环url
for url in urls:
    html = requests.get(url,headers= headers)
    selector = etree.HTML(html.text)
    #取大标签，以此循环
    infos = selector.xpath('//tr[@class = "item"]')
    #循环获取信息
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        book_infos = info.xpath('td/p/text()')[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('td/div/span[2]/text()')[0]
        comments = info.xpath('td/p/span/text()')
        comment = comments[0] if len (comments) != 0 else "空"
        #写入数据
        writer.writerow((name,url,author,publisher,date,price,rate,comment))
fp.close()
