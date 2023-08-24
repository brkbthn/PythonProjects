# operator overloading (operator aşırı yüklenmesi)

sayi1 = 10
sayi2 = 20
sonuc = sayi1 +sayi2

print(sonuc)

ad = "berk batuhan"
soyad = "devran"
isim = ad+" "+soyad

print(isim)

# + operatoru birden fazla iş yapabiliyor

# arka tarafta işlem şu şekilde gercekleşir

sonuc2 = int.__add__(sayi1,sayi2)
print(sonuc2)

isim2 = str.__add__(str.__add__(ad," "), soyad)
print(isim2)
