class Student:
    count=0
    StudentList=[]
    def __init__(self, name, id):
         self.id=id
         self.name=name
         Student.count+=1
         print("đã khởi tạo 1 student")
         Student.StudentList.append(self)
    def display(self):
         print("ID: %d \nName: %s" % (self.id, self.name))
     
Stu1= Student("Huy", 1)
Stu2= Student("Huy", 1)
Stu3= Student("Huy", 1)
Stu4= Student("Huy", 1)
Stu5= Student("Huy", 1)
Stu6= Student("Huy", 1)
Stu7= Student("Huy", 1)
print("Số lượng sinh viên: ", Student.count)

print("--- Danh sách sinh viên ---")
for s in Student.StudentList:
    print(f"ID: {s.id} | Tên: {s.name}")

class Teacher(Student):
     def __init__(self, name, id):
          super().__init__(name, id)
     def show(self):
          print("Đây là giáo viên")


d= Teacher("Manh",2);
d.show();
d.display()