import logging
import time
import scrapy
import json
import re
from lxml import etree
from wang.settings import COOKIES_DETAIL
from wang.model.chaoyang_park_comment import ChaoyangParkComment
from wang.utils import *
from wang.const import mfw_park_id


class CommentSpider(scrapy.Spider):
    name = "comment_mfw"
    cookies = []

    def __init__(self, id=None, *args, **kwargs):
        super(CommentSpider, self).__init__(*args, **kwargs)
        if id == None:
            return
        self.id = id
        self.park_name = "ritan"
        self.source = 0
        self.poi = mfw_park_id.get(self.park_name)
        self.url = "https://pagelet.mafengwo.cn/poi/pagelet/poiCommentListApi?callback=jQuery18107015652895717579_1638438784262&params=%7B%22poi_id%22%3A%22{}%22%2C%22page%22%3A{}%2C%22just_comment%22%3A1%7D&_ts=1638438796486&_sn=191eb3a2b0&_=1638438796487".format(self.poi,id)

        
    def start_requests(self):
        self.cookies = {i.split("=")[0]: i.split("=")[1]
                        for i in COOKIES_DETAIL.split("; ")}
        
        self.log("start scrapy, url: {}".format(self.url))
        headers = {
            "scheme": "https",
            "referer": "https://www.mafengwo.cn/poi/{}.html".format(self.poi),
            "authority": "pagelet.mafengwo.cn"
        }
        yield scrapy.Request(url=self.url, callback=self.parse, cookies=self.cookies,headers=headers)

    def parse(self, response):
        resp = re.search(r'{"data":([\s\S]*)}}', response.body.decode()).group()
        data = json.loads(resp)
        selector=etree.HTML(data.get("data",{}).get("html",""))
        filename = f'comment.html'
        with open(filename, 'wb') as f:
            f.write(data.get("data",{}).get("html","").encode())
        
        content = HandleTextList(selector.xpath(
            '//p[@class="rev-txt"]/text()'))
        user_name = selector.xpath(
            '//a[@class="name"]/text()')
        publish_time = selector.xpath(
            '//span[@class="time"]/text()')
        span_star = re.findall(r'<span class="s-star s-star\d"></span>', data.get("data",{}).get("html",""))
        star = [int(item[26:27]) for item in span_star]

        if len(content) != len(user_name):
            self.log("len don't match!!, content = {}, user_name = {}".format(len(content), len(user_name)), level=logging.ERROR)
        i=0
        while i< len(content):
            try:
                res = {
                    "user_name": user_name[i],
                    "content": content[i],
                    "star": star[i],
                    "publish_time": publish_time[i],
                    "source": self.source,
                    "park_name": self.park_name
                }
                self.log(res, level=logging.ERROR)
                ChaoyangParkComment.insert(res).execute()
            except Exception as e:
                self.log("Create Content err: {}".format(e), level=logging.ERROR)
            i = i+1
        self.log("Create Content success!", level=logging.ERROR)
