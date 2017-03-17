import scrapy

class BetSpider(scrapy.Spider):
    name = 'betspider'
    start_urls = ['https://www.betbrain.com/football/england/premier-league/']

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        next_page = response.css('div.prev-post > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
