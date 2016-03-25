# -*- coding: utf-8 -*-

# Scrapy settings for Lianjia project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Lianjia'

SPIDER_MODULES = ['Lianjia.spiders']
NEWSPIDER_MODULE = 'Lianjia.spiders'

DOWNLOAD_DELAY = 10

ITEM_PIPELINES={
    # 'Lianjia.pipelines.pipelines.LianjiaJsonPipeline':300,
    'Lianjia.pipelines.MongoPipelines.LianjiaMongoPipeline':800
}


MONGODB_SERVER = 'guaxiaoda.cn'
MONGODB_PORT = 27017
MONGODB_DB = 'housedb'
MONGODB_COLLECTION = 'houseinfo'

# start mysql conf
# MYSQL_HOST = 'guanxiaoda.cn'
# MYSQL_DNAME = 'house'
# MYSQL_USER = 'gxd'
# MYSQL_PASSWD = 's327gxd'
# end mysql conf

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Lianjia (+http://www.yourdomain.com)'
