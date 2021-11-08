import logging
import scrapy
import re
import time
from wang.model.ctrip_detail_link import CtripDetailLink


class BamaLinkSpider(scrapy.Spider):
    name = "bama_link"

    def start_requests(self):
        cookies = "_ga=GA1.2.154392288.1583660238; MKT_CKID=1583660239407.7opl2.fsaw; _RSG=V7aggpYzIHBtiCe9bDDkdA; _RDG=28db1243f91e6f2bfa3992d46e50470510; _RGUID=b452f62c-eaaa-41df-a9ee-34d949a0cb37; GUID=09031016118352743163; nfes_isSupportWebP=1; nfes_isSupportWebP=1; MKT_Pagesource=PC; _RF1=36.110.2.34; ASP.NET_SessionSvc=MTAuMTQuMjA2LjExNnw5MDkwfG91eWFuZ3xkZWZhdWx0fDE2MjMxNDM0NTY1NDE; MKT_CKID_LMT=1633863484295; _gid=GA1.2.98699611.1633863485; _bfa=1.1583660235564.2fqtja.1.1633701274853.1633863482356.9.29; _bfs=1.4; _jzqco=%7C%7C%7C%7C%7C1.1338445489.1633665493663.1633863576704.1633863613275.1633863576704.1633863613275.0.0.0.22.22; __zpspc=9.7.1633863484.1633863613.4%234%7C%7C%7C%7C%7C%23; appFloatCnt=9; _bfi=p1%3D290570%26p2%3D290570%26v1%3D29%26v2%3D28"
        cookies = {i.split("=")[0]: i.split("=")[1]
                   for i in cookies.split("; ")}
        i = 1
        while i <= 20:
            url = "https://you.ctrip.com/travels/bama3041/t3-p{}.html".format(
                i)
            i += 1
            yield scrapy.Request(url=url, callback=self.parse, cookies=cookies)

    def parse(self, response):
        links = response.xpath(
            '//a[@class="journal-item cf"]/@href').extract()
        self.log(links, logging.WARNING)

        for item in links:
            res = {
                "name": "bama",
                "content": item,
            }
            try:
                CtripDetailLink.insert(res).execute()
            except Exception as e:
                self.log("insert ctrip link error :".format(
                    e), level=logging.ERROR)
