import mysql.connector


try:
    minsungdb = mysql.connector.connect(
        host="192.168.56.101",
        port='4567',
        user="minsung",
        password="1234",
        database="madang")

    cur = minsungdb.cursor()

    cur.execute("SELECT bookname,price FROM Book")

    result = cur.fetchall()

    for x in result:
        print(x)

except mysql.connector.Error as e:
    print(e)
