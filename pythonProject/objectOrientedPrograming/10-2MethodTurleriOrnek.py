from datetime import date
class Kisi:

    zam_orani = 1.1
    kisi_sayisi = 0

    def __init__(self, isim, yas): #constructor
        self.isim = isim
        self.yas = yas
        Kisi.kisi_sayisi +=1

    def bilgilerini_soyle(self): #instance method
        return "ad:{} yas:{}".format(self.isim, self.yas)

    @classmethod
    def kisiSayisiniGoster(cls):
        print(cls.kisi_sayisi)

    @classmethod
    def stringIleOlustur(cls, strNew):
        isim, yas = strNew.split("-") # - karakterine göre ayır
        return cls(isim, yas) # constructor a değer yolluyor

    @classmethod
    def dogumYiliIleOlustur(cls, isim, dogumYili):
        return cls(isim, date.today().year-dogumYili)

    @staticmethod
    def dogumYiliHesapla(kisi): #içerisine değişken almak zorunda değil, ayrıca magic deişkeni de diğer method türlerinden farklı olarak mevcut değil
        return date.today().year-kisi.yas

    @staticmethod
    def merhaba():
        print("Merhaba, ben Kisi sınıfıyım")



kisi1 = Kisi("batuhan", 23)
Kisi.kisiSayisiniGoster()
kisi2 = Kisi("mehmet", 24)
Kisi.kisiSayisiniGoster()

# eğer dışarıdan çok sayıda bizim class ımızın veri depolama şekline uymayan veri eklememiz gerkirse;
# bir classmethod olan strinIleOlustur methodunu kullanarak classa uyygun veri tipinde nesneler oluşturabiliriz
# class methodların en önemli özelleriklerinden biri bu işlem ile görülebilir

kisi3 = Kisi.stringIleOlustur("burak-28")
Kisi.kisiSayisiniGoster()
print(kisi3.bilgilerini_soyle())


# eğer dışarıdan bizim istedeimiz yaş formatından farklı olarak doğum yılı gelirse:
# classmethod kullanarak(dogumYiliIleOlustur) yine kendi veri türümüze uygun hale getirilmiş nesneler oluşturabiliriz

kisi4 = Kisi.dogumYiliIleOlustur("sehriban", 1966)
Kisi.kisiSayisiniGoster()
print(kisi4.bilgilerini_soyle())

#instance methodun anlam kazanabilmesi için bir nesne üretilmesi gerekir, parametre olarak nesneyi alır
#classmethod bir nesneye bağlı değildir parametre olarak sınıfı alır




print(Kisi.dogumYiliHesapla(kisi4))
# static method classın kendisinden de classtan oluşan nesnelerden de bağımsız olarak çalışabilir, class üzerinden veya nesne üzerinden erişilebilir
Kisi.merhaba()
kisi1.merhaba()


##### NOTTTT  ###########

# Instance methodlar sadece nesneleri, classmethodlar hem sınıfı hem de sınıfın nesnelerini, sataticmethodlar da hem sınıfı hem de nesneleri kapsar