# import scrapy
# from yahoo.items import YahooItem
# from spider.yahoo_spider_showmore import yahooSpider


#     def parse_link(self,response):
#         links = response.xpath('//h3[@class="question-title"]/a/@href').extract()
#         # time.sleep(5)
#         # print "links for answers"
#         # print links
#         # item = YahooItem()
#         for link in links:
#             link = "https://answers.yahoo.com"+link
#             # print link
#             # yield YahooItem(link = title[i])
#             yield Request(link,callback = self.parse_answer)

#     def parse_answer(self,response):
#         # for sel in response.xpath('//ul'):
#             # print response
#             # time.sleep(5)
#             item = YahooItem()
#             titles = response.xpath('//h1[@itemprop="name"]/text()').extract()
#             questions = response.xpath('//span[@class="D-n ya-q-full-text Ol-n"]/text()').extract()
#             cates = response.xpath('//div[@itemprop="breadcrumb"]/text()').extract()
#             for i in range(len(titles)):
#                 print titles[i]
#                 yield YahooItem(title = titles[i], ques = questions[i], cate = cates[i],links = links[i])