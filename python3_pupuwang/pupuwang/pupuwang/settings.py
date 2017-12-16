# -*- coding: utf-8 -*-

# Scrapy settings for pupuwang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pupuwang'

SPIDER_MODULES = ['pupuwang.spiders']
NEWSPIDER_MODULE = 'pupuwang.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pupuwang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 并发量
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Cookie" : "tq_source_page_url=https://www.baidu.com/link!url^3Dq3nz4Vq6GhvW1N84PUulLwkgYQQ-kOGU4EJg0iDZfaN8DIg9ABWrlcKNM1dFf1h9*wd^3D*eqid^3Dbc73b9af000452a0000000045a33b2b2; tq_current_visit_time=1513337534306; tq_current_source_page_url=https://www.baidu.com/link!url^3Dq3nz4Vq6GhvW1N84PUulLwkgYQQ-kOGU4EJg0iDZfaN8DIg9ABWrlcKNM1dFf1h9*wd^3D*eqid^3Dbc73b9af000452a0000000045a33b2b2; request_city=18e8f8a8-d780-4332-af4d-20ea1b622ec5; Hm_lvt_a2ba633c40a657eb8a72e6086d4cc8b7=1513337454,1513337535; Hm_lpvt_a2ba633c40a657eb8a72e6086d4cc8b7=1513351505",
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pupuwang.middlewares.PupuwangSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'pupuwang.middlewares.RandomUserAgent': 1,
   # 'pupuwang.middlewares.FreeRandomProxy': 2,
}
DOWNLOAD_TIMEOUT = 3
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'pupuwang.pipelines.PupuwangPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
