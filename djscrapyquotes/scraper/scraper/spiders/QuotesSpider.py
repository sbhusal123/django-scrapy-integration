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