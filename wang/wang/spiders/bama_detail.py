import logging
import scrapy
import re
import time
from wang.model.travel_content import TravelContent
from wang.utils import *


class BamaDetailSpider(scrapy.Spider):
    name = "bama_detail"

    def __init__(self, id=None, *args, **kwargs):
        super(BamaDetailSpider, self).__init__(*args, **kwargs)
        if id == None:
            return
        self.id = id

    def start_requests(self):
        cookies = "_ga=GA1.2.154392288.1583660238; MKT_CKID=1583660239407.7opl2.fsaw; _RSG=V7aggpYzIHBtiCe9bDDkdA; _RDG=28db1243f91e6f2bfa3992d46e50470510; _RGUID=b452f62c-eaaa-41df-a9ee-34d949a0cb37; GUID=09031016118352743163; nfes_isSupportWebP=1; nfes_isSupportWebP=1; MKT_Pagesource=PC; ASP.NET_SessionSvc=MTAuMTQuMjA2LjExNnw5MDkwfG91eWFuZ3xkZWZhdWx0fDE2MjMxNDM0NTY1NDE; MKT_CKID_LMT=1633863484295; _gid=GA1.2.98699611.1633863485; _bfa=1.1583660235564.2fqtja.1.1633863482356.1633866465198.10.32; _bfs=1.1; _jzqco=%7C%7C%7C%7C%7C1.1338445489.1633665493663.1633864492368.1633866465293.1633864492368.1633866465293.0.0.0.25.25; __zpspc=9.8.1633866465.1633866465.1%234%7C%7C%7C%7C%7C%23; appFloatCnt=12; _bfi=p1%3D290605%26p2%3D290605%26v1%3D32%26v2%3D31; _RF1=36.110.2.34"
        cookies = {i.split("=")[0]: i.split("=")[1]
                   for i in cookies.split("; ")}
        url = "https://you.ctrip.com" + self.id
        self.log(url, logging.WARNING)
        yield scrapy.Request(url=url, callback=self.parse, cookies=cookies)

    def parse(self, response):
        # self.log(response.xpath(
        #     '//div[@class="w_journey"]/dl/dt/span/text()').extract(), logging.WARNING)
        title = ConvertListToStr(response.xpath(
            '//div[@class="ctd_head_left"]/h2/text()').extract())

        user_name = ConvertListToStr(response.xpath(
            '//div[@class="ctd_head_right"]/p/a/@title').extract())
        
        days = ""
        days_str = response.xpath(
            '//div[@class="w_journey"]/dl/dt/span/text()').extract()
        if len(days_str)>0:
            days = ConvertListToStr(re.findall(r'\d+', days_str[0]))

        publish_time = response.xpath(
            '//div[@class="ctd_head_left"]/h2/@data-publishdate').extract()
        
        content = ConvertListToStr(response.xpath(
            '//div[@class="ctd_content wtd_content"]/p/text()').extract())

        if content == "":
            content = ConvertListToStr(response.xpath(
            '//div[@class="ctd_content"]/p/text()').extract())
        res = {
            "source": 1,
            "key_words": "巴马",
            "user_name": user_name,
            "title": title,
            "content": content,
        }
        if days:
            res["travel_days"] = int(days)
        if len(publish_time)>0:
            res["publish_time"] = publish_time
        self.log(res, logging.WARNING)
        try:
            TravelContent.insert(res).execute()
        except Exception as e:
            self.log("insert travel content error :".format(
                e), level=logging.ERROR)
