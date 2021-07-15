#INPUT
#Dòng đầu: Số nhà và số tiền ban đầu
#Giá tiền các ngôi nhà và địa chỉ


count_house = int(input(
    "Nhap so luong ngoi nha can ban: "
))
before_money = int(input(
    "Nhap so tien ban dau: "
))

lst_house = []
cart = []
lst_house_bought = []

for i in range(0, count_house, 1) :
    house = input(
        "Nhap ten ngoi nha thu {}: ".format(str(i+1))
    )
    lst_house.append([house])
    price = float(
        input("Nhap gia tien cua ngoi nha {}: ".format(lst_house[i][0]))
    )
    lst_house[i].append(price)

print("Danh sach nha can ban \n \n")
for i in range(0, count_house, 1) :
    print("{}. {} --- Gia tien: {}\n"
    .format(str(i+1),str(lst_house[i][0]),str(lst_house[i][1])))
print("{}. Thoat".format(str(len(lst_house)+1)))

count = 0
while True:
    file = open('bai2_de2.txt','w')
    print("Nhap lua chon cua ban \n")
    choice = int(input())
    file = open('bai2_de2.txt','w')
    ele = lst_house[choice-1][0]
    price = lst_house[choice-1][1]
    before_money -= price
    a = "{} ----- Gia: {}".format(ele, str(price))

    lst_house_bought.append(a)
    print(lst_house_bought)
    if (before_money <= 0) :
        print("Ban da het tien :((")
        file.write("Tong so nha da mua: {} \n".format(len(lst_house_bought)))
        for c in lst_house_bought:
            file.write(
                "{} \n"
                .format(str(c))
            )
        file = open('Z:/Python/bai2_de2.txt')
        break


