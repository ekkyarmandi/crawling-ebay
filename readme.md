# Ebay Product Data Crawling

Ebay product data scraping/crawling using [Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html)

### How to run
#### 1. Clone RepO
```cmd
git clone https://github.com/ekkyarmandi/crawling-ebay.git
```

#### 2. Install Dependencies
```cmd
pip install requirements.txt
```

### 3. Change the search keyword
Open the [spider](ebay/spiders/ebay_spider.py), change the `_nkw` url parameter with your keyword or you can add more queries into the `start_urls`
```python
class EbaySpiderSpider(scrapy.Spider):
    name = 'ebay_spider'
    allowed_domains = ['ebay.com']
    start_urls = ['https://www.ebay.com/sch/i.html?_nkw=<your-keyword-here>']
```
or
```python
class EbaySpiderSpider(scrapy.Spider):
    name = 'ebay_spider'
    allowed_domains = ['ebay.com']
    start_urls = [
        'https://www.ebay.com/sch/i.html?_nkw=keyword1',
        'https://www.ebay.com/sch/i.html?_nkw=keyword2',
    ]
```

### 4. Run the crawler
```
scrapy crawl ebay_spider
```
You also can specify the output as json or csv file by adding -o parameter
```
scrapy crawl ebay_spider -o results.json
```
or
```
scrapy crawl ebay_spider -o results.csv
```

### Current Issue
* The spider only capable to crawl the page up to 5 pages