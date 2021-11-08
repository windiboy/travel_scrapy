import time
import scrapy
import json
import re
from lxml import etree
from wang.settings import COOKIES_DETAIL
from wang.model.mfw_detail_page import MfwDetailLink
from wang.model.travel_content import TravelContent
from wang.utils import *


class MafengwoSpider(scrapy.Spider):
    name = "detail"
    cookies = []
    content = ""
    id = 0
    iid = 0
    next_seq = 0
    has_more = True

    def __init__(self, id=None, *args, **kwargs):
        super(MafengwoSpider, self).__init__(*args, **kwargs)
        if id == None:
            return
        self.id = id
        self.url = "https://www.mafengwo.cn/i/{}.html".format(id)

    def start_requests(self):
        self.cookies = {i.split("=")[0]: i.split("=")[1]
                        for i in COOKIES_DETAIL.split("; ")}
        
        self.log("start scrapy, url: {}".format(self.url))
        yield scrapy.Request(url=self.url, callback=self.parse, cookies=self.cookies)

    def parse(self, response):
        # 正文
        self.content = ConvertListToStr(response.xpath(
            '//p[@class="_j_note_content _j_seqitem"]/text()').extract())

        # 其余字段
        title = ConvertListToStr(response.xpath('//h1/text()').extract())
        user_name = ConvertListToStr(response.xpath(
            '//meta[@name="author"]/@content').extract())
        if user_name:
            user_name = user_name[9:]
        days_str = ConvertListToStr(response.xpath(
            '//li[@class="day"]/text()').extract())
        days = ConvertListToStr(re.findall(r'\d+', days_str))
        spend_str = ConvertListToStr(response.xpath(
            '//li[@class="cost"]/text()').extract())
        spend = ConvertListToStr(re.findall(r'\d+', spend_str))
        departure_time = ConvertListToStr(
            response.xpath('//li[@class="time"]/text()').extract())
        if departure_time:
            departure_time = departure_time[4:]

        # 异步加载正文补充
        iid = ConvertListToStr(re.findall(r'"new_iid":"\d+"', response.text))
        if iid:
            iid = iid[11:-1]
        else:
            self.log("Get rest Content err, iid={}".format(iid))
            return
        self.iid = iid
        self.next_seq = int(response.xpath(
            '//p[@class="_j_note_content _j_seqitem"]/@data-seq').extract()[-1])
        while self.has_more:
            rest_url = "https://www.mafengwo.cn/note/ajax/detail/getNoteDetailContentChunk?id={}&iid={}&seq={}&back=0".format(
                self.id, self.iid, self.next_seq)
            yield scrapy.Request(url=rest_url, callback=self.parse_rest, cookies=self.cookies)
            time.sleep(0.5)

        data = {
            "source": 0,
            "user_name": user_name,
            "title": title,
            "content": self.content,
            "travel_days": days,
            "travel_spend": spend,
            "departure_time": departure_time,
        }
        try:
            TravelContent.insert(data).execute()
        except Exception as e:
            self.log("Create Content err: {}".format(e))
            return
        self.log("Create Content success!")


    def parse_rest(self, response):
        data = json.loads(response.body.decode())
        self.has_more = data.get("data",{}).get("has_more","")
        if self.has_more == "":
            self.has_more = False

        selector=etree.HTML(data.get("data",{}).get("html",""))
        if selector == None:
            self.log("selector is None")
            return
        self.next_seq = int(selector.xpath(
            '//p[@class="_j_note_content _j_seqitem"]/@data-seq')[-1])

        self.content += ConvertListToStr(selector.xpath(
            '//p[@class="_j_note_content _j_seqitem"]/text()'))
        self.log("update content, seq: {}, len: {}, has_more: {}".format(self.next_seq,len(self.content),self.has_more))

        # html = response.body.decode("unicode-escape")
        # content_list = re.compile(
        #     '[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\u4e00-\u9fa5]+').findall(html)
        # for item in content_list:
        #     self.content += item
