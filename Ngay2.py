diem = float(input("Nhập điểm của bạn: "))
if diem >= 8.5:
    print("Bạn đạt loại giỏi")
elif diem >= 6.5:
    print("Bạn đạt loại khá")
elif diem >= 5:
    print("Bạn đạt loại trung bình")
else:
    print("Bạn đạt loại yếu")
# Lệnh for
for i in range(1, 8):
    print(f"7 x {i} = {7 * i}")
# Lệnh while
mat_khau = ""
while mat_khau != "python":
    mat_khau = input("Mật khẩu: ")
print("Đăng nhập thành công")