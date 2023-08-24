#Konu = Type of Polymorphizm

# 1-)Mehod Overloading (metodun aşırı yüklenmesi)
# 1-)Method Overriding (metodu geçersiz kılma)

#Python'da bir sınıf içinde  aynı metot ismini kullanmıyoruz. Yani doğrudan method overloading yapamıyoruz

# Notu: mir fonksşyon sınıf içerisindeyse method olarak isimlendirilir


#overloading kavramı
def topla(s1, s2):
    return s1+s2

print(topla(4,6))

def topla(s1, s2, s3=0):
    return s1+s2+s3
print(topla(1,2,3))
# print(topla(1,2)) # hata alırız çünkü python method overloadinge izin vermez ama bizim çeşitli yöntemlerimiz mevcut: değişkenlerden
# sonuncusunun varsayılan değerini sıfır yaparız
print(topla(1,2))





class Islem:
    # def topla(self,sayi1, sayi2, sayi3=0):
    #     return sayi1+sayi2+sayi3

    def topla(self, sayi1 = None, sayi2 = None, sayi3 = None):
        sonuc = 0
        if(sayi1 != None and sayi2 != None and sayi3 != None):
            sonuc = sayi1 + sayi2 +sayi3
        elif sayi1 != None and sayi2 != None:
            sonuc = sayi1+sayi2
        else:
            sonuc = sayi1
        return sonuc   #single entry single exit


i1 = Islem()

print(i1.topla(1,23,45))
print(i1.topla(1,23))