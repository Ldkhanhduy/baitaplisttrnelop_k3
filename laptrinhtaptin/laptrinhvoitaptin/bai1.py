def luu_chuoi_vao_tt():
    chuoi=input("Nhập chuỗi kí tự từ bàn phím:")
    nguon=input("Nhap ten tap tin bao (bao gom nguon):")
    f=open(nguon,"w")
    f.write(chuoi)
luu_chuoi_vao_tt()