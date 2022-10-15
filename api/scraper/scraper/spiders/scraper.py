import json
from scrapy.utils.project import get_project_settings
import scrapy
import psycopg2

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
                dataitem = (
                    i+1,
                     response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/a/text()')[i].get(),
                    #[0] has been used to extract the string from a list of one element
                    #There are 8 rows, hence i*8 has been used to extract each attribute from the row i
                     response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[1+(i*8)].getall()[0],
                     response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[2+(i*8)].getall()[0],
                     response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[3+(i*8)].getall()[0],
                     response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[4+(i*8)].getall()[0],
                     response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[5+(i*8)].getall()[0],
                     response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[6+(i*8)].getall()[0],
                     response.xpath('//div[@id="indexes-div"]/div/div/table/tr/td/text()')[7+(i*8)].getall()[0],
                )
                print(dataitem)
                data.append(dataitem)
                i+=1
        bulkInsert(data)

def bulkInsert(records):
    try:
        connection = psycopg2.connect(
                                      database="mystats")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM db_statslist", ())
        sql_insert_query = """ INSERT INTO db_statslist (id,Symbol,Last,Change,Changeperc,Close,High,Low,LastTrade) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) """

        # executemany() to insert multiple rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into statslist table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into statslist table {}".format(error))

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")




