# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
# from scrapy.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
import requests
import os
import codecs
import ndss_spider.settings as settings

ABS_PATH = settings.ABS_PATH

class NdssSpiderPipeline(object):
    def process_item(self, item, spider):
        # return item
        # self.item = item
        print("[进入Pipeline] ", item)
        # yield scrapy.Request(item['pdf'])

        # 下载pdf
        # 创建目录pdf
        pdfs_path = settings.ABS_PATH + "\\pdfs"
        if os.path.exists(pdfs_path) == False:
            os.mkdir(pdfs_path)
        filename = item['pdf'].split('/')[-1]
        print("[下载] pdf： ", filename)        
        filepath = pdfs_path + "\\" + filename
        if os.path.exists(filepath) == False:
            res = requests.get(item['pdf'])
            with open(filepath, "wb") as f:
                f.write(res.content)

        # 下载slide
        # 创建目录slides
        slides_path = settings.ABS_PATH + "\\slides"
        if os.path.exists(slides_path) == False:   
            os.mkdir(slides_path)
        if item['slide'] != '':
            filename = item['slide'].split('/')[-1]
            print("[下载] slide: ", filename)        
            filepath = slides_path + "\\" + filename
            if os.path.isfile(filepath) == False:
                res = requests.get(item['slide'])
                with open(filepath, "wb") as f:
                    f.write(res.content)

        # 下载video
        # 创建目录videos
        videos_path = settings.ABS_PATH + "\\videos"
        if os.path.exists(videos_path) == False:
            os.mkdir(videos_path)
        if item['video'] != '':
            # print("++++PDF PDF", item['pdf'])
            # filename = item['pdf'].split('/')[-1].split('_')
            # filename = '_'.join(filename[:-1]) + "_video.mp4"
            filename = item['pdf'].split('/')[-1].split(".")[0] + "_video.mp4"
            print("[下载] video: ", filename)        
            # 设置videos下载目录
            filepath = videos_path   
            lastfile = filepath + "\\" + filename
            if os.path.isfile(lastfile):
                print("文件已经存在!")
            else:
                print("文件不存在!")
                # 使用you-get工具下载视频
                command = 'you-get "{0}" -o {1} -O {2} {3}'.format(item['video'], filepath, filename, "--debug")
                print(command)
                os.system(command)
        return item


