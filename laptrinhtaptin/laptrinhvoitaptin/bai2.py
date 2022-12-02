def doc_tap_tin():
    nguon=input("Nhap ten tap tin (bao gom nguon):")
    with open(nguon,"r") as f:
        doc=f.read()
        print(doc)
doc_tap_tin()