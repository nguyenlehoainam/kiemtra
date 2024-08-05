my_tuple = tuple(map(int, input("nhap mot loat cac so nguyen : ").split()))

my_dict = {}

for num in my_tuple:
    if num in my_dict:
        my_dict[num] += 1
    else:
        my_dict[num] = 1

print("cac so thoa man la:", [num for num, count in my_dict.items() if count % 5 == 0 and count % 10 != 0])
