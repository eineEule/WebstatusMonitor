#!/usr/bin/env python

import MySQLdb
import cgi


def getdata():
        formData = cgi.FieldStorage()
        listurl = formData.getvalue('listurl')
        return listurl

def dbconnect():
	db = MySQLdb.connect(host="HOST",
        	user="USERNAME",
        	passwd="PASSWORD",
        	db="DATABASE")

	cur = db.cursor()
	return db, cur

def selecturl(db, cur):
	cur.execute("select url from TABLE")
	urls = cur.fetchall()
	return urls

def inserturl(db, cur, listurl, urls):
        if listurl == None:
		pass
        else:
                cur.execute("insert ignore into TABLE(COLUMN) values('{0}')".format(listurl))
                db.commit()

def selecttable(db, cur):
        cur.execute("select * from TABLE")
        urltable = cur.fetchall()
        return urltable

def readfile():
        f = open('error.log','r')
        contents = f.read()
        print(contents)
        f.close()
        return contents

