import random
from datetime import date
print("Hôm nay là: ", date.today())
# Hàm có tham số và giá trị trả về
def chi_so_bmi(chieu_cao, can_nang):
    bmi = can_nang / (chieu_cao ** 2)
    return round(bmi, 1)
print("Chỉ số BMI của bạn là: ", chi_so_bmi(1.62, 60))
# List
mon_an = ["Phở", "Bún chả", "Cơm tấm"]
mon_an.append("Bánh mì")
print(mon_an[0], len(mon_an))
print("Hôm nay ăn gì? ", random.choice(mon_an))
# Dict
sinh_vien = {"ten": "An", "tuoi": 20, "diem": [8, 7.5, 9]}
sinh_vien["lop"] = "K66"
tb = sum(sinh_vien["diem"]) / len(sinh_vien["diem"])
print(f"{sinh_vien['ten']} - điểm TB {tb:.2f}")
# Duyệt dict
for khoa, gia_tri in sinh_vien.items():
    print(khoa, "->", gia_tri)