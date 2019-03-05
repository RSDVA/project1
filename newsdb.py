# Database code for results of questions for project 1
#
#

import psycopg2

DBNEWS = "news"

def get_qone():
  """Returns the results of question 1 from the 'database'"""
  db = psycopg2.connect(database=DBNEWS)
  c = db.cursor()
  c.execute("""
SELECT Split_part(l.path, '/', 3), Count(*) AS num FROM log l INNER JOIN ( 
SELECT art.slug FROM articles AS art GROUP BY art.slug) a ON l.path LIKE '%' 
|| a.slug GROUP BY l.path ORDER BY num DESC LIMIT 3
  """)
  qone = c.fetchall()
  db.close()
  return qone

def get_qtwo():
  """Returns the results of question 2 from the 'database'"""
  db = psycopg2.connect(database=DBNEWS)
  c = db.cursor()
  c.execute("""
SELECT ss.NAME, Sum(ss.num) AS total FROM (SELECT b.NAME, c.num FROM articles 
AS a LEFT JOIN authors AS b ON a.author = b.id LEFT JOIN (SELECT Split_part( 
l.path, '/', 3) AS path, Count(*) AS num FROM log l INNER JOIN (SELECT art.slug 
FROM articles AS art GROUP BY art.slug) a ON l.path LIKE '%' || a.slug 
GROUP BY l.path ORDER BY path) AS c ON a.slug LIKE '%' || c.path ORDER BY a.slug 
) AS ss GROUP BY ss.NAME ORDER BY total DESC
  """)
  qtwo = c.fetchall()
  db.close()
  return qtwo

def get_qthree():
  """Returns the results of question 3 from the 'database'"""
  db = psycopg2.connect(database=DBNEWS)
  c = db.cursor()
  c.execute("""
WITH perc_table AS (WITH t AS (SELECT Date(time) AS date, Count(*) FROM log 
GROUP BY date), e AS (SELECT Date(time) AS date, status, Count(*) FROM log 
GROUP BY date, status HAVING status LIKE '%404%') SELECT a.date, a.count 
AS total, b.count AS error, 100.0 * ( b.count * 1.0 / a.count * 1.0 ) AS 
percentage FROM t a INNER JOIN e b ON a.date = b.date) SELECT date, round(percentage,2) FROM 
perc_table WHERE percentage > 1
  """)
  qthree = c.fetchall()
  db.close()
  return qthree