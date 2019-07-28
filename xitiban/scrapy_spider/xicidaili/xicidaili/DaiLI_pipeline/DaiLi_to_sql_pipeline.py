from scrapy_spider.xicidaili.xicidaili.DaiLI_pipeline.mysql import Sql


class Daili_pipeline(object):
    def process_item(self, item, spider):
        Sql.insert_to_sql(item)
        return item