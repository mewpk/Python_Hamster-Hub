data =[3,2,4,8,10,2,6,9,8,3,7]
kee = []
z = 0
k = 0
print("ผลรวมข้อมูล : "+str(sum(data)))
print("ค่าเฉลี่ย : "+str(sum(data)/11))
for x in range(0, 11):
    if data[x] // 2 == data[x] /2:
        z +=1
    else : kee.append(data[x])
    if x == 10 :
        print("จำนวนที่เป็นเลขคี่ : "+str(kee))
        print("เลขคู่มีทั้งหมด : "+str(z)+" ตัว")