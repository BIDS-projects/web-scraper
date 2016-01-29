from utils.items import EdgeItem, VertexItem


class LinkItem(VertexItem):
    base_url = scrapy.Field()
    url = scrapy.Field()
    link = scrapy.Field()
    timestamp = scrapy.Field()

class TextItem(VertexItem):
    base_url = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()
    timestamp = scrapy.Field()
