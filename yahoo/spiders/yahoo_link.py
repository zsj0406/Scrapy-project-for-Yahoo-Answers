import scrapy
from yahoo.items import YahooItem
from scrapy.http import Request
from scrapy.http import Request,FormRequest
import time

class yahooSpider(scrapy.Spider):
	name = "yahoo_link"
	keywords = "low+back+pain"
	start_urls = [
			"https://answers.yahoo.com/search/search_result?fr=uh3_answers_vert_gs&type=2button&p=" 
			+ keywords + "&s=1"
			]
	cookies = None

	def parse(self,response):
			item = YahooItem()
			time.sleep(3)
			titles = response.xpath('//h3[@class="question-title"]/a/text()').extract()
			links = response.xpath('//h3[@class="question-title"]/a/@href').extract()
			for i in range(len(links)):
				links[i] = "https://answers.yahoo.com"+links[i]

			for i in range(len(titles)):
				yield YahooItem(title = titles[i], link = links[i])
			