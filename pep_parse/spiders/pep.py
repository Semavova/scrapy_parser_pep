import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css('#numerical-index tbody a[href]')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': int(
                response.css(
                    'head title::text'
                ).get().replace('PEP ', '').split(' – ')[0]
            ),
            'name': response.css(
                'head title::text'
            ).get().split(' – ')[-1].split(' |')[0],
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        }
        yield PepParseItem(data)
