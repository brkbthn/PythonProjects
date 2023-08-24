# Variable'lar 2 ye ayrılır

# Instance Variables
# Class/Static Variables

# namespace obje ve değişkenlerin oluşturulduğu ve depolandığı bir alandır
# -class namespace
# -Object/Instance namespace


class User:
    #class namespace
    sayac = 0
    def __init__(self, isim = "isim yok", kayitTarihi = "20.12.2012"):
        #object/instance namespace
        self.isim = isim
        self.kayitTarihi = kayitTarihi
        User.sayac += 1

#sınıf değişkenlerine hem sınıf ismi üzerinden hem de nesneler üzerinden ulaşabiliyoruz, sınıf değişkenleri aynı zamanda otomatik olarak nesneye de atanır
#fakat ovject(instance) değişkenlere(isim, kayıtTarihi) nesneler üzerinden ulaşabilriken sınıf üzerinden ulaşamayız

print(User.sayac)
user1 = User("berk", "19.02.1999")
user2 = User("baatuhan", "19.09.2019")
print(user1.sayac)
print(User.sayac)

user2.sayac = 3
print(user2.sayac)# user2 nin sayacını değiştirebildik
print(User.sayac) # ancak sınıfın sayac bilgisini değitiremedik

User.sayac = 9    # bu şekilde sınıfın da sayac bilgisini değişirdik
print(User.sayac)

user3 = User("devran", "13.12.1395")
print(User.sayac)
print(user3.sayac)

# sınıf üzerinden sayac bilgisinde yaptığımız değişiklik yeni nesneleri etkiler
# ancak nesneler üzerinden sayac değeri üzerinde değişiklik yaparsak sınıfın sayac değeri dolayısıyla da yeni nesneler etkilenmez

user3.sayac = 1000
print(User.sayac)
user4 = User("a", "12.12.1223")
print(user4.sayac)
print(User.sayac)

#kısaca nesne özelinde yaptığımız değişiklik sadece nesneyi ilgilendirirken sınıf üzerinden yapacağımız değişiklik sınıfı ve
# daha sonra oluşturulacak nesneleri etkiler

# sayacı javadaki statik değişken gibi düşünebilirsin nesneler clas içinde oluşturulalan değikeni referans eder farklı değerler sonradan atanırsa
#artık sonradan atanan değerleri tutarlar