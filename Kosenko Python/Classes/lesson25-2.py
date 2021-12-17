class Human:
    def info(self,n):
        for i in range(n):
            print(f"Name:{self.name} , \nSurname:{self.surname} , \nYear:{self.year_of_birth}")
    def years(self,year):
        age=year-self.year_of_birth
        return age
    pass
p1=Human()
p1.name='Illia'
p1.surname='Katerinych'
p1.year_of_birth=2007
p1.info(1)
print(p1.years(2021))

p2=Human()
p2.name='Den'
p2.surname='Dmitriev'
p2.year_of_birth=1997
p2.info(1)
print(p2.years(2021))

p3=Human()
p3.name='Stas'
p3.surname='Matveychuk'
p3.year_of_birth=2006
p3.info(1)
print(p3.years(2021))
