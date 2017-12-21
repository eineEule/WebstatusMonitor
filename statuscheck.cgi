#!/usr/bin/env python

from vishtml import *
from funct import *

def htmlnav():
	print("""<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <a class="navbar-brand" href="#">Site Monitor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" href="sites.cgi">Sites <span class="sr-only"></span></a>
      </li>
      <li class="nav-item active">
	<a class="nav-link" href="statuscheck.cgi">Status</a>
</li>
      <li class="nav-item">
        <a class="nav-link" href="error.cgi">Logs</a>
      </li>
      </li>
    </ul>
  </div>
</nav>""")

def showtable(urltable):
	print("""<table class="table table-hover table-stripped text-white">
		<thread class="thread-dark">
		<tr>
			<th scope="col">URLS</th>
			<th scope="col">STATUS</th>
			<th scope="col">TIME</th>
		</tr>
		</thread>
		<tbody>""")
	for row in urltable:
		print("<tr>")
		print("<td>{0}</td>".format(row[1]))
		print("<td>{0}</td>".format(row[2]))
		print("<td>{0}</td>".format(row[3]))
		print("</tr>")
	print("</tbody></table>")

try:
	htmlHead()
	htmlnav()
	openstatcon()
	db, cur = dbconnect()
	urltable = selecttable(db, cur)
	cur.close()
	showtable(urltable)
	closecontainer()
	htmlEnd()
except:
	cgi.print_exception()
