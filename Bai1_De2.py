#######################################################
# Bai 1
import numpy as np

lst = []
new_lst = []
new_lst2 = []
index_max2 = []
index_min2 = []

N = int(input("Nhap so phan tu trong danh sach: "))
for i in range(0, N, 1) :
    ptu = int(input(
        "Nhap phan tu thu {}: ".format(str(i+1))
    ))
    new_lst = new_lst2 = lst.append(ptu)
    
ptu_max1 = np.max(lst)
ptu_min1 = np.min(lst)
    

try:
    file = open('bai1_de2.txt','w')
    if len(lst) > 1:
        new_lst = list(filter((ptu_max1).__ne__, lst))   
        new_lst2 = list(filter((ptu_min1).__ne__, lst))   
        
        ptu_max2 = np.max(new_lst)
        ptu_min2 = np.min(new_lst2)

        for i in range(0, N, 1):
            if lst[i] == ptu_max2:
                index_max2.append(i)
            if lst[i] == ptu_min2:
                index_min2.append(i)
        file.write(
            "Phan tu lon thu 2 la: {} index: {} \n".format(str(ptu_max2),index_max2)+
            "Phan tu nho thu 2 la: {} index: {} \n".format(str(ptu_min2),index_min2)
        )
        file = open('Z:/Python/bai1_de1.txt')
    else:
        file.write("Khong ton tai phan tu can tim")
except:
    print("Khong mo duoc file")
finally:
    file.close()

