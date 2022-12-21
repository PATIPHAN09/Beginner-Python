''' BMI First '''
# BMI = น้ำหนัก
#สูตร น้ำหนัก/ส่วนสูง กำลังสอง

weight = int(input("ระบุน้ำหนักนะไอน้อน (Kg) : "))
height = int(input("ระบุส่วนสูงเป็นเซ็นติเมตรเด้อ (Cm) : "))
height = height/100
#result = weight/(height*height)
result = weight/(height**2)
print("BMI = " , result)