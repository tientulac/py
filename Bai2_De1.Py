#######################################################
#INPUT:
# Bai 2
#5
#Nguyen Duy Anh
#8 8 6
#Bui Duc Duy
#9 9 7
#Duy Quan Hoa
#6 5 3
#Ukabaduy
#7 7 7
#T’ri TDuy
#9 8 8

lst_sv = []

count_sv = int(input("Nhap so luong sinh vien: "))
count_diem = int(input("Nhap so luong diem cua tung sinh vien: "))

for i in range(0, count_sv, 1) :
    sv = input(
        "Nhap sinh vien thu {}: ".format(str(i+1))
    )
    lst_sv.append([sv])
    for j in range(0, count_diem, 1):
            diem = float(
                input("Nhap diem thu {} cua sinh vien {}: ".format(j+1,lst_sv[i][0]))
            )
            lst_sv[i].append(diem)
try:
    file = open('bai2_de1.txt','w')
    file.write(
        "So luong sinh vien: {} \n".format(str(len(lst_sv)))
    )
    file.write("Danh sach sinh vien: \n")
    sum = 0
    for i in range(0, count_sv, 1):
        for j in range(0, count_diem, 1):
            sum+=lst_sv[i][j+1]
        file.write(
            "{} co tong diem la : {} \n".format(str(lst_sv[i][0]).upper(),str(sum))
        )
        sum = 0
    file = open('Z:/Python/bai2_de1.txt')
except:
    print("Khong mo duoc file")
finally:
    file.close()