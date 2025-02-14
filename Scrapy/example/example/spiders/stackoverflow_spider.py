import scrapy
import datetime

class StackOverflowSpider(scrapy.Spider):
    name = "stackoverflow" # need to be unique because scraby will be look for the class with this name

    def start_requests(self):
        urls = [
            'https://stackoverflow.com/questions/tagged/python'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = "test.html"

        with open(filename, 'ab') as html_file:
            questions = response.xpath('//*[@class="grid--cell fl1 fs-body3 mr12"]/text()').get().strip()
            questions = questions[:-10]
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            output = questions + " | " + date + "\n"
            html_file.write(output.encode())

