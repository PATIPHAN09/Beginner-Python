#โปรแกรมคำนวนเกรดเหมือนทำข้อสอบ
G = int(input("กรุณาระบุเกรดของเอ็งมา : "))

if G >= 80:
    result = "A"
elif G >= 70:
    result = "B"
elif G >= 60:
    result = "C"
elif G >= 50:
    result = "D"
else :
    result = "F"     

print(result)