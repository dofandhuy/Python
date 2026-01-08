from datetime import date
class Person:
      def __init__(self, name, country, dateofbirth):
            self.name=name
            self.country=country
            self.dateofbirth= dateofbirth

      def Ageperson(self):
            today = date.today()
            age= today.year-self.dateofbirth.year
            if(today < date(today.year, self.dateofbirth.month, self.dateofbirth.day)):
                 age-=1
            return age
      
adult= Person("Huy", "Viet name", date(2005,4,1))
age =adult.Ageperson()
print("Age of adult = "+str(age))