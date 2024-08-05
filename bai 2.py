x = int(input("nhap dich den chu rua can phai di X (1<x<1000) : "))

so_buoc = x // 3  
if x % 3 != 0:
    so_buoc += 1  

print("so buoc toi thieu la :", so_buoc)
