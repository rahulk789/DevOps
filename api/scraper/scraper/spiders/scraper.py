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

def bulkInsert(records):
    try:
        connection = psycopg2.connect(user="xenon",
                                      password="",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="mystats")
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO stats (id, model, price) VALUES (%s,%s,%s) """

        # executemany() to insert multiple rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into mobile t able {}".format(error))

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

records_to_insert = [(4, 'LG', 800), (5, 'One Plus 6', 950)]
bulkInsert(records_to_insert)

def updateInBulk(records):
    try:
        ps_connection = psycopg2.connect(user="xenon",
                                         password="",
                                         host="127.0.0.1",
                                         port="5432",
                                         database="mystats")
        cursor = ps_connection.cursor()

        # Update multiple records
        sql_update_query = """Update mobile set price = %s where id = %s"""
        cursor.executemany(sql_update_query, records)
        ps_connection.commit()

        row_count = cursor.rowcount
        print(row_count, "Records Updated")

    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if ps_connection:
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")


tuples = [(750, 4), (950, 5)]
updateInBulk(tuples)


