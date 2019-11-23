import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes_spider'  
    start_urls = ['http://quotes.toscrape.com/page/1/']


    def parse(self, response):
        filename_quotes = 'quotes.txt'
        filename_auth = 'auth.txt'

        # Extrai todas as frases da página
        with open(filename_quotes, 'w') as f:
            for quote in response.css('span.text::text').getall():
                f.write(quote)


        #extrai todos os autores da página]
        with open(filename_auth, 'w') as f:
            for auth in response.css('small.author::text').getall():
                f.write(auth)
