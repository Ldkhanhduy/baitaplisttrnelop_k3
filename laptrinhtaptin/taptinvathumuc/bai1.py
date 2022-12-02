import os

# bai 1
print('thu muc lam viec hien tai cua chuong trinh:', os.getcwd())


# bai2
def chuyennguon():
    x = input('nhap nguon:')
    os.chdir(x)
    print('thu muc hien tai sau khi chuyen:', os.getcwd())


chuyennguon()


# bai3
def taothumuc():
    ten = "NNLT"
    duongdan = "D:/data/"
    path = os.path.join(duongdan,ten)
    mode = 0o666
    os.makedirs(path,mode)
    print("thu muc",ten,"da duoc tao.")
taothumuc()
#bai4
def lietke():
    nguon ="C:/Users/ACER/Documents/"
    listphantu=os.listdir(nguon)
    print(listphantu)
lietke()
#bai5
def kiemtrataptin():
    nguon="D:/Baitap/BT_EXCEL"
    kiem=os.path.exists(nguon)
    print("tap tin co o trong may:", kiem)
kiemtrataptin()
#bai6
def xoa():
    os.remove(os.path.join("D:/data","ok.txt"))
    os.rmdir(os.path.join("D:/data","NNLT"))
    print("da xoa")
xoa()

