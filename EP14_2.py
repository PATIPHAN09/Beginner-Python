'''
age = int(input("กรอกอายุ : "))
if age > 15:
    print("ไอนี้มันโตแล้ว")
    print("จบการทำงานของโปรแกรมใน IF")
else:
    print("มันยังเด็กอยู่เลย")
print("จบการทำงานของโปรแกรม")

'''



#Ternary Oparator
age = int(input("กรอกอายุ : "))
print ("โต") if age >= 15 else print("เด็ก")