import mysql.connector


minsungdb = mysql.connector.connect(
        host="192.168.56.101",
        port='4567',
        user="minsung",
        password="1234",
        database="sportscenter")

cur = minsungdb.cursor()

while 1:
    print("1. Enroll sports center")
    print("2. Enroll member")
    print("3. Enroll teacher")
    print("4. Enroll lecture")
    print("5. Enroll car")
    print("6. Delete sports center")
    print("7. Delete member")
    print("8. Delete teacher")
    print("9. Delete lecture")
    print("10. Delete car")
    print("11. Search sports center")
    print("12. Search member")
    print("13. Search teacher")
    print("14. Search lecture")
    print("15. Search car")
    menu = int(input())

    if menu == 1:
        sql = "INSERT INTO center (title, owner, phone, address) VALUES(%s, %s, %s, %s)"
        print("등록할 스포츠센터 정보를 입력해주세요 : (센터이름, 센터장, 센터번호, 센터주소)")
        title = str(input())
        owner = str(input())
        phone = str(input())
        address = str(input())
        cur.execute(sql, (title, owner, phone, address))


    elif menu == 2:
        sql = "INSERT INTO member (memberNumber,memberName,memberId, memberPassword,memberAddress,memberPhone, memberRrn,memberEmail,centerTitle) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)"
        print("등록할 멤버의 이름을 입력해주세요 : (멤버넘버, 이름, 아이디, 비밀번호, 주소, 전화번호, 주민등록번호, 이메일, 등록한 스포츠센터)")
        memberNumber = int(input())
        memberName = str(input())
        memberId = str(input())
        memberPassword = str(input())
        memberAddress = str(input())
        memberPhone = str(input())
        memberRrn = str(input())
        memberEmail = str(input())
        centerTitle = str(input())
        cur.execute(sql, (memberNumber,memberName,memberId, memberPassword,memberAddress,memberPhone, memberRrn,memberEmail,centerTitle))

    elif menu == 3:
        sql = "INSERT INTO teacher (teacherNumber, teacherName ) VALUES ()"
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

    elif menu == 5:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    elif menu == 6:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    elif menu == 7:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    elif menu == 8:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    elif menu == 9:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    elif menu == 10:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    elif menu == 11:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    elif menu == 12:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    elif menu == 13:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    elif menu == 14:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    elif menu == 15:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    else:
        break
    minsungdb.commit()