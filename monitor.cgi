# WebstatusMonitor
#!/usr/bin/env python

import cgi
import MySQLdb

def htmlHead():
	print("""Content-type: text/html\n\n
		<!DOCTYPE html>
		<html>
		<head>
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
			<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
			<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>

			<title>Test</title>
		</head>
		<body class="bg-dark">""")

def htmlEnd():
	print("""</body>
		</html>""")
def htmlnav():
	print("""<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <a class="navbar-brand" href="#">Site Monitor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only"></span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Sites</a>
      </li>
    </ul>
  </div>
</nav>""")

def opencontainer():
	print("""<div class="container">""")

def closecontainer():
	print("</div>")

def htmlform():
	print("""</br><form class="text-white" method="post" action="test.cgi">
                        <input class="form-control form-control-lg" type="text" name="listurl" placeholder="Enter URL to Monitor" autofocus></br>
                </form>""")

#def css():
#	print("""<style>body{background-color:#2E2E2E;}</style>""")

def getdata():
        formData = cgi.FieldStorage()
        listurl = formData.getvalue('listurl')
        return listurl

def inserturl(db, cur, listurl):
	if listurl == None:
		pass
	else:
		cur.execute("insert into urllist(url) values('{0}')".format(listurl))
       		db.commit()

def dbconnect():
	db = MySQLdb.connect(host="localhost",
        	user="USERNAME_HERE",
        	passwd="PASSWORD_HERE",
        	db="httptable")

	cur = db.cursor()
	return db, cur

def selecttable(db, cur):
	cur.execute("select * from urllist")
	urls = cur.fetchall()
	return urls

def showtable(urls):
	print("""<table class="table table-hover table-stripped text-white">
		<thread class="thread-dark">
		<tr>
			<th scope="col">ID</th>
			<th scope="col">URLS</th>
		</tr>
		</thread>
		<tbody>""")
	for row in urls:
		print("<tr>")
		print("""<th scope="col">{0}</th>""".format(row[0]))
		print("<td>{0}</td>".format(row[1]))
		print("</tr>")
	print("</tbody></table>")

try:
	htmlHead()
#	css()
	htmlnav()
	opencontainer()
	htmlform()
	db, cur = dbconnect()
	listurl = getdata()
	inserturl(db, cur, listurl)
	urls = selecttable(db,cur)
	cur.close()
	showtable(urls)
	closecontainer()
	htmlEnd()
except:
	cgi.print_exception()
