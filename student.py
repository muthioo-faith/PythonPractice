# class Student:
#     name="Judy"
#     age=20
#     country="Kenya"
#     school="Akirachix"

class Student:
    school="Akirachix"
    def __init__(self,name,age,country) :
          self.name=name
          self.age=age
          self.country=country
    def greet(self):
        return f"Hello {self.name},welcome to {self.school},how is {self.country}"
            