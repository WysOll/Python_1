class Human:
    def __init__(self,name,surname,age,birth_place,year_of_birth):
        self.name=name
        self.surname=surname
        self.age=age
        self.birth_place=birth_place
        self.year_of_birth=year_of_birth
    def info(self):
        print(f"Name:{self.name} \nSurname:{self.surname} \nAge:{self.age} \nPlace where birth:{self.birth_place} \nYear:{self.year_of_birth}")
    def years(self,year):
        age=year-self.year_of_birth
        return age
p1=Human('Den','Surname',24,'Ua',1997)
p1.info()
