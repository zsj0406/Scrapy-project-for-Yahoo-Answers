import scrapy
from yahoo.items import YahooItem
from scrapy.http import Request
from scrapy.http import Request,FormRequest
import time
from bs4 import BeautifulSoup
import lxml.html
import json

class yahooSpider(scrapy.Spider):
    name = "yahoo_showmore"

    keywords = "low+back+pain"
    start_urls = [
            "https://answers.yahoo.com/search/search_result?fr=uh3_answers_vert_gs&type=2button&p="+keywords+"&s=1"
            ]
    cookies = None
    
    def parse(self,response):
        global links
        global link
        links = response.xpath('//h3[@class="question-title"]/a/@href').extract()
        # time.sleep(5)

        item = YahooItem()
        
        for link in links:
            link = "https://answers.yahoo.com"+link
            yield Request(link,callback = self.parse_answer)

        # next page
        urls = response.xpath('//a[@class="ya-sr-next"]/@href').extract()
        if urls:
            for url in urls:
                url = "https://answers.yahoo.com/search/" + url
                yield Request(url,callback = self.parse)

    def parse_answer(self,response):
            # time.sleep(5)
            item = YahooItem()
            titles = response.xpath('//h1[@itemprop="name"]/text()').extract()
            l1 = response.xpath('//*[@id="Stencil"]/head/link[4]/@href').extract()
            q1 = response.xpath('//span[@class="D-n ya-q-full-text Ol-n"]/text()').extract()           
            if q1:
                questions = response.xpath('//span[@class="D-n ya-q-full-text Ol-n"]').extract()
            else:
                questions = response.xpath('//span[@itemprop="text"]').extract()
            c1 = response.xpath('//div[@id="brdCrb"]/a[3]/text()').extract()
            if c1:
                cates = response.xpath('//div[@id="brdCrb"]/a[3]/text()').extract()
            else:
                cates = response.xpath('//div[@id="brdCrb"]/a[2]/text()').extract()
            for i in range(len(titles)):
                t = lxml.html.fromstring(questions[i])
                data = t.text_content()
                yield YahooItem(title = titles[i], ques = data, cate = cates[i], link = l1[i])