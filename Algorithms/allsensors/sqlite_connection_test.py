import sqlite3 as lite

########### SET UP ############

#Database Name
DB_NAME = "tempDB"

SQL_FILE_NAME = "add_records.sql"
#idea is to have allsensors_multithread_v2.py to output .sql file
#OR have a connection/add function inside using curs.execute(..INSERT..) like in add_records.sql

################################

add_records = "";
with open (SQL_FILE_NAME, 'r') as ExecutionFile:
	add_records = ExecutionFile.read().replace('\n','')

#DB Connection
conn = lite.connect(DB_NAME)
curs = conn.cursor()
print("Connection to " + DB_NAME + " successful!\n")

#Execute SQL File
lite.complete_statement(add_records)
curs.executescript(add_records)
conn.commit()

#Print Resulting Table
curs.execute("SELECT * FROM sensors;")
print(curs.fetchall())
print("\nTable update successful.")

#Close Database
curs.close()
conn.close()