import scrapy

class DocSectionItem(scrapy.Item):
    # section_name attribute is of type scrapy.Field()
    section_name = scrapy.Field()
    section_link = scrapy.Field()

class PythonDocumentationSpider(scrapy.Spider):
    name = 'pydoc_bot'
    start_urls = ['https://docs.python.org/3/']

    def parse(self, response):
        for a_el in response.xpath('//table[@class="contentstable"]//a[@class="biglink"]'):
            section = DocSectionItem()
            section['section_name'] = a_el.xpath('./text()').extract()[0]
            section['section_link'] = a_el.xpath('./@href').extract()[0]
            # print(type(section))
            yield section