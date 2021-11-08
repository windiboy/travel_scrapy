# Scrapy settings for wang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
COOKIES_DETAIL = "uva=s%3A108%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1585970106%3Bs%3A10%3A%22last_refer%22%3Bs%3A40%3A%22http%3A%2F%2Fwww.mafengwo.cn%2Fpoi%2F33596540.html%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __jsluid_s=3bfea5342f3732fc3341fe21fb6358a1; PHPSESSID=31et7dqa914vhrtj8ljocm27t1; mfw_uuid=61404906-c3b9-7269-a688-a904d6ae61df; __mfwc=direct; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1631602957; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1631602951%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=61404906-c3b9-7269-a688-a904d6ae61df; UM_distinctid=17be31d5c9281-0518e07d7c3fb3-b383f66-190140-17be31d5c9356c; __omc_chl=; __omc_r=; __jsluid_h=4faec5defa945088c5d2036952f19c5a; __jsl_clearance_s=1632228608.74|0|S5qwD0BurpKr8xSUmtfbnVdlP2w%3D; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222021-09-21+20%3A50%3A12%22%3B%7D; __mfwlv=1632228618; __mfwvn=13; bottom_ad_status=0; CNZZDATA30065558=cnzz_eid%3D1210821945-1631602778-https%253A%252F%252Fwww.mafengwo.cn%252F%26ntime%3D1632228027; __mfwb=bf6cc45b230b.1.direct; __mfwa=1631602956941.70885.20.1632228618464.1632230706404; __mfwlt=1632230706; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1632230706"
COOKIES = "uva=s%3A108%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1585970106%3Bs%3A10%3A%22last_refer%22%3Bs%3A40%3A%22http%3A%2F%2Fwww.mafengwo.cn%2Fpoi%2F33596540.html%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __jsluid_s=3bfea5342f3732fc3341fe21fb6358a1; PHPSESSID=31et7dqa914vhrtj8ljocm27t1; mfw_uuid=61404906-c3b9-7269-a688-a904d6ae61df; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222021-09-14+15%3A02%3A30%22%3B%7D; __mfwc=direct; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1631602957; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1631602951%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=61404906-c3b9-7269-a688-a904d6ae61df; UM_distinctid=17be31d5c9281-0518e07d7c3fb3-b383f66-190140-17be31d5c9356c; __omc_chl=; __omc_r=; __jsluid_h=4faec5defa945088c5d2036952f19c5a; bottom_ad_status=0; __mfwa=1631602956941.70885.7.1631696254485.1631702958928; __mfwlv=1631702958; __mfwvn=5; CNZZDATA30065558=cnzz_eid%3D1210821945-1631602778-https%253A%252F%252Fwww.mafengwo.cn%252F%26ntime%3D1631692748; __mfwb=ad2df73762ec.3.direct; __mfwlt=1631702995; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1631702996"
BOT_NAME = 'wang'
LOG_LEVEL = "WARNING" 
SPIDER_MODULES = ['wang.spiders']
NEWSPIDER_MODULE = 'wang.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
  'Referer': 'https://www.mafengwo.cn/poi/28124.html',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wang.middlewares.WangSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'wang.middlewares.WangDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'wang.pipelines.WangPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
