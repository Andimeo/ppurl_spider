'''
Created on Jun 19, 2015

@author: andimeo
'''

from scrapy import Spider, Request
from ppurl.items import PpurlItem

class PPUrlSpider(Spider):
    name = 'ppurl'
    allowed_domains = ['bt8.nl']
    start_urls = ['http://bt8.nl/ebook.php?page=1']
    
    def parse(self, response):
        books = response.xpath('/html/body/div[3]/table/tr')
        for book in books:
            l = book.xpath('td[7]/a/@href').extract()
            link_url = 'http://bt8.nl/' + ('' if len(l) == 0 else l[0])
            yield(Request(url=link_url, callback=self.store))
        pageNO = int(response.url.split('?')[1].split('=')[1])
        if pageNO < 162:
            pageNO += 1
            next_page_url = response.url.split('?')[0] + '?page=' + str(pageNO)
            yield(Request(url=next_page_url, callback=self.parse))
                  
    def store(self, response):
        item = PpurlItem()
        l = response.xpath('/html/body/table/tr[1]/td[2]/font/text()').extract()
        item['title'] = '' if len(l) == 0 else l[0]
        l = response.xpath('/html/body/table/tr[2]/td[2]/font/text()').extract()
        item['author'] = '' if len(l) == 0 else l[0]
        l = response.xpath('/html/body/table/tr[3]/td[2]/font/text()').extract()
        item['ISBN'] = '' if len(l) == 0 else l[0]
        l = response.xpath('/html/body/table/tr[4]/td[2]/font/text()').extract()
        item['publish_date'] = '' if len(l) == 0 else l[0]
        l = response.xpath('/html/body/table/tr[5]/td[2]/font/text()').extract()
        item['pages'] = '' if len(l) == 0 else l[0]
        l = response.xpath('/html/body/table/tr[6]/td[2]/font/text()').extract()
        item['format'] = '' if len(l) == 0 else l[0]
        l = response.xpath('/html/body/table/tr[7]/td[2]/font/text()').extract()
        item['size'] = '' if len(l) == 0 else l[0]
        item['link'] = 'http://' + response.xpath('/html/body/table/tr[8]/td[2]/a/@href').extract()[0]
        return item
        