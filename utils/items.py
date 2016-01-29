"""
Scrapy Items
---
BIDS Institutional Ecosystem Mapping

These are ScraPy items emitted by the scraper. ScrapyHub only saves these items.
"""

import scrapy


class EdgeItem(scrapy.Item):
    base_url = scrapy.Field()
    url = scrapy.Field()
    link = scrapy.Field()
    timestamp = scrapy.Field()

class VertexItem(scrapy.Item):
    base_url = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()
    timestamp = scrapy.Field()
