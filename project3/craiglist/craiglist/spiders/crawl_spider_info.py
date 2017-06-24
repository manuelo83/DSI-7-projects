import scrapy
from craiglist.items import CraiglistItem
from bs4 import BeautifulSoup as bs
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
import pandas as pd

class CraiglistBaseSpider(CrawlSpider):
	### CrawlSpider
	### scrapy.Spider #individual spider
	# unique name/alias for the spider
	name = "craiglistCrawl"

	# where the spider will go
	urls = pd.read_csv('/Users/manuel/Desktop/dsi-sf-7-materials_manuel/projects/project-3/lista_us_cities.csv')
	urls = urls['0'].tolist()
	city_urls = []
	for url in urls:
	    if ' ' not in url:
	        city_urls.append("http://{}.craigslist.org/search/sss?query=rv".format(url))

	start_urls = city_urls
	# start_urls = ['http://chicago.craigslist.org/search/sss?query=rv']

	# rule to crawl next pages
	rules = (Rule(LinkExtractor(restrict_xpaths = ['//span/a[@class="button next"]']), follow = True, callback = 'parse_data'),)

	def parse_data(self,response):
		### parse_data for the rule, otherwise keep it plain PARSE
		# hxs = HtmlXPathSelector(response)

		titles = response.xpath('//p/a/text()').extract()
		# titles = hxs.xpath
		# cities = response.xpath('//span/span[@class="result-hood"]/text()').extract()
		prices = response.xpath('//span[@class="result-price"]/text()').extract()

		for title, price in zip(titles, prices):
			item = CraiglistItem()
			item['title'] = title
			item['city'] = response.xpath('//span/a/text()').extract()[0]
			item['price'] = int(price.strip('$'))
			yield item
