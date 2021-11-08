import logging
import time
import scrapy
import json
import re
from lxml import etree
from wang.model.chaoyang_park_comment import ChaoyangParkComment
from wang.utils import *


class ChaoyangSpider(scrapy.Spider):
    name = "chaoyang"
    cookies = []

    def __init__(self, id=None, *args, **kwargs):
        super(ChaoyangSpider, self).__init__(*args, **kwargs)
        if id == None:
            return
        self.id = id
        # 0: 朝阳公园90782
        # 1: 紫竹院公园76636
        self.url = "https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList?_fxpcqlniredt=09031016118352743163&x-traceID=09031016118352743163-1633701366720-9895923"
        # 2: 中山公园76635
        # 3: 奥林匹克森林公园
        # 4: 玉渊潭公园84758

        self.cookie = "_ga=GA1.2.154392288.1583660238; MKT_CKID=1583660239407.7opl2.fsaw; _RSG=V7aggpYzIHBtiCe9bDDkdA; _RDG=28db1243f91e6f2bfa3992d46e50470510; _RGUID=b452f62c-eaaa-41df-a9ee-34d949a0cb37; nfes_isSupportWebP=1; _RF1=36.110.2.34; MKT_CKID_LMT=1633665493668; _gid=GA1.2.2033470670.1633665495; _gat=1; _bfa=1.1583660235564.2fqtja.1.1584421364418.1633665487811.5.6; _bfs=1.2; _bfi=p1%3D290510%26p2%3D290510%26v1%3D6%26v2%3D5; _jzqco=%7C%7C%7C%7C%7C1.1338445489.1633665493663.1633665493663.1633665533031.1633665493663.1633665533031.0.0.0.2.2; __zpspc=9.3.1633665493.1633665533.2%234%7C%7C%7C%7C%7C%23"

    def start_requests(self):
        self.cookies = {i.split("=")[0]: i.split("=")[1]
                        for i in self.cookie.split("; ")}
        self.log("start scrapy, url: {}".format(self.url))
        body_raw = "{\"arg\":{\"channelType\":2,\"collapseType\":0,\"commentTagId\":0,\"pageIndex\":2,\"pageSize\":10,\"poiId\":90782,\"sourceType\":1,\"sortType\":1,\"starType\":0},\"head\":{\"cid\":\"09031016118352743163\",\"ctok\":\"\",\"cver\":\"1.0\",\"lang\":\"01\",\"sid\":\"8888\",\"syscode\":\"09\",\"auth\":\"\",\"xsid\":\"\",\"extension\":[]}}"
        body = json.loads(body_raw)
        body["arg"]["pageIndex"] = self.id
        # 不同公园要修改此处
        body["arg"]["poiId"] = 76635
        self.source = 2

        headers = {
            "cookieorigin": "https://you.ctrip.com",
            "authority": "m.ctrip.com"
        }
        yield scrapy.Request(url=self.url, callback=self.parse, cookies=self.cookies,body=json.dumps(body), method='POST')

    def parse(self, response):
        data = json.loads(response.body.decode()).get("result",{}).get("items",[])

        for item in data:
            publish_time = int(item.get("publishTime")[6:16])
            timeArray = time.localtime(publish_time)
            timeStr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            scores = item.get("scores", [])
            star = 0
            extra = []
            if scores:
                star = scores[0].get("score",0)
                for one in scores:
                    extra.append({"name":one.get("name",""),"score":one.get("score",0)})

            res = {
                "user_name": item.get("userInfo", {}).get("userNick"),
                "content": item.get("content"),
                "star": star,
                "extra": extra,
                "publish_time": timeStr,
                "source": self.source
            }
            self.log(res,logging.WARNING)
            try:
                ChaoyangParkComment.insert(res).execute()
            except Exception as e:
                self.log("Create Content err: {}".format(
                    e), level=logging.ERROR)
        self.log("Create Content success!")
