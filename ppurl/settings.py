# -*- coding: utf-8 -*-

# Scrapy settings for ppurl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ppurl'

SPIDER_MODULES = ['ppurl.spiders']
NEWSPIDER_MODULE = 'ppurl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ppurl (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
    'ppurl.pipelines.PpurlPipeline': 300
}