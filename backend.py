#!/usr/bin/env python

import MySQLdb, urllib2, datetime, logging

logging.basicConfig(filename="error.log", level=logging.ERROR, format="%(asctime)s:%(levelname)s:%(message)s")

def dbconnect():
	db = MySQLdb.connect(host="HOST",
        	user="USERNAME",
        	passwd="PASSWORD",
        	db="DATABASE")

	cur = db.cursor()
	return db, cur

def selecturl(db, cur):
	cur.execute("select * from TABLE")
	urls = cur.fetchall()
	return urls

def t():
	ti = datetime.datetime.now()
	return ti

def status_check(db, cur, urls, ti):
	try:
		for item in urls:
			req = urllib2.urlopen('{0}'.format(item[1]))
			cod = req.getcode()
			print cod
			print ti

			if cod == 200:
				cur.execute("update TABLE set status='UP' where COLUMN='{0}'".format(item[1]))
				cur.execute("update TABLE set time='{}' where COLUMN='{}'".format(ti, item[1]))
				db.commit()
			else:
				cur.execute("update TABLE set status='DOWN' where COLUMN='{0}'".format(item[1]))
				db.commit()
	except Exception as e:
		cur.execute("update TABLE set status='NOT AVIALABLE' where COLUMN='{0}'".format(item[1]))
                cur.execute("update TABLE set time='{}' where COLUMN='{}'".format(ti, item[1]))
		db.commit()
try:
	db, cur = dbconnect()
	urls = selecturl(db,cur)
	ti = t()
	status_check(db, cur, urls, ti)
	cur.close()
except Exception as e:
	logging.error(e)
