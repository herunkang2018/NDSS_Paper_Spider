# NDSS_Paper_Spider
This is a Spider for crawling NDSS2017 papers and speech slides &amp; videos based on Python3, Scrapy and open source video downloader you-get.

To using it, first you should confirm you have already installed latest verison of scrapy and you-get, by simply using pip3:
```
pip3 install Scrapy you-get
```

Secondly, comfirm you can get access to youtube.

Then, clone this project and run the scrapy spider:
```
git clone git@github.com:hackeryard/NDSS_Paper_Spider.git
cd NDSS_Paper_Spider
scrapy crawl ndss_paper_spider
```
The default folder to store downloaded file is configured in settings.py
```
ABS_PATH = E:\\NDSS2017 #set what you like
```

Any question you have, feel free to open a issue.