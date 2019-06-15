# custom made by muhaimenul
form scrapy.cmdline import execute

try:
    execute(
        [
            'scrapy',
            'crawl',
            'stackoverflow'
        ]
    )

except SystemExit:
    pass