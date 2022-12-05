import datetime

import mysql.connector
from datetime import time

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
        print("등록할 멤버의 정보를 입력해주세요 : (멤버넘버, 이름, 아이디, 비밀번호, 주소, 전화번호, 주민등록번호, 이메일, 등록한 스포츠센터)")
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
        sql = "INSERT INTO teacher (teacherNumber, teacherName, teacherId, teacherPassword, teacherAddress, teacherPhone, teacherRrn, teacherEmail, centerTitle) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        print("등록할 강사의 정보를 입력해주세요 : (강사넘버, 이름, 아이디, 비밀번호, 주소, 전화번호, 주민등록번호, 이메일, 등록한 스포츠센터)")
        teacherNumber = int(input())
        teacherName = str(input())
        teacherId = str(input())
        teacherPassword = str(input())
        teacherAddress = str(input())
        teacherPhone = str(input())
        teacherRrn = str(input())
        teacherEmail = str(input())
        centerTitle = str(input())
        cur.execute(sql, (teacherNumber, teacherName, teacherId, teacherPassword, teacherAddress, teacherPhone, teacherRrn, teacherEmail, centerTitle))
#lecture
    elif menu == 4:
        sql = "INSERT INTO lecture (lectureCenter, lectureNumber,lectureName, lectureTotal, lectureLocation,  lectureDay, startTime, endTime, lecturePay, lectureteacherNumber) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        print("등록할 강의 정보를 입력해주세요 : (강의센터, 강의번호, 강의이름, 강의정원수, 강의장소,강의요일, 강의시작시간,강의종료시간, 강의요금, 강의강사번호)")
        lectureCenter = str(input())
        lectureNumber = int(input())
        lectureName = str(input())
        lectureTotal = str(input())
        lectureLocation = str(input())
        lectureDay = str(input())
        a1 = int(input())
        a2 = int(input())
        a3 = int(input())
        startTime = datetime.time(a1, a2, a3)
        b1 = int(input())
        b2 = int(input())
        b3 = int(input())
        endTime = datetime.time(b1, b2, b3)
        lecturePay = int(input())
        lectureteacherNumber = int(input())
        cur.execute(sql, (lectureCenter, lectureNumber, lectureName, lectureTotal, lectureLocation, lectureDay, startTime, endTime, lecturePay, lectureteacherNumber))
#car
    elif menu == 5:
        sql = "INSERT INTO car (carNumber, carType, carMember, carTeacher) VALUES (%s, %s, %s, %s)"
        print("등록할 자동차 정보를 입력해주세요 : (자동차번호, 차종, 자동차소유 회원번호, 자동차소유 강사번호 )")
        carNumber = str(input())
        carType = str(input())
        carMember = int(input())
        carTeacher = int(input())
        cur.execute(sql, (carNumber, carType, carMember, carTeacher))


    elif menu == 6:
        sql = "DELETE FROM center WHERE title= %s"
        print("삭제할 스포츠센터 이름을 입력해주세요: ")
        deleteCenter = str(input())
        cur.execute(sql, (deleteCenter,))
        minsungdb.commit()

    elif menu == 7:
        sql = "DELETE FROM member WHERE centerTitle =%s AND memberNumber =%s"
        print("삭제할 회원이 다니는 스포츠센터 이름과 회원 번호를 입력해주세요: ")
        deleteCenter = str(input())
        deleteMember = str(input())
        cur.execute(sql, (deleteCenter, deleteMember,))
        minsungdb.commit()

    elif menu == 8:
        sql = "DELETE FROM teacher WHERE centerTitle =%s AND teacherNumber =%s"
        print("삭제할 강사가 다니는 스포츠센터 이름과 강사 번호를 입력해주세요: ")
        deleteCenter = str(input())
        deleteTeacher = str(input())
        cur.execute(sql, (deleteCenter, deleteTeacher,))
        minsungdb.commit()

    elif menu == 9:
        sql = "DELETE FROM lecture WHERE lectureteacherNumber =%s AND lectureNumber = %s"
        print("삭제할 강사가 다니는 스포츠센터 이름과 강사 번호와 강의번호를 입력해주세요: ")
        deleteCenter = str(input())
        deleteTeacher = str(input())
        deleteLecture = str(input())
        cur.execute(sql, (deleteTeacher, deleteLecture,))
        minsungdb.commit()

    elif menu == 10:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    elif menu == 11:
        sql = "SELECT * FROM center WHERE title = %s"
        print("정보를 원하는 센터 이름을 입력해주세요: ")
        searchCenter = str(input())
        cur.execute(sql, (searchCenter,))
        result = cur.fetchall()
        for data in result:
            print(data)

    elif menu == 12:
        sql = "SELECT * FROM member WHERE memberName = %s"
        print("검색을 원하는 회원 이름을 입력해주세요: ")
        searchMember = str(input())
        cur.execute(sql, (searchMember,))
        result = cur.fetchall()
        for data in result:
            print(data)

    elif menu == 13:
        sql = "SELECT * FROM teacher WHERE teacherName = %s"
        print("검색을 원하는 강사 이름을 입력해주세요: ")
        searchTeacher = str(input())
        cur.execute(sql, (searchTeacher,))
        result = cur.fetchall()
        for data in result:
            print(data)

    elif menu == 14:
        sql = "SELECT * FROM lecture WHERE lectureName = %s"
        print("검색을 원하는 강의 이름을 입력해주세요: ")
        lectureName = str(input())
        cur.execute(sql, (lectureName,))
        result = cur.fetchall()
        for data in result:
            print(data)

    elif menu == 15:
        sql = "SELECT * FROM Book"
        cur.execute(sql)
        result = cur.fetchall()
        for row_data in result:
            print(row_data)

    else:
        break
    minsungdb.commit()