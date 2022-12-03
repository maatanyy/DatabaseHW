<?php
//$mysqli = mysqli_connect("example.com", "user", "password", "database");
//$result = mysqli_query($mysqli, "SELECT 'Please do not use the deprecated mysql extension for new development. ' AS _msg FROM DUAL");
//$row = mysqli_fetch_assoc($result);
//  echo $row['_msg'];

//minsungdb = mysql.connector.connect(
//        host="192.168.56.101",
//        port='4567',
//        user="minsung",
//        password="1234",
//        database="madang")

$conn = mysqli_connect("192.168.56.101","minsung","1234","sportscenter",4567);
mysqli_query($conn, "
    INSERT INTO center (
        title,
        owner,
        phone,
        address
    ) VALUES (
        '충북스포츠센터',
        '오바마',
        '010-3939-2020',
        '청주 충북대학교',
        NOW()
    )
");
?>




