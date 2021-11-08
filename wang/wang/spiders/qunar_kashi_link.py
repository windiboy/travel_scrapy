import logging
import time
import scrapy
import json
import re
from lxml import etree
from wang.model.qunar_detail_link import QunarDetailLink
from wang.utils import *


class QunarKashiSpider(scrapy.Spider):
    name = "QunarKashiLink"
    cookies = []

    def __init__(self, id=None, *args, **kwargs):
        super(QunarKashiSpider, self).__init__(*args, **kwargs)
        if id == None:
            return
        self.id = id
        self.url = "https://travel.qunar.com/place/api/html/comments/poi/5740400?poiList=true&sortField=1&rank=0&pageSize=10&page={}".format(self.id)

        self.cookie = "JSESSIONID=A125A6A2BE659C6DC782A396FCABA2B5; QN1=00007080306c39fcc490c4ee; QN300=s%3Dbaidu; QN99=4931; QN205=s%3Dbaidu; QN277=s%3Dbaidu; csrfToken=YCosjyezN36X4gqA7IP4fd7K6ewdh7xj; _i=ueHd8ITZOCfX_Y2yUxBo0cPUPdXX; _vi=QPXvsR7ETRoOoTmBSi8c939f4gNWy4gfmO3uu8VKLREPCnkpSRYiVzIeuNppeKfc1d0OxXJXJprdTYqTwmEVzVinJqjgDMMEHBdO6iu5iYDypzjNwV6_E_CQPyl7REfy7oH3ebMq8FRQ3OWGKMtKrCWmsh9U_EfmOvE_unaP8hhE; QN601=54b3747c3762c1c40b9ac39281b6baab; QN269=67D96690612011EAAEADFA163E72A92B; QN48=000070802f1039fcc490e586; QN163=0; QN667=B; fid=cdbfd3e0-e4ad-410e-a5a8-6ae432026c67; qunar-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false}; QN243=9; Hm_lvt_c56a2b5278263aa647778d304009eafc=1636373160; viewpoi=5740400; viewdist=299889-2; uld=1-299889-2-1636373182|1-297649-1-1636373172; Hm_lpvt_c56a2b5278263aa647778d304009eafc=1636373184; QN271=88c6b3ab-3e4a-44d1-9010-37045b673ece; QN267=02022521129eeb91023"

    def start_requests(self):
        self.cookies = {i.split("=")[0]: i.split("=")[1]
                        for i in self.cookie.split("; ")}
        self.log("start scrapy, url: {}".format(self.url))

        yield scrapy.Request(url=self.url, callback=self.parse, cookies=self.cookies)

    def parse(self, response):
        data = json.loads(response.body.decode()).get("data","")
        selector=etree.HTML(data)
        links = selector.xpath(
            '//a[@class="seeMore"]/@href')

        for item in links:
            res = {
                "name": "kashigucheng",
                "content": item,
            }
            self.log(res,logging.WARNING)
            try:
                QunarDetailLink.insert(res).execute()
            except Exception as e:
                self.log("Create Content err: {}".format(
                    e), level=logging.ERROR)
        self.log("Create Content success!")
