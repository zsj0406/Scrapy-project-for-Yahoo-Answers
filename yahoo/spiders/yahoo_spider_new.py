# import scrapy
# from yahoo.items import YahooItem
# # from scrapy.contrib.linkextractors import LinkExtractor
# from scrapy.http import Request

# class yahooSpider(scrapy.Spider):
# 	name = "yahoo_new"	
# 	keywords = "teeth+pain"
# 	start_urls = [
# 			"https://answers.yahoo.com/search/search_result?fr=uh3_answers_vert_gs&type=2button&p=" 
# 			+ keywords + "&s=1"
# 			]
# 	# srart_urls = ["https://answers.yahoo.com/search/search_result?fr=uh3_answers_vert_gs&type=2button&p=chest+pain&s=1"]
# 	cookies = None


# 	# def start_request(self):
# 	# 	return [FormRequest("hhttps://answers.yahoo.com/search/search_result?fr=uh3_answers_vert_gs&type=2button&p=chest+pain&s=1", 
# 	# 		callback = self.pre)]
# 	# print "start yahoo new"

# 	def parse(self,response):
# 		#add website pages
# 		urls = response.xpath('//div[@id="ya-sr-pg"]/a/@href').extract()
# 		for url in urls:
# 			url = "https://answers.yahoo.com/search/" + url
# 			links = response.xpath('//h3[@class="question-title"]/a/@href').extract()
# 			for link in links:
# 				link = "https://answers.yahoo.com"+link
# 				yield Request(link,callback = self.parse)

# 	def parse_answer(self,response):
# 			item = YahooItem()
# 			titles = response.xpath('//h1[@itemprop="name"]/text()').extract()
# 			questions = response.xpath('//span[@class="D-n ya-q-full-text Ol-n"]/text()').extract()
# 			cates = response.xpath('//div[@itemprop="breadcrumb"]/text()').extract()
# 			for i in range(len(titles)):
# 				yield YahooItem(title = titles[i], ques = questions[i], cate = cates[i])
