'''หาเลขคู่เลขคี่
รับค่า
ช็คว่าเป็นเลขหรือเปล่า
และแสดงผลออกมาว่าเป็นเลขคู่หรือเลขคี่'''
print("โปรแกรมตรวจสอบเลขคู่/คี่")
a = int(input("ระบุเลข : "))

if a%2 == 1:
    print("คี่")
else:    
    print("คู่")
