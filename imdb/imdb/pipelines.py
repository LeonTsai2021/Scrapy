# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo
import sqlite3

class SQLitePipeline(object):    
    
    def open_spider(self,spider):
        self.collection=sqlite3.connect("imdb.db")
        self.c=self.collection.cursor()
        try:
            self.c.execute('''
                CREATE TABLE best_movie(
                    title TEXT,
                    year TEXT,
                    duration TEXT,
                    genre TEXT,
                    rating TEXT,
                    movie_url TEXT
                )                           
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass
        
    def close_spider(self,spider):
        self.connection.close()
        
    
    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO best_movie(title,year,duration,genre,rating,movie_url) VALUES(?,?,?,?,?,?)    
        ''', (
            item.get('title'),
            item.get('year'),
            item.get('duration'),
            item.get('genre'),
            item.get('rating'),
            item.get('movie_url'),
        ))
        self.collection.commit()
        return item
