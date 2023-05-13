import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{url}/' for url in allowed_domains]

    def parse(self, response):
        for pep_link in response.css('#numerical-index tbody a[href]'):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css(
            'head title::text'
        ).get().split(' – ', maxsplit=1)
        yield PepParseItem(
            number=number.replace('PEP ', ''),
            name=name.replace(' | peps.python.org', ''),
            status=response.css('dt:contains("Status") + dd abbr::text').get(),
        )
