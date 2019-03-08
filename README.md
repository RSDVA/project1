# Project 1: Logs Analysis

This project will demonstrate being able to access a database and run queries on it to answer 3 questions.  It is a web page that will have 3 buttons which correspond to each question.  Once you press on the button it will send a request to the database for the results.  The results will show up under the buttons.  Please see sample results below for each question.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You will need psycopg2, and flask installed

## Installing

Run pip install psycopg2, and pip install flask

1.) Then download the news data base and unzip it to the same directory as you cloned this repo  https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

2.) run this command psql -d news -f newsdata.sql

## Running the Project

1.) Open a command prompt of your choice (I used Git Bash) and cd into the directory where the project.py and newsdb.py are located

2.) Then run python ./project1.py

3.) Now open up your favorite browser (I used Chrome) and go to http://localhost:8000

4.) You will see 3 Buttons each one corresponds to each question for this project.  Click on it and it will call a query on the data base and show the results both in the web page below the buttons and in the Git Bash console.

## Question Results
### Q1:
	Candidate is jerk, alleges rival - 338647 views
	Bears love berries, alleges bear - 253801 views
	Bad things gone, say good people - 170098 views

### Q2:
    Ursula La Multa - 507594 views
    Rudolf von Treppenwitz - 423457 views
    Anonymous Contributor - 170098 views
    Markoff Chaney - 84557 views

### Q3:
    2016-07-17 - 2.26% errors


## Author(s)

Alfredo Garcia
