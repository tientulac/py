#######################################################
# Bai 1
#INPUT:
# N: 4
# k: 5
# Dai hoc su pham ha noi
# Cong nghe thong tin
# Chao mung nam hoc moi
# K70 FIT HNUE

lst_chuoi = []
N = int(input("So chuoi muon nhap: "))
k = int(input("Nhap so tu muon so sanh: "))
for i in range(0, N, 1) :
    chuoi = input(
        "Nhap chuoi thu {}: ".format(str(i+1))
    )
    lst_chuoi.append(chuoi)
count = 0
for c in lst_chuoi :
    if len(c.split()) > k:
        count += 1
# Dòng 1: N:Số dòng được nhập chuỗi k: Số chuối có số từ > k 
try:
    file = open('bai1_de1.txt','w')
    file.write(
        "Tong so chuoi: {} \n So chuoi co so tu lon hon {} : {} \n"
        .format(str(N),str(k),str(count))
    )
    for c in lst_chuoi:
        count_c = len(c.split())
        file.write(
            "{} \t So tu: {} \n"
            .format(str(c),str(count_c))
        )
    file = open('Z:/Python/bai1_de1.txt')
except:
    print("Khong mo duoc file")
finally:
    file.close()
