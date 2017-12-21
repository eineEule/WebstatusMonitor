#!/usr/bin/env python

import cgi

def htmlHead():
	print("""Content-type: text/html\n\n
		<!DOCTYPE html>
		<html>
		<head>
			<meta name="viewport" content="initial-scale=1, maximum-scale=5">
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
			<title>Site Monitor</title>
		</head>
		<body class="bg-dark">""")

def htmlEnd():
	print("""</body>
		</html>""")

def opencontainer():
	print("""</br><div class="container"><font color="white"><h1>Site List</h1></font>""")

def closecontainer():
	print("</div>")

def htmlform():
	print("""</br><form class="text-white" method="post" action="sites.cgi">
                        <input class="form-control form-control-lg" type="text" name="listurl" placeholder="(i.e. https://www.google.com)" autocomplete="off" autofocus></br>
                </form>""")

def errHead():
        print("""Content-type: text/html\n\n
                <!DOCTYPE html>
                <html>
                <head>
                        <meta name="viewport" content="initial-scale=1, maximum-scale=5">
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
               <style> .container{ background-color: white; } </style>
         <title>Site Monitor</title>
                </head>
                <body class="bg-dark">""")

def openerrcon():
        print("""</br><div class="container"><h1>Error Log</h1>""")

def openstatcon():
        print("""</br><div class="container"><font color="white"><h1>Site Status</h1></font>""")

def openconconf():
        print("""</br><div class="container">""")
