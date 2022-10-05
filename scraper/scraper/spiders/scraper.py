import json
from scrapy.utils.project import get_project_settings
import scrapy
import django

class McxSpider(scrapy.Spider):
    name = 'mcx'
    start_urls = [
            'https://mcxlive.org'
            ]
    def parse(self, response):
        rows =  len(response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/a/text()').getall())
        i=0
        data = []
        while i<rows:
                dataitem = {
                    "Symbol" : response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/a/text()')[i].get(),
                    #[0] has been used to extract the string from a list of one element
                    #There are 8 rows, hence i*8 has been used to extract each attribute from the row i
                    'Last' : response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[1+(i*8)].getall()[0],
                    'Change' : response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[2+(i*8)].getall()[0],
                    'Change%' : response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[3+(i*8)].getall()[0],
                    'Close' : response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[4+(i*8)].getall()[0],
                    'High' : response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[5+(i*8)].getall()[0],
                    'Low' : response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[6+(i*8)].getall()[0],
                    'Last Trade' :response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[7+(i*8)].getall()[0],
                }
                print(dataitem)
                data.append(dataitem)
                i+=1
