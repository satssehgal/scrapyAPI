from __future__ import unicode_literals
import scrapy

dictionary = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}

pages=int(input('How Many Pages Do you Want to Scrape?'))

class ThespiderSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/catalogue/page-{}.html'.format(i+1) for i in range(pages)]
    
    def parse(self, response):
        data={}
        books=response.css('ol.row')
        for book in books:
            for b in book.css('article.product_pod'):
                yield {
                    'Title' : b.css('a::attr(title)').getall()[0],
                    'Price' : b.css('div.product_price p.price_color::text').getall()[0],
                    'Stock' : b.css('div.product_price p.instock.availability::text').getall()[1].strip(),
                    'Star' : [v for k,v in dictionary.items() if k in b.css('p::attr(class)').getall()[0].split()[-1]][0]
                }

              
