#!/usr/bin/env python

from funct import *
from vishtml import *

def htmlnav():
	print("""<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <a class="navbar-brand" href="#">Site Monitor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="sites.cgi">Sites <span class="sr-only"></span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="statuscheck.cgi">Status</a>
      </li>
	<li class="nav-item">
        <a class="nav-link" href="error.cgi">Logs</a>
      </li>
    </ul>
  </div>
</nav>""")

def showtable(urls):
	print("""<table class="table table-hover table-stripped text-white">
		<thread class="thread-dark">
		<tr>
			<th scope="col">URLS</th>
		</tr>
		</thread>
		<tbody>""")
	for row in urls:
		print("<tr>")
		print("<td>{0}</td>".format(row[0]))
		print("</tr>")
	print("</tbody></table>")

try:
	htmlHead()
	htmlnav()
	opencontainer()
	htmlform()
	db, cur = dbconnect()
	listurl = getdata()
	urls = selecturl(db,cur)
	inserturl(db, cur, listurl, urls)
	cur.close()
	showtable(urls)
	closecontainer()
	htmlEnd()
except:
	cgi.print_exception()
