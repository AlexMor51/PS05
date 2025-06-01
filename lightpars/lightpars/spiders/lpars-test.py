import scrapy


class LparsSpider(scrapy.Spider):
    name = "lpars-test"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css('div.lcSMD')
        for light in lights:
            yield  {
                'name' :  light.css('div.lsooF span::text').getall()[0],
                'price': light.css('div.lsooF span::text').getall()[1],
                'url': light.css('a::attr(href)').get()

            }