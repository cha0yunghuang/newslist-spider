import scrapy
from bs4 import BeautifulSoup
from newslist.items import NewslistItem

class setCrawler(scrapy.Spider):
    name = 'setnews-spider'
    start_urls = ['https://www.setn.com/ViewAll.aspx']

    def parse(self,response):
        domain = 'https://www.setn.com'
        res = BeautifulSoup(response.body)

        for news in res.select('.view-li-title'):
            yield scrapy.Request(domain + news.select('a')[0]['href'], self.parse_detail)
    

    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        setnewsItem = NewslistItem()
        setnewsItem['post_title'] = res.select('h1')[0].text
        setnewsItem['post_date'] = res.select('.page-date')[0].text
        return setnewsItem

        # ===> json: scrapy crawl setnews-spider -o setnews.json -t json
        # ===> csv: scrapy crawl setnews-spider -o setnews-spider.csv