def bilgiGoster():
    print("benim adım Berk Batuhan Devran")

print(type(bilgiGoster))

bilgiSoyle = bilgiGoster #shallow copy . doğrudan adres kopyalanır

print(bilgiSoyle)
bilgiSoyle() #bilgiGoster fonksiyonu gibi kullanılıyor

print("----------------------------------")
bilgiGoster()

print("----------------------------------")

print(id(bilgiSoyle))
print(id(bilgiGoster))
#kopya fonksşyon ile bizim fonksiyonumuzun id si aynı yani fonksiyon objesi de immutuable değiştirilemez bir objedir

def bilgileriGoster(isim, soyisim):
    print("kisi bilgileri: ", isim, soyisim)
bg = bilgileriGoster
bilgileriGoster("berk", "batuhan")
bg("berk", "batuhan")


#Fonksiyon objelerini parametre olarak gonderme
def topla(sayilar):
    return sum(sayilar)

def carp(sayilar):
    sonuc = 1
    for sayi in sayilar:
        sonuc *= sayi
    return sonuc

def hesapla(toplaFunc, carpFunc, islem, sayilarArg):
    if islem == "topla":
        return toplaFunc(sayilarArg)
    elif islem == "carp":
        return carpFunc(sayilarArg)

sayilar = [2,3,54,6,67]
sonuc = hesapla(topla, carp, "topla", sayilar)
print(sonuc)

def hesapla(toplaFunc, carpFunc, sayilarArg):
    return toplaFunc(sayilarArg), carpFunc(sayilar)#sonucun liste olması için köşeli paranteze alabilirsin

print(hesapla(topla, carp, sayilar))#cevap tuple şeklinde geri döner

toplamSonuc, carpimSonuc = hesapla(topla, carp, sayilar)
print(toplamSonuc)
print(carpimSonuc)