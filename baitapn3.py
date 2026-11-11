so_nhap = int(input("Nhập số nguyên: "))
so_lan = 0
for i in range(2, so_nhap):
    j = so_nhap / i
    if j == int(j):
        so_lan += 1
if so_lan != 0:
        print(f"{so_nhap} không phải là số nguyên tố")
else: 
        print(f"{so_nhap} là số nguyên tố")
# dict
ban = {"huy": 1984, "phong": 1995, "phước": 1992, "hùng": 1990, "hải": 1993}
for ten, nam_sinh in ban.items():
    lon_nhat = min(ban.values())
    if nam_sinh == lon_nhat:
        print(f"Người lớn nhất với năm sinh {lon_nhat} là {ten}")
# Đếm số từ trong câu
cau = input("Nhập câu: ")
dem = 0
# Đếm các từ giống nhau
cac_tu = cau.lower().split()
dem_tu = {}
for tu in cac_tu:
    if tu in dem_tu:
        dem_tu[tu] += 1
    else:
        dem_tu[tu] = 1
for tu, so_lan_xuat_hien in dem_tu.items():
    if so_lan_xuat_hien > 1:
        print(f"Từ '{tu}' xuất hiện {so_lan_xuat_hien} lần")
