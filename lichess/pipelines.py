# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# pipelines.py
import pandas as pd
import re
from datetime import datetime as dt

date = dt.now().strftime("%Y%m%d_%H-%M-%S")

class LichessPipeline:
    def open_spider(self, spider):
        # Initialize the dataframe when the spider opens
        self.dataframe = pd.DataFrame(columns=['name', 'headline', 'languages', 'location', 'rating_fide', 'rating_bullet', 'rating_blitz', 'rating_rapid', 'rate'])

    def close_spider(self, spider):
        pattern = r'\b(GM|WGM|IM|WIM|FM|WFM|CM|WCM|NM|WNM)\b'
        self.dataframe["titles"] = [re.search(pattern, name).group(0) if re.search(pattern, name) else None for name in self.dataframe["name"]]
        # Clean the FIDE: <number> entries into just the FIDE numeric rating
        self.dataframe['rating_fide'] = pd.to_numeric(self.dataframe['rating_fide'].str.extract('(\d+)')[0], errors='coerce')
        # Handle empty strings and language array
        self.dataframe = self.dataframe.fillna("None")
        # When the spider closes, save the dataframe to a CSV file
        self.dataframe.to_csv(f'{date}_coaches_table.csv', index=False)

    def process_item(self, item, spider):
        # Add each item to the dataframe
        self.dataframe = pd.concat([self.dataframe, pd.DataFrame([item])], ignore_index=True)
        return item

