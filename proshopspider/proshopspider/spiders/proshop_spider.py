import scrapy

class ProshopSpider(scrapy.Spider):
    name = "proshop"
    start_urls = ["http://proshop.dk/", ]

    def parse(self,response):
        for item in response.css('div.site-bar-menu'):

            yield {
                'title' : item.css('li a::text').getall()
            }

#TODO Yield of custom search terms, and the details of these items.
#TODO Yield of price reductions and short term deals. 