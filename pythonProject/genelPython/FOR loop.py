# While den farkı squence(dizi) ile çalışır
for i in range(4):
    print(i)
isim = "Berk Batuhan"
for i in isim:
    print(i)
for i in "Batuhan":
    print(i)
for harf in "Batuhan":
    print(harf, end=" ")

sayılar=[2,3,4,5]

for sayı in sayılar:
    print(sayı)
karışık=["a", 24.5, "batuhan"]
for ifade in karışık:
    print(ifade)

bilgiler = {'Batuhan':"Elektrşk Mühendis",'Berk':'Matematik Mühendisi'}
print(bilgiler.items())
for anahtar, değer in bilgiler.items():
    print(anahtar, değer)

benzersizsayılar= {-1, 3, 5, 7}
for sayı in benzersizsayılar:
    print(sayı,end=" ")
değişmeyensayılar=(2, 3, 4, 5, 6)
for sayı in değişmeyensayılar:
    print(sayı)

tuplelist=[(21,32), (41,53), (0,-11)]
for tup in tuplelist:
    print(tup)

for tupsayı1, tupsayı2 in tuplelist:
    print(tupsayı1, tupsayı2)

tuplelist=[(21,32,17), (41,53,17), (0,-11,17), (10,19,17), (12,90,17), (11,13,17)]
for tupe1, tupe2, tupe3 in tuplelist:
    print(tupe1,tupe2,tupe3)

sayılar = list(range(1,51))
print(sayılar)
print(sum(sayılar))
toplam = 0
for sayı in sayılar:
    toplam += sayı
print(toplam)

sayı1 = int(input("lütfen ilk sayıyı giriniz"))
sayı2 = int(input("lütfen ikinci sayıyı giriniz"))
sayılar = list(range(sayı1, sayı2+1))
toplam = 0
for sayı in sayılar:
    toplam += sayı
print(toplam, sum(sayılar))


# bir liste içerisindeki tek ve çift sayıları tutan ve bu elemanları liste içerisinde ayrı ayrı tutan programı yazınız.
sayılar = [2, 3, 4, 5, 65, 67, 78, 90, 12, 2, 6, 78, 65, 45, 43, 64, 87, 98]
ciftliste = []
tekliste = list()
for sayı in sayılar:
    if sayı %2 == 0:
        ciftliste.append(sayı)
    else:
        tekliste.append(sayı)
print("Tek sayılar:{} ve {} tek sayı bulunmaktatadır.".format(tekliste, len(tekliste)))
print("çift sayılar:{} ve {} çift sayı bulunmaktadır".format(ciftliste, len(ciftliste)))


# Şekildeki çıktıyı veren programı yazınız.
"""
*****
*****
*****
*****
*****"""
#1.yol
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()
#2. yol
for i in range(5):
    print(5*"*", end="")
    print()

# Çarpım tablosunu veren programı yazınız.

for i in range(1,11):
    for j in range(1,11):
        print("{}*{}={}".format(i,j,j*i), end="            ")
    print()


# 1 ile 1001 arasında karekökü tam sayı olan sayılar hangileridir.
from math import sqrt
for i in range(1,1001):
    if int(sqrt(i))**2==i :
        print("karekök", i, sqrt(i), "i karekökü tam sayı olan bir sayıdır")

# Öğrenci bilgisi içeren model oluşturacağız. 5tane çğrencinin ayrı ayrı isim, numara, 2. vize notu ve 1 final notunu
# tutan bir dizi oluşturun.Daha sonra her öğrenci için dönem sonu notunu hesaplayın.(1. vizw %25, 2.vize %35 final%40)
# Derste çan sistemi uygulanmaktadır. 5öğrencinin dönem sonu ortalamasının üzerinde kalan öğrenciler dersi geçmiş
# diğer öğreniler kalmı sayılacaktır

öğr1 = {"isim":"Batuhan", "vize notları":[75,45], "final notu": 85}
öğr2 = {"isim":"Aliss", "vize notları":[85,53], "final notu": 85}
öğr3 = {"isim":"Melis", "vize notları":[35,45], "final notu": 85}
öğr4 = {"isim":"Emıly", "vize notları":[75,35], "final notu": 85}
öğr5 = {"isim":"Berk", "vize notları":[25,85], "final notu": 85}

ogrenciler = [öğr1, öğr2, öğr3, öğr4, öğr5]

ogrencilerindonemsonunottoplamı = 0
for ogrenci in ogrenciler:
    ogrDonemSonuNot = ogrenci["vize notları"][0]*0.25+ogrenci["vize notları"][1]*0.35+ogrenci["final notu"]*0.40
ogrencilerindonemsonunottoplamı += ogrDonemSonuNot
ogrencidonemsonunotort =ogrencilerindonemsonunottoplamı/ len(ogrenciler)


for ogrenci in ogrenciler:
    ogrDonemSonuNot = ogrenci["vize notları"][0] * 0.25 + ogrenci["vize notları"][1] * 0.35 + ogrenci[ "final notu"] * 0.40
    if ogrDonemSonuNot>=ogrencidonemsonunotort:
        print("OgrenciAdı:{} ortalaması:{} Geçti".format(ogrenci["isim"],ogrDonemSonuNot))
    else:
        print("OgrenciAdı:{} ortalaması:{} Kaldı".format(ogrenci["isim"], ogrDonemSonuNot))


bilgiler = [[16,"bursa","ipek"],[38, "kayseri", "mantı"], [41,"kocaeli","pişmaniye"]]
for plakakodu, isim, meshurürünü in bilgiler:
    print(plakakodu, isim, meshurürünü)












