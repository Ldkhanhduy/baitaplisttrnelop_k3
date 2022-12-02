def them_ki_tu_vao_chuoi():
    nguon=input("Nhap ten tap tin (bao gom nguon):")
    chuoi=input("Nhap chuoi muon them:")
    with open(nguon,"a") as f:
        f.write(chuoi)
them_ki_tu_vao_chuoi()