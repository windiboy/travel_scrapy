import logging
import time
import scrapy
import json
import re
from lxml import etree
from wang.model.kashi_comment import KashiComment
from wang.utils import *


class CtripKashiSpider(scrapy.Spider):
    name = "CtripKashi"
    cookies = []

    def __init__(self, id=None, *args, **kwargs):
        super(CtripKashiSpider, self).__init__(*args, **kwargs)
        if id == None:
            return
        self.id = id
        self.url = "https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList?_fxpcqlniredt=09031167419349745447&x-traceID=09031167419349745447-1636371185309-3121230"

        self.cookie = "_ga=GA1.2.154392288.1583660238; MKT_CKID=1583660239407.7opl2.fsaw; _RSG=V7aggpYzIHBtiCe9bDDkdA; _RGUID=b452f62c-eaaa-41df-a9ee-34d949a0cb37; _RDG=28db1243f91e6f2bfa3992d46e50470510; nfes_isSupportWebP=1; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; appFloatCnt=23; GUID=09031167419349745447; librauuid=5oZmuX34bDaOug4L; ibu_h5_lang=en; ibu_h5_local=en-us; _pd=%7B%22r%22%3A11%2C%22d%22%3A226%2C%22_d%22%3A215%2C%22p%22%3A226%2C%22_p%22%3A0%2C%22o%22%3A228%2C%22_o%22%3A2%2C%22s%22%3A228%2C%22_s%22%3A0%7D; _RF1=106.39.42.238; _gid=GA1.2.778923893.1636370828; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&createtime=1636370828&Expires=1636975628131; MKT_CKID_LMT=1636370828162; MKT_Pagesource=PC; _bfs=1.2; _bfa=1.1583660235564.2fqtja.1.1636370804427.1636370825371.14.54.10650043435; _bfi=p1%3D290510%26p2%3D100101991%26v1%3D54%26v2%3D53; _jzqco=%7C%7C%7C%7C%7C1.1338445489.1633665493663.1636370828159.1636370842184.1636370828159.1636370842184.0.0.0.44.44; __zpspc=9.12.1636370828.1636370842.2%232%7Cwww.baidu.com%7C%7C%7C%7C%23"

    def start_requests(self):
        self.cookies = {i.split("=")[0]: i.split("=")[1]
                        for i in self.cookie.split("; ")}
        self.log("start scrapy, url: {}".format(self.url))
        body_raw = "{\"arg\":{\"channelType\":2,\"collapseType\":0,\"commentTagId\":0,\"pageIndex\":2,\"pageSize\":10,\"poiId\":90782,\"sourceType\":1,\"sortType\":3,\"starType\":0},\"head\":{\"cid\":\"09031016118352743163\",\"ctok\":\"\",\"cver\":\"1.0\",\"lang\":\"01\",\"sid\":\"8888\",\"syscode\":\"09\",\"auth\":\"\",\"xsid\":\"\",\"extension\":[]}}"
        body = json.loads(body_raw)
        body["arg"]["pageIndex"] = self.id
        # 不同地方要修改此处
        body["arg"]["poiId"] = 93884
        # 0马蜂窝 1携程 2去哪儿
        self.source = 1

        yield scrapy.Request(url=self.url, callback=self.parse, cookies=self.cookies,body=json.dumps(body), method='POST')

    def parse(self, response):
        data = json.loads(response.body.decode()).get("result",{}).get("items",[])

        for item in data:
            publish_time = int(item.get("publishTime")[6:16])
            timeArray = time.localtime(publish_time)
            timeStr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            scores = item.get("scores", [])
            star = item.get("score",0)
            extra = []
            if scores:
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
                KashiComment.insert(res).execute()
            except Exception as e:
                self.log("Create Content err: {}".format(
                    e), level=logging.ERROR)
        self.log("Create Content success!")
