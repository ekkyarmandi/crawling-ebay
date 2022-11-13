import scrapy
from urllib.parse import urlparse
from urllib.parse import parse_qs
from datetime import datetime
import re


class EbaySpiderSpider(scrapy.Spider):
    name = 'ebay_spider'
    allowed_domains = ['ebay.com']
    start_urls = ['https://www.ebay.com/sch/i.html?_nkw=keyboard']

    def parse(self, response):

        # get all products
        items = response.css('ul.srp-list li')
        parsed_url = urlparse(response.url)
        kw = parse_qs(parsed_url.query)['_nkw'][0]
        for item in items:

            watchers = item.css('span.s-item__watchCountTotal ::text').get()
            if not watchers:
                watchers = 0

            is_free_returns = item.css('span.s-item__freeReturnsNoFee ::text').get()
            if is_free_returns:
                is_free_returns = True
            else:
                is_free_returns = False

            shipping_info = item.css('span.s-item__logisticsCost ::text').get()
            if shipping_info:
                cost = re.search('[0-9\+\.\,\$]+',shipping_info)
                if cost:
                    shipping_info = cost.group()

            result = dict(
                sraped_datetime=datetime.now().strftime('%Y-%m-%d_%T'),
                title=item.css('div.s-item__title ::text').get(),
                link=item.css('a.s-item__link::attr(href)').get(),
                image_url=item.css('img.s-item__image-img::attr(src)').get(),
                secondary_info=item.css('div.s-item__subtitle ::text').get(),
                product_price=item.css('span.s-item__price ::text').get(),
                shipping_info=item.css('span.s-item__logisticsCost ::text').get(),
                shipping_origin=item.css('span.s-item__itemLocation ::text').get(),
                product_sold=item.css('span.s-item__quantitySold ::text').get(),
                watchers=watchers,
                is_free_returns=is_free_returns,
            )
            if result['link'] and kw in result['title'].lower():
                yield result

        # find the next page
        next_url = response.css('a.pagination__next::attr(href)').get()
        yield scrapy.Request(next_url, callback=self.parse)