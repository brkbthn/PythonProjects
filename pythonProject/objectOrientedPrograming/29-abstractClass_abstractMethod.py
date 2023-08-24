# KONU: abstract classes (soyut sınıflar) ve abstract methods(soyut metotlar)
# abstraction kavramı yüksek seviyeli programlama dillerinde bulunur
# aslında pythonda abstraction doğrudan yoktur ama abstract base class (ABC) sayesinde dolaylı olarak kendi abstract sınıfımızı oluşturabiliyoruz
# abstract sınıfların oluşturulabilmesi icin ; from abc import ABC, abstractmethod işlei yapılmalıdır
# abstract sınıflar ABC sınıfından kalıtılır
# abstract class'lardan nesne üretilmez
# abstract metot yazılmadan önce,  @abstractmethod kullanılır
# abstract metotların gövdesi yazılmaz.
# pythonda abstract bir sınıfın sadece abstract methodları olabilir
# soyut classlardan türeyen sınıflar mutlaka soyut sınıfın metotlarını override etmelidir
from abc import ABC, abstractmethod

class Makine(ABC):
    @abstractmethod
    def calis(self):
        pass

class CamasirMakinesi(Makine):
    def calis(self):
        print("camasir makinesi calisti")

class BulasikMakinesi(Makine):
    def calis(self):
        print("bulasik makinesi calisti")

class Insan:
    def camasirYika(self, makine:CamasirMakinesi):
        if type(makine) == CamasirMakinesi:
            print("çamasirlar yikandi")
            makine.calis()
        else:
            print("camasşrlar sadece camasır makşnsaında yikanir")


c1 = CamasirMakinesi()
c1.calis()
b1 = BulasikMakinesi()
b1.calis()

i1 = Insan()
i1.camasirYika(c1)