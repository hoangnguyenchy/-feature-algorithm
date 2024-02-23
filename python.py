def dem_chu_viet_trong_chuoi(chuoi):
    tu_dien = {'aw': 'ă', 'aa': 'â', 'dd': 'đ', 'ee': 'ê', 'oo': 'ô', 'ow': 'ơ', 'w': 'ư'}
    dem = 0
    i = 0
    while i < len(chuoi):
        if chuoi[i:i+2] in tu_dien or chuoi[i:i+1] in tu_dien:
            dem += 1
            if chuoi[i:i+2] in tu_dien:
                i += 2
            else:
                i += 1
        else:
            i += 1
    return dem

chuoi_nhap = input("Nhập chuỗi chữ cái Latin: ")
so_chu_viet = dem_chu_viet_trong_chuoi(chuoi_nhap)
print("Số lượng chữ cái Tiếng Việt có thể tạo thành trong chuỗi là:", so_chu_viet)