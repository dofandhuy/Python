# str1 = "HELLOMyNameHuy"
# # print(str1[:])
# # print(str1[0:])
# # print(str1[:5])
# # print(str1[:3])
# # print(len(str1))
# print(str1.lstrip())
# print(str1.replace('L','t'))
# x= "n" in str1
# print(x)
# str2= "xin chào tôi là {}, năm tôi {} tuổi , đến từ {}"
# print(str2.format("Huy", 22, "Hà Nội"))
# print(max(str1))
# print(max(str2))
# print(min(str1))
# print(min(str2))
# print(str1.replace("L","n"))
# print(str2.title())
# import time;
# x=time.asctime( time.localtime(time.time()))
# print("Thời gian hiện tai: " ,x )

# def printme( str ):
#     "Chuỗi được truyền vào trong hàm"
#     print(str)
#     return;

# printme("hello xin chào mọi người ")


# def sum(args1, args2):
#     total= args1+args2
#     print("Bên trong hàm: ", total)
#     return total;

# total = sum(10,20)
# print("Bên ngoài hàm: ", total)

def changeme( mylist ):
    "Thay doi list da truyen cho ham nay0"
    mylist=[1,2,3,4]
    print("Các giá trị bên trong hàm là: ", mylist)
    return;

mylist=[10,20,30]
changeme(mylist)
print("Các giá trị bên ngoài hàm là: ", mylist)

def printinfo(args, *vartuple):
    "In một tham số đã truyền"
    print("Ket quả là: ")
    print (args)

    for var in vartuple:
        print(var)

    return;

printinfo(70)
printinfo(70,90,50)



square =lambda x1: x1*x1 
print("Bình phương của số là", square(10))