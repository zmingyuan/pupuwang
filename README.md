# pupuwang
铺铺旺网站数据爬取

项目实现：
    CrawlSpider
    “找店选址”栏详情页匹配规则：details/\d+
    其他包含详情页链接（列表页）：all
    
字段：
    求租标题：title
    求租链接：url
    求租行业：industry
    发布时间：pubtime
    面积大小：size
    期望租金：rent
    详情描述：describe
    
反反爬：
    1、设置随机useragent
    2、设置代理IP
    
    后期可继续实现的反反爬虫：
        采用分布式
        模拟JavaScript
