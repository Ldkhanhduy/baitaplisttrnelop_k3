import random as r

def ghi_va_doc():
    x=r.choices(range(-1000,1001),k=1000)
    nguon=input("Nhap ten tap tin (bao gom nguon):")
    f=open(nguon,"w")
    tam=[]
    for i in range(10):
        tam.append(i)
    for i in range(100):
        for j in range(10):
            tam[j]=str(x[i*10+j])
        f.write(','.join(tam)+"\n")
    f.close()
    with open(nguon,"r+") as f:
        d=f.read()
        d=d.replace(",", "  ")
        print(d)
ghi_va_doc()