for i in range(2, 10):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
# Tính tổng số chẵn 1-100
tong = 0
for i in range(1, 101):
    if i % 2 == 0:
        tong += i
print(f"Tổng các số chẵn từ 1 đến 100 là: {tong}")
# Đoán số
import random
So_bi_mat = random.randint(1, 100)
So_doan = ""
while So_doan != So_bi_mat:
    So_doan = int(input("Đoán số từ 1 đến 100: "))
    if So_doan < So_bi_mat:
        print("Số bạn đoán nhỏ hơn số bí mật")
    elif So_doan > So_bi_mat:
        print("Số bạn đoán lớn hơn số bí mật")