#Not: overloading java da doğrudan yapılırken pythonda dolaylı olarak yapılır, ilerileyen kısımda işlenecek

# Duck Typing ; eğer yürüyor ve vak vak diye se çıkarıyorsa o bir ördektir)

class Arac:
    def __init__(self, tur):
        self.tur = tur

    def calis(self):
        pass

class Araba(Arac):
    def __init__(self):
        super(Araba, self).__init__('araba')
    def calis(self):
        print("motor calisti")
        print(" hareket edebilirsiniz")

class Motosiklet(Arac):
    def __init__(self):
        super(Motosiklet, self).__init__('motosiklet')

    def calis(self):
        print("motor calistirildi")
        print("motor ısınmaa basladi")
        print("motor ısınma sureci bitti")
        print("hareket etmeye baslayabilirsiniz")

class Insan:
    def git(self, arac): #polimorfizim sayesinde arac değişkeni Arac sınıfının herhangi bir subclasını tutabilir
        arac.calis()
        print("hareket etmeye başlanan aracın türü: ", arac.tur)


i1 = Insan()
i2 = Insan()
a1 = Araba()
m1 = Motosiklet()

i1.git(a1)
i2.git((m1))
m1.calis()
