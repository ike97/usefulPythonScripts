import sqlite3

conn = sqlite3.connect("Conference.db")

conn.execute("CREATE TEMPORARY TABLE Pastors (id INT, name TEXT);")
conn.execute("INSERT INTO Pastors (id, name) VALUES(1, 'Ama');")
conn.execute("INSERT INTO Pastors (id, name) VALUES(2, 'Kaudi');")
conn.execute("INSERT INTO Pastors (id, name) VALUES(3, 'Vivian');")

conn.commit

cursor = conn.execute('SELECT * FROM Pastors;')
    
for row in cursor:
    print ("id = #", row[0])
    print ("name = ", row[1])
    
conn.close