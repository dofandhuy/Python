def chao_mung(str):
    a= "Chao mung ban {} đã đến"
    print(a.format(str))
    return;

name= input("Nhập tên: ")
chao_mung(name)