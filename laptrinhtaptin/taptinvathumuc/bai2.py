#bai1
f1=open("D:/data/file.txt","r")
print(f1)
#bai2
f2=open("D:/data/file.txt","w")
print(f2)
#bai3
f3=open("D:/data/file.txt","r+b")
print(f3)
#bai4
f4=open("D:/data/file.txt","r")
print(f4)
#bai5
f4.close()
#bai6
try:
    f6=open("D:/data/file.txt","r")
    f6.read()
finally:
    f6.close()
#bai7
with open("D:/data/file.txt") as f:
    f.read()
    f.close()
#bai8
with open("D:/data/file.txt","w") as f:
    f.write('python')
    f.write('nnlt')
    f.write('ga')
    f.close()
#bai9
with open("D:/data/file.txt","r") as f:
    print(f.read())
    f.close()
#bai10
with open("D:/Ảnh/DSC_0592.JPG","rb") as f:
    print(f.read())
