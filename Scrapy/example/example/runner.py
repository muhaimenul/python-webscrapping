# custom made by muhaimenul
from scrapy.cmdline import execute

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