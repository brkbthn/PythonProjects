# Konu: Methodlar  3 ayrılır
# 1-) Instance Methods = self anahtar kelimeli parametre olmak zorunda onun dışında diğer parametreler opsiyonelrdir) /şu ana kadar öğrenilen metotlar

# 2-) Class Methods = @classmethod cls anahtar kelimeli parametre olmak zorunda onun dışında diğer parametreler opsiyonel

# 3-) Static Methods = @staticmethod default anahtar kelime ileile parametre yok onun dışında diğer parametreler opsiyonel sınıf üzerinden çağırılabilir


class Calisan:
    sirket = "Devran Academy"
    def __init__(self, isim, soyad, sabitMaas, prim):
        #Instance variable
        self.isim = isim
        self.soyad = soyad
        self.sabitMaas = sabitMaas
        self.prim = prim
        #self anahtar kelimesi dinamikliği sağlıyor, yani manipülasyon yaptığımızın göstergesi dolayısıyla statik olmayan bir metot olduğunu anlıyoruz

    def toplamMaas(self):
        return self.sabitMaas + self.prim

    @classmethod #eğer bu decorator kullanılmazsa sınıf üzerinden sirket ismine ulaşılamaz: printf(Calisan.getSirketIsmi(Calisan)) şeklinde class ismi girilmesi gerekir
    def getSirketIsmi(cls):
        return cls.sirket

    @staticmethod
    def bilgi():
        print("calisan sinifinin static metotudur")

    @staticmethod
    def bilgi2(info = None):
        if info != None:
            print(info)
        else:
             print("calisan sinifinin 2. static metotudur")



c1 = Calisan("berk", "batuhan", 23000, 8000)
c2 = Calisan("berk batuhan", "devran", 28000, 8800)
print(c2.toplamMaas()) #nesne metotu olduğuna e nesne üzerinden erişildiğine dikkat et
print(Calisan.toplamMaas(c2)) #sınıf üzerinden erişilebilmesi için parametre olarak bir nesne istedi

print(Calisan.getSirketIsmi()) #bir class metot olduğuna ve sınıf üzerinden sınıfa ait değişkene erişilebildiğine dikkat et
print(c1.getSirketIsmi()) # obje üzerinden de erişilebildiğine ikkat et: oluşturulan objeler ototmatik olarak sınıfın şirket bilgisini kullanıyor

c1.bilgi() #bir static metot olduğuna ve sınıf üzerinden erişilebildiğine dikkat et
Calisan.bilgi() #static metot olduğu iççin parametre yollamadan çağırabildik çünkü static metotlar nesneye bağlı değildir

# class metotun static metottan farki cls gizli parametresinin bulunmasıdır cls magic olduğu için bizim parametre girmemize gerek yoktur
# ayrıca self oluşturulan nesneyi yemsil ederken cls de sınıfı temsil eder ve sınıf üzerinden işle yapmamımızı sağlar



c2.bilgi2()
c2.bilgi2("berk batuhan devran tarafından olusturulmustur")