import scrapy
from ..items import QuotesItem

"""
command: scrapy crawl some-quotes -a author="<author_name>" -L WARN

Example: scrapy crawl some-quotes -a author="Albert Einstein" -L WARN

Those author name should match the name on the site.
"""

class SpecificAuthorQuotesSpider(scrapy.Spider):
    """Extracts the quotes from specific author"""

    start_urls = ['https://quotes.toscrape.com/']

    name = "some-quotes"

    def __init__(self, author=None, **kwargs):
        self.author = author
        super().__init__(**kwargs)

    def parse(self, response, **kwargs):
        item = QuotesItem()

        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract_first().replace('”', '').replace("“", "")
            author = quote.css('.author::text').extract_first()

            # Check if author's name matches
            if author.strip().lower() == self.author.strip().lower():
                item['text'] = title
                item['author'] = author
                yield item

        # Crawl Next Page
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)