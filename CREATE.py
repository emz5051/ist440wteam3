#!/usr/bin/python
#! -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team3', 'TestDB');

with con:

	cur = con.cursor()
	cur.execute("SET sql_notes = 0; ")
	cur.execute("DROP TABLE IF EXISTS Test")
	cur.execute("CREATE TABLE IF NOT EXISTS Test(Id INT PRIMARY KEY AUTO_INCREMENT, FirstName VARCHAR(25), LastName VARCHAR(25), Email VARCHAR (50), FlightNo INT)")
	cur.execute("INSERT INTO Test(FirstName, LastName, Email, FlightNo) VALUES('Jim', 'Bo','JIMBO@email.com', '2829922')")
	cur.execute("INSERT INTO Test(FirstName, LastName, Email, FlightNo) VALUES('Kevin', 'Wilkinison', 'KevinWilkinson@email.com', '3773827')")
	cur.execute("INSERT INTO Test(FirstName, LastName, Email, FlightNo) VALUES('Osei', 'Seraphin','OseiSeraphin@email.com', '8171882')")
	cur.execute("INSERT INTO Test(FirstName, LastName, Email, FlightNo) VALUES('Nicholas', 'Alexander', 'NicholasAlexander@email.com', '2625554')")
	cur.execute("INSERT INTO Test(FirstName, LastName, Email, FlightNo) VALUES('Lejaney', 'Blue', 'LejaneyBlue@email.com', '8899884')")
	cur.execute("INSERT INTO Test(FirstName, LastName, Email, FlightNo) VALUES('Brandon', 'Crandall', 'BrandonCrandall@email.com', '8833736')")
	cur.execute("INSERT INTO Test(FirstName, LastName, Email, FlightNo) VALUES('Nigel', 'Phillips', 'NigelPhillips@email.com', '6657588')")
	cur.execute("INSERT INTO Test(FirstName, LastName, Email, FlightNo) VALUES('Bob', 'Pizza', 'BobPizza@email.com', '3938722')")
	cur.execute("INSERT INTO Test(FirstName, LastName, Email, FlightNo) VALUES('John', 'Doe', 'JohnDoe@email.com', '3345223')")
	cur.execute("INSERT INTO Test(FirstName, LastName, Email, FlightNo) VALUES('Lisa', 'Ray', 'LisaRay@email.com', '7677584')")
