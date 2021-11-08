from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from wang.model.ctrip_detail_link import CtripDetailLink
from wang.utils import *


class Controller():
    name = "controller"

    def run(self):
        setting = get_project_settings()
        start = 150
        end = 170

        process = CrawlerProcess(setting)
        # test
        # process.crawl("bama_detail", row.content)
        rows = CtripDetailLink.select().where(CtripDetailLink.id.between(start, end))
        for row in rows:
            process.crawl("bama_detail", row.content)
        print("start scrapy, start:{}, end:{}".format(start, end))
        process.start()


if __name__ == '__main__':
    control = Controller()
    control.run()
