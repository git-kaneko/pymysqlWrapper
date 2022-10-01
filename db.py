#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql.cursors
import pymysql

class DB:

    def __init__(self, host: str, user: str, dbName: str, password: str, cherset: str = 'utf8', cursorClass: str = "DictCursor"):
        self.host: str = host
        self.user: str = user
        self.dbName: str = dbName
        self.password: str = password
        self.cherset: str = cherset
        self.cursorClass: str = cursorClass
        self.connection = self.connect()

    def __del__(self):
        self.connection.close()
    
    def connect(self):
        return pymysql.connect(
            host = self.host,
            user = self.user,
            db = self.dbName,
            password = self.password,
            charset = self.cherset,
            cursorclass = pymysql.cursors.DictCursor
        )