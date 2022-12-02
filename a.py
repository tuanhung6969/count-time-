print("Lưu ý năm đầu tiên phải nhỏ hơn năm thứ 2")
a = int(input("tháng đầu tiên là "))
b = int(input("năm đầu tiên là "))
c = int(input("tháng thứ 2 là "))
d = int(input("năm thứ 2 là "))

if b > d:
    print("lỗi")
elif b <= d:
    if d - b ==1 :
        a = 12 - a 
        f = a + c
    if d - b ==0:
        if c - a == 0:
            f == 0 
    if d - b >0:
        a = 12 - a
        s = d - b -1 
        s = s*12
        f = a + c + s
print("Khoảng cách giữa các cột mốc thời gian là " + str(f) + " " + "tháng.")

