import json
from scrapy.utils.project import get_project_settings
import scrapy
import django

class McxSpider(scrapy.Spider):
    name = 'mcx'
    start_urls = [
            'https://mcxlive.org.html'
            ]
    def parse(self, response):
        # links = response.css('a').xpath('@href').getall()
        heading = response.xpath('//td[1]').getall()
        i=1
        data = []
        while i<(len(heading)):
            dataitem = {
                "Symbol" : response.xpath('//td[]')[i].get(),
                'Last' : response.xpath('//td[1]')[i].get(),
                'Change' : response.xpath('//td[1]')[i].get(),
                'Change%' : response.xpath('//td[1]')[i].get(),
                'Close' : response.xpath('//td[1]')[i].get(),
                'High' : response.xpath('//td[1]')[i].get(),
                'Low' : response.xpath('//td[1]')[i].get(),
                'Last Trade' : response.xpath('//td[1]')[i].get(),
            }
            data.append(dataitem)
            i+=1
        firebase_store(data)
