distance = int(input("ใส่ระยะทาง : "))


if distance >= 5 and distance <= 50:
    print("10 บาท")
elif distance > 50 and distance <= 100 :
    print("15 บาท")
elif distance > 100 and distance <= 300 :
    print("25 บาท")
elif distance > 300 and distance <= 500 :
    print("35 บาท")
elif distance > 500 :
    print("45 บาท")
else:
    print("ไม่ส่งจ้า")