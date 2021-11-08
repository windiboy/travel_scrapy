from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from wang.settings import COOKIES_DETAIL
from wang.model.mfw_detail_page import MfwDetailLink
from wang.utils import *


class Controller():
    name = "controller"
    cookies = []

    def run(self):
        setting = get_project_settings()
        start = 450
        step = 100
        while start <= 500:
            process = CrawlerProcess(setting)
            self.cookies = {i.split("=")[0]: i.split("=")[1]
                            for i in COOKIES_DETAIL.split("; ")}
            rows = MfwDetailLink.select().where(MfwDetailLink.id.between(start, start+step)
                                                ).order_by(MfwDetailLink.id.desc())
            for row in rows:
                process.crawl("detail", row.link_id)
            print("start scrapy, start:{}, end:{}".format(start, start+step))
            process.start()
            break
            start += step

if __name__ == '__main__':
    control = Controller()
    control.run()
