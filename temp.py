import sqlite3

conn = sqlite3.connect("Customers.db")

conn.execute('''CREATE TEMPORARY TABLE Cus(id INT AUTO_INCREMENT, name TEXT);
             ''')

conn.commit;

conn.execute("INSERT INTO Cus (id, name) VALUES(1, 'Kwame')")
conn.execute("INSERT INTO Cus (id, name) VALUES(2, 'Kwadjo')")
conn.execute("INSERT INTO Cus (id, name) VALUES(3, 'Kwasi')")

conn.commit;

cursor = conn.execute("SELECT * FROM Cus")

for row in cursor:
    print ("id = #", row[0])
    print ("name =", row[1])
    
    