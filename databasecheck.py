import mysql.connector
con = mysql.connector.connect(
    username ="....",
    password ="",
    host = "localhost",
    port = '3306',
    database ="llfgllgf"
)
cursor = con.cursor()

word =input("Enter Search Word :")
query = cursor.execute("SELECT * FROM dictionary WHERE exp= '%s'" % word)
result = cursor.fetchall()
print(result)
for items in result:
    print(items[1], "=", items[2])

#
#

cursor = con.cursor()
indata = input("insert  Exp data:")
desdata = input("insert  Des data:")
query =cursor.execute("INSERT INTO dictionary (exp,des)VALUES (%s,%s)", (indata, desdata))
con.commit()
