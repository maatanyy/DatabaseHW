#### 2018038076 소프트웨어학과 3학년 노민성
#### 데이터베이스시스템 최종 프로젝트
#### 2022-12-05

import datetime

import mysql.connector
from datetime import time

################################### Network Connect

minsungdb = mysql.connector.connect(
        host="192.168.56.101",
        port='4567',
        user="minsung",
        password="1234",
        database="sportscenter")

cur = minsungdb.cursor()

################################### MENU

while 1:
    ###### 데이터 등록
    print("1. Enroll sports center")
    print("2. Enroll member")
    print("3. Enroll teacher")
    print("4. Enroll lecture")
    print("5. Enroll member car")
    print("6. Enroll teacher car")

    ###### 데이터 삭제
    print("7. Delete sports center")
    print("8. Delete member")
    print("9. Delete teacher")
    print("10. Delete lecture")
    print("11. Delete car")

    ###### 데이터 검색
    print("12. Search sports center")
    print("13. Search member")
    print("14. Search teacher")
    print("15. Search lecture")
    print("16. Search car")

    ###### 센터 정보 수정
    print("17. Update sports center owner")
    print("18. Update sports center phone")
    print("19. Update sports center address")

    ###### 멤버 정보 수정
    print("20. Update member id")
    print("21. Update member password")
    print("22. Update member phone")

    ###### 강사 정보 수정
    print("23. Update teacher id")
    print("24. Update teacher password")
    print("25. Update teacher phone")

    ###### 강의 정보 수정
    print("26. Update lecture Location")
    print("27. Update lecture Day")
    print("28. Update lecture Pay")


    ###### 차량 정보 수정
    print("29. Update car number")


    ###### 전체 조회
    print("30. SHOW all center people information")
    menu = int(input())

################################### INSERT

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
        sql = "INSERT INTO car (centerTitle, carNumber, carType, carMember) VALUES (%s, %s, %s, %s)"
        print("등록할 회원 자동차 정보를 입력해주세요 : (센터이름, 자동차번호, 차종, 자동차소유 회원번호 )")
        centerTitle = str(input())
        carNumber = str(input())
        carType = str(input())
        carMember = int(input())
        cur.execute(sql, (centerTitle, carNumber, carType, carMember))

    elif menu == 6:
        sql = "INSERT INTO car (centerTitle, carNumber, carType, carTeacher) VALUES (%s, %s, %s, %s)"
        print("등록할 강사 자동차 정보를 입력해주세요 : (센터이름, 자동차번호, 차종, 자동차소유 강사번호 )")
        centerTitle = str(input())
        carNumber = str(input())
        carType = str(input())
        carTeacher = int(input())
        cur.execute(sql, (centerTitle, carNumber, carType, carTeacher))

################################### Delete

    elif menu == 7:
        sql = "DELETE FROM center WHERE title= %s"
        print("삭제할 스포츠센터 이름을 입력해주세요: ")
        deleteCenter = str(input())
        cur.execute(sql, (deleteCenter,))
        minsungdb.commit()

    elif menu == 8:
        sql = "DELETE FROM member WHERE centerTitle =%s AND memberNumber =%s"
        print("삭제할 회원이 다니는 스포츠센터 이름과 회원 번호를 입력해주세요: ")
        deleteCenter = str(input())
        deleteMember = str(input())
        cur.execute(sql, (deleteCenter, deleteMember,))
        minsungdb.commit()

    elif menu == 9:
        sql = "DELETE FROM teacher WHERE centerTitle =%s AND teacherNumber =%s"
        print("삭제할 강사가 다니는 스포츠센터 이름과 강사 번호를 입력해주세요: ")
        deleteCenter = str(input())
        deleteTeacher = str(input())
        cur.execute(sql, (deleteCenter, deleteTeacher,))
        minsungdb.commit()

    elif menu == 10:
        sql = "DELETE FROM lecture WHERE lectureteacherNumber =%s AND lectureNumber = %s"
        print("삭제할 강사가 다니는 스포츠센터 이름과 강사 번호와 강의번호를 입력해주세요: ")
        deleteCenter = str(input())
        deleteTeacher = str(input())
        deleteLecture = str(input())
        cur.execute(sql, (deleteTeacher, deleteLecture,))
        minsungdb.commit()

    elif menu == 11:
        sql = "DELETE FROM car WHERE centerTitle = %s AND carNumber =%s"
        print("삭제할 자동차가 등록된 센터이름과 차랑 번호를 입력해주세요: ")
        deleteCenter = str(input())
        deleteNumber = str(input())
        cur.execute(sql, (deleteCenter, deleteNumber,))
        minsungdb.commit()

################################### Search

    elif menu == 12:
        sql = "SELECT * FROM center WHERE title = %s"
        print("정보를 원하는 센터 이름을 입력해주세요: ")
        searchCenter = str(input())
        cur.execute(sql, (searchCenter,))
        result = cur.fetchall()
        for data in result:
            print(data)

    elif menu == 13:
        sql = "SELECT * FROM member WHERE memberName = %s"
        print("검색을 원하는 회원 이름을 입력해주세요: ")
        searchMember = str(input())
        cur.execute(sql, (searchMember,))
        result = cur.fetchall()
        for data in result:
            print(data)

    elif menu == 14:
        sql = "SELECT * FROM teacher WHERE teacherName = %s"
        print("검색을 원하는 강사 이름을 입력해주세요: ")
        searchTeacher = str(input())
        cur.execute(sql, (searchTeacher,))
        result = cur.fetchall()
        for data in result:
            print(data)

    elif menu == 15:
        sql = "SELECT * FROM lecture WHERE lectureName = %s"
        print("검색을 원하는 강의 이름을 입력해주세요: ")
        lectureName = str(input())
        cur.execute(sql, (lectureName,))
        result = cur.fetchall()
        for data in result:
            print(data)

    elif menu == 16:
        sql = "SELECT * FROM car WHERE carNumber = %s"
        print("검색을 원하는 자동차 번호를 입력해주세요: ")
        carNumber = str(input())
        cur.execute(sql, (carNumber,))
        result = cur.fetchall()
        for data in result:
            print(data)


################################### Update

    elif menu == 17:
        sql = "UPDATE center SET owner=%s  WHERE title=%s"
        print("정보 수정을 원하는 센터이름을 입력해주세요: ")
        centerName = str(input())
        print("새로운 센터장을 입력해주세요: ")
        owner = str(input())
        cur.execute(sql, (owner,centerName,))
        minsungdb.commit()

    elif menu == 18:
        sql = "UPDATE center SET phone=%s  WHERE title=%s"
        print("정보 수정을 원하는 센터이름을 입력해주세요: ")
        centerName = str(input())
        print("새로운 센터번호를 입력해주세요: ")
        phone = str(input())
        cur.execute(sql, (phone,centerName,))
        minsungdb.commit()

    elif menu == 19:
        sql = "UPDATE center SET address=%s  WHERE title=%s"
        print("정보 수정을 원하는 센터이름을 입력해주세요: ")
        centerName = str(input())
        print("새로운 센터주소를 입력해주세요: ")
        address = str(input())
        cur.execute(sql, (address,centerName,))
        minsungdb.commit()




    elif menu == 20:
        sql = "UPDATE member SET memberId=%s  WHERE memberId=%s AND centerTitle=%s"
        print("정보 수정을 원하는 학생이 다니는 센터 이름과 아이디를 입력해주세요: ")
        centerName = str(input())
        oldId = str(input())
        print("새로운 아이디를 입력해주세요: ")
        newId = str(input())
        cur.execute(sql, (newId, oldId, centerName,))
        minsungdb.commit()

    elif menu == 21:
        sql = "UPDATE member SET memberPassword=%s  WHERE memberPassword=%s AND centerTitle=%s AND memberId=%s"
        print("정보 수정을 원하는 학생이 다니는 센터 이름과 기존 아이디와 비밀번호를 입력해주세요: ")
        centerName = str(input())
        Id = str(input())
        oldPassword = str(input())
        print("새로운 비밀번호를 입력해주세요: ")
        newPassword = str(input())
        cur.execute(sql, (newPassword, oldPassword, centerName,Id,))
        minsungdb.commit()

    elif menu == 22:
        sql = "UPDATE member SET memberPhone=%s  WHERE memberPhone=%s AND centerTitle=%s"
        print("정보 수정을 원하는 학생이 다니는 센터 이름과 기존 전화번호를 입력해주세요: ")
        centerName = str(input())
        oldmemberPhone = str(input())
        print("새로운 전화번호를 입력해주세요: ")
        newmemberPhone = str(input())
        cur.execute(sql, (newmemberPhone, oldmemberPhone, centerName,))
        minsungdb.commit()

    #print("22. Update member address")
    #print("23. Update member phone")
    #print("24. Update member email")

    elif menu == 23:
        sql = "UPDATE teacher SET teacherId=%s  WHERE teacherId=%s AND centerTitle=%s"
        print("정보 수정을 원하는 강사가 다니는 센터 이름과 아이디를 입력해주세요: ")
        centerName = str(input())
        oldId = str(input())
        print("새로운 아이디를 입력해주세요: ")
        newId = str(input())
        cur.execute(sql, (newId, oldId, centerName,))
        minsungdb.commit()

    elif menu == 24:
        sql = "UPDATE teacher SET teacherPassword=%s  WHERE teacherPassword=%s AND centerTitle=%s AND teacherId=%s"
        print("정보 수정을 원하는 강사가 다니는 센터 이름과 기존 아이디와 비밀번호를 입력해주세요: ")
        centerName = str(input())
        Id = str(input())
        oldPassword = str(input())
        print("새로운 비밀번호를 입력해주세요: ")
        newPassword = str(input())
        cur.execute(sql, (newPassword, oldPassword, centerName,Id,))
        minsungdb.commit()

    elif menu == 25:
        sql = "UPDATE teacher SET teacherPhone=%s  WHERE teacherPhone=%s AND lectureCenter=%s"
        print("정보 수정을 원하는 강사가 다니는 센터 이름과 기존 전화번호를 입력해주세요: ")
        centerName = str(input())
        oldteacherPhone = str(input())
        print("새로운 전화번호를 입력해주세요: ")
        newteacherPhone = str(input())
        cur.execute(sql, (newteacherPhone, oldteacherPhone, centerName,))
        minsungdb.commit()

    elif menu == 26:
        sql = "UPDATE lecture SET lectureLocation=%s  WHERE lectureCenter=%s AND lectureName=%s"
        print("정보 수정을 원하는 센터와 강의 이름을 입력해주세요: ")
        centerName = str(input())
        oldName = str(input())
        print("새로운 강의 지역을 입력해주세요: ")
        newLocation = str(input())
        cur.execute(sql, (newLocation, centerName, oldName,))
        minsungdb.commit()

    elif menu == 27:
        sql = "UPDATE lecture SET lectureDay=%s  WHERE lectureCenter=%s AND lectureName=%s"
        print("정보 수정을 원하는 센터와 강의 이름을 입력해주세요: ")
        centerName = str(input())
        oldName = str(input())
        print("새로운 강의 날짜를 입력해주세요: ")
        newDay = str(input())
        cur.execute(sql, (newDay, centerName, oldName,))
        minsungdb.commit()


    elif menu == 28:
        sql = "UPDATE lecture SET lecturePay=%s  WHERE lectureName=%s AND lectureCenter=%s"
        print("정보 수정을 원하는 센터와 강의 이름을 입력해주세요: ")
        centerName = str(input())
        oldName = str(input())
        print("새로운 강의 요금을 입력해주세요: ")
        newPay = str(input())
        cur.execute(sql, (newPay, oldName, centerName,))
        minsungdb.commit()


    elif menu == 29:
        sql = "UPDATE car SET carNumber=%s  WHERE carNumber=%s AND centerTitle=%s"
        print("정보 수정을 원하는 센터이름과 차량 번호를 입력해주세요: ")
        centerName = str(input())
        oldNumber = str(input())
        print("새로운 차량 번호를 입력해주세요: ")
        newNumber  = str(input())
        cur.execute(sql, (newNumber, oldNumber, centerName,))
        minsungdb.commit()

################################### Show all center people information

    elif menu == 30:
        sql = "SELECT * FROM member WHERE centerTitle = %s UNION SELECT * FROM teacher WHERE centerTitle = %s"
        print("정보 보기를 원하는 스포츠센터 이름을 입력해주세요: ")
        title = str(input())
        cur.execute(sql, (title,title,))
        result = cur.fetchall()
        for data in result:
            print(data)

    else:
        break
    minsungdb.commit()