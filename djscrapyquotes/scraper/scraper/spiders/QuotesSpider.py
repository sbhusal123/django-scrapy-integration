import scrapy
from ..items import QuotesItem

class QuotesSpider(scrapy.Spider):

    start_urls = ['https://quotes.toscrape.com/']

    name = "quotes"

    def parse(self, response, **kwargs):
        item = QuotesItem()

        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract_first().replace('”', '').replace("“", "")
            author = quote.css('.author::text').extract_first()

            item['text'] = title
            item['author'] = author
            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)