import sqlite3 as lite

############# SET UP ################
## REFER TO SQL FILE NAME TO MAKE INIT EDITS ##

#Datbase Name
DB_NAME = "tempDB"

#SQL file with DB setup and Initialized Data
SQL_FILE_NAME = "Pothole_Table_Schema.sql"	

#####################################

Pothole_Table_Schema = ""
with open (SQL_FILE_NAME, 'r') as SchemaFile:
	Pothole_Table_Schema = SchemaFile.read().replace('\n','')

#DB Connection
conn = lite.connect(DB_NAME)
curs = conn.cursor()

#Create Tables
lite.complete_statement(Pothole_Table_Schema)
curs.executescript(Pothole_Table_Schema)
print( DB_NAME + " has been created/cleared.")

#Close Database
curs.close()
conn.close()