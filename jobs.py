import scrapy

class JobItem(scrapy.Item):
    # Data structure to store the title, company name and location of the job
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    
class StackOverflowSpider(scrapy.Spider):
    name = 'jobs' 
    start_urls = ['https://stackoverflow.com/jobs?med=site-ui&ref=jobs-tab']
    
    def parse(self, response):
        for a_el in response.xpath('//div[@class="listResults"]'):
            section = DocSectionItem()
            section['title'] = a_el.xpath('.//a[@class="s-link stretched-link"]/@title').extract()
            section['company'] = a_el.xpath('.//h3[@class="fc-black-700 fs-body1 mb4"]/span[1]/text()')
            section['location'] = a_el.xpath('.//h3[@class="fc-black-700 fs-body1 mb4"]/span[2]/text()').extract()
            yield section
        