from scrapy import Spider
from scrapy.selector import Selector


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["https://zor.uzhttps://zor.uz/cat/arenda-kvartir/page/1"]
    start_urls = [
        "",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')