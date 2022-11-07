import mysql.connector


minsungdb = mysql.connector.connect(
        host="192.168.56.101",
        port='4567',
        user="minsung",
        password="1234",
        database="madang")

cur = minsungdb.cursor()

while 1:
    print("Please 1 to Insert Book")
    print("Please 2 to Delete Book")
    print("Please 3 to Search Book")
    print("Please 4 to Show Book")
    print("Please 5 to Finish")
    menu = int(input())
    if menu == 1:
        sql = "INSERT INTO Book (bookid, bookname, publisher, price) VALUES(%s, %s, %s, %s)"
        print("삽입할 책의 정보를 다음과 같은 순서로 입력해주세요: (bookid,bookname,publisher,price)")
        bookid = int(input())
        bookname = str(input())
        publisher = str(input())
        price = int(input())
        cur.execute(sql, (bookid, bookname, publisher, price))

    elif menu == 2:
        sql = "DELETE FROM Book WHERE bookname = %s"
        print("삭제할 책의 이름을 입력해주세요: ")
        deleteName = str(input())
        cur.execute(sql, (deleteName,))
        minsungdb.commit()

    elif menu == 3:
        sql = "SELECT * FROM Book WHERE bookname = %s"
        print("검색할 책의 이름을 입력해주세요: ")
        searchBook = str(input())
        cur.execute(sql, (searchBook,))
        result = cur.fetchall()
        for data in result:
            print(data)

    elif menu == 4:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    else:
        break
    minsungdb.commit()