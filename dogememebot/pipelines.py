# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import cloudinary.uploader
import os
from scrapy.utils.project import get_project_settings
import csv
import pandas as pd

class DogememebotPipeline:

    settings = get_project_settings()
    def __init__(self):
        self.file_name = self.settings.get('FILE_NAME')
        cloudinary.config(
            cloud_name="shivam1519",
            api_key="854775435856326",
            api_secret="HvYInSsrqgYDlL0t8ILlS2H-mqk"
        )

    def open_spider(self, spider):
        self.file = open(self.file_name, mode='w+', encoding='utf-8', errors='ignore')
        fieldnames = self.settings.get('FEED_EXPORT_FIELDS')
        self.writer = csv.DictWriter(self.file, fieldnames=fieldnames)
        self.writer.writeheader()

    def close_spider(self, spider):
        self.file.close()
        csv_data = pd.read_csv(self.file_name)
        csv_data.sort_values(['time_posted'], axis=0, ascending=[False], inplace=True)
        with open(self.file_name, mode='r+', encoding='utf-8', errors='ignore') as f:
            cloudinary.uploader.upload(f.name, resource_type='raw', use_filename=True,
                                       unique_filename=False)
            f.close()
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
                                    
    def process_item(self, item, spider):
        row_to_add = {
            'time_posted': item['time_posted'],
            'image_url': item['image_url'],
            'shortcode': item['shortcode'],
            'hashtags': item['hashtags'],
            'username': item['username'],
            'id': item['id']
        }
        self.writer.writerow(item)
        return item 