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

    keywords = "headache"
    start_urls = [
            "https://answers.yahoo.com/search/search_result?fr=uh3_answers_vert_gs&type=2button&p="+keywords+"&s=1"
            ]
    # srart_urls = ["https://answers.yahoo.com/question/index?qid=20110713135545AAwsbf6"]
    cookies = None
    
    def parse(self,response):
        # print response.url
        # print response
        # urls = response.xpath('//div[@id="ya-sr-pg"]/a[@class="ya-sr-next"]/@href').extract()
        links = response.xpath('//h3[@class="question-title"]/a/@href').extract()
        # item = YahooItem()
        # time.sleep(5)
        for link in links:
            link = "https://answers.yahoo.com"+link
            yield Request(link,callback = self.parse_answer)

        urls = response.xpath('//a[@class="ya-sr-next"]/@href').extract()
        if urls:
            for url in urls:
                url = "https://answers.yahoo.com/search/" + url
                # yield YahooItem(url = link[i])
                yield Request(url,callback = self.parse)

    def parse_answer(self,response):
        # for sel in response.xpath('//ul'):
            # print response
            # time.sleep(5)
            item = YahooItem()
            titles = response.xpath('//h1[@itemprop="name"]/text()').extract()
            print titles
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
                print titles[i]
                yield YahooItem(title = titles[i], ques = data, cate = cates[i])




