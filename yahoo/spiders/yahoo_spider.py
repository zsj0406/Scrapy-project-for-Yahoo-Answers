import scrapy
from yahoo.items import YahooItem
# from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request

class yahooSpider(scrapy.Spider):
	name = "yahoo"
	keywords = "teeth+pain"
	start_urls = [
			"https://answers.yahoo.com/search/search_result?fr=uh3_answers_vert_gs&type=2button&p=" 
			+ keywords + "&s=1"
			]
	# srart_urls = ["https://answers.yahoo.com/dir/index?sid=396547122"]
	cookies = None

	# rules = (
	# 	Rule(LinkExtractor(allow =r"" ),
	# 	callback = "parse", follow = True),
	# )

	def parse(self,response):
		# for sel in response.xpath('//ul'):
			item = YahooItem()
			# item = []
			# item['title'] = response.xpath('//h3[@class="question-title"]/a/text()').extract()
			# item['ques'] = response.xpath('//span[@class="question-description"]/text()').extract()
			# item['cate'] = response.xpath('//div[@class="question-meta"]/a/text()').extract()
			# # item.append(item)
			titles = response.xpath('//h3[@class="question-title"]/a/text()').extract()
			questions = response.xpath('//span[@class="question-description"]/text()').extract()
			cates = response.xpath('//div[@class="question-meta"]/a/text()').extract()
			links = response.xpath('//h3[@class="question-title"]/a/@href').extract()
			# links = "https://answers.yahoo.com" + links
			for i in range(len(titles)):
				yield YahooItem(title = titles[i], ques = questions[i], cate = cates[i],link = links[i])
			urls = response.xpath('//div[@id="ya-sr-pg"]/a/@href').extract()
			for url in urls:
				url = "https://answers.yahoo.com/search/" + url
				yield Request(url,callback = self.parse)
			


	# def get_title(self,response,item):
	# 	item['title'] = response.xpath('//h3[@class="question-title"]/a/text()').extract()