#Kendi sınıfımızı oluşturalım

class Insan:
    def ozellikleriniGoster(self):
        print("Berk Batuhan Devran, Matematik Mühendisi, Full stack java developer")


insan1 = Insan()
insan2 = Insan()

# Insan.ozellikleriniGoster() -> hata alırız çünkü self nedeniyle özellikleriniGoster metoduna sadece nesne üzerinden erişebiliriz

insan1.ozellikleriniGoster()



print(type(insan2))
print(type(Insan))#bütün sınıflar type (java da object) sınıfından türer
print(type(dict))
print(type(list))



#Magic Metotlar ; sınıf içerisinde otomatik oluşturulan metotlardır
#magic metotlar __ile başlar ve biter bu stili biz de kendi metotlarımızda kullanabiliriz ama kullanmamız karışıklık olmaması için daha iyidir

print(dir(Insan)) #insan classının hangi metotları taşıdığını gösterir kendi oluşturduklarımız ve magic metotları brilikte gösterir
