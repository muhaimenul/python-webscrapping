import scrapy

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
        print(response.body)
        # with open(filename, 'wb') as html_file:
        #     html_file.write(response.body)

