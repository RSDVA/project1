#!/usr/bin/env python3
# 
# A web service accessing database news to answer 3 questions

from flask import Flask, request, redirect, url_for

from newsdb import get_qone, get_qtwo, get_qthree

app = Flask(__name__)

# HTML template for the question page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Project 1:  Questions</title>
  </head>
  <body>
    <h1>Questions</h1>
    <form action="http://localhost:8000/question1">
      <div><button id="q1" type="submit">Pull Q1</button></div>
    </form><br>
    <form action="http://localhost:8000/question2">
      <div><button id="q2" type="submit">Pull Q2</button></div>
    </form><br>
    <form action="http://localhost:8000/question3">
      <div><button id="q3" type="submit">Pull Q3</button></div>
    </form><br>
    <!-- question results will go here -->
    %s
  </body>
</html>
'''

# HTML template for each question
qonetwo = '''\
    <div>%s - %s views</div>
'''

qthree = '''\
    <div>%s - %s%% errors</div>
'''

@app.route('/', methods=['GET'])
def main():
  '''Main page for questions'''

  return HTML_WRAP % ""

@app.route('/question1', methods=['GET'])
def q_1():
  '''Question 1 results'''
  q12 = "".join(qonetwo % (articles, views) for articles, views in get_qone())
  html = HTML_WRAP % q12
  return html

@app.route('/question2', methods=['GET'])
def q_2():
  '''Question 1 results'''
  q12 = "".join(qonetwo % (author, views) for author, views in get_qtwo())
  html = HTML_WRAP % q12
  return html

@app.route('/question3', methods=['GET'])
def q_3():
  '''Question 3 results'''
  q3 = "".join(qthree % (date, errors) for date, errors in get_qthree())
  html = HTML_WRAP % q3
  return html

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
