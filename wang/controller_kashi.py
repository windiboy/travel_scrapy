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
        start = 0
        step = 1
        end = 10

        process = CrawlerProcess(setting)
        self.cookies = {i.split("=")[0]: i.split("=")[1]
                        for i in COOKIES_DETAIL.split("; ")}
        while start <= end:
            process.crawl("comment", start)
            start += step
        print("start scrapy, start:{}, end:{}".format(start, end))
        process.start()

if __name__ == '__main__':
    control = Controller()
    control.run()
