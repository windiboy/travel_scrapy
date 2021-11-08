import logging
import scrapy
import re
import time
from wang.settings import COOKIES
from wang.model.mfw_detail_page import MfwDetailLink


class MafengwoSpider(scrapy.Spider):
    name = "all_page"

    def start_requests(self):
        cookies = COOKIES
        cookies = {i.split("=")[0]: i.split("=")[1]
                   for i in cookies.split("; ")}
        url = "https://www.mafengwo.cn/gonglve/ajax.php?act=get_travellist"
        i = 1
        while i <= 142:
            i += 1
            myFormData = {
                "mddid": "10758",
                "pageid": "mdd_index",
                "sort": "1",
                "cost": "0",
                "days": "0",
                "month": "0",
                "tagid": "0",
                "page": str(i),
                "_ts": "1631624286528",
                "_sn": "468aeb20b1",
            }
            yield scrapy.FormRequest(url=url, callback=self.parse, cookies=cookies, method='POST', formdata=myFormData)
            time.sleep(1.0)

    def parse(self, response):
        pattern = re.compile(r'/\d+.html')   # 查找数字
        urls = pattern.findall(response.text)
        urls = self.url_dedup(urls)
        self.log(f'save urls: {urls}')

        for item in urls:
            try:
                MfwDetailLink.insert(item).execute()
            except Exception as e:
                self.log("insert mfw link error :".format(
                    e), level=logging.ERROR)

    def url_dedup(self, urls):
        res = []
        i = 0
        while i+2 < len(urls):
            if urls[i] == urls[i+1] and urls[i] == urls[i+2]:
                res.append({"link_id": urls[i][1:-5]})
                i += 3
            else:
                i += 1
        return res
