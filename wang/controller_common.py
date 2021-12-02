from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from wang.settings import COOKIES_DETAIL
from wang.utils import *


class Controller():
    name = "controller"
    def run(self):
        setting = get_project_settings()
        start = 1
        step = 1
        end = 5

        process = CrawlerProcess(setting)
        print("start scrapy, start:{}, end:{}".format(start, end))
        while start <= end:
            process.crawl("comment_mfw", start)
            start += step
        process.start()

if __name__ == '__main__':
    control = Controller()
    control.run()
