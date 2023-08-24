### LOOPS

i=1
while i < 5:
    print("berk batuhan devran")
    i = i + 1
print("dögü tamamlandı",i)
for i in range(4):
    print("berk")
print("dögü tamamlandı",i)

for i in range(4):
    print(i)
    print("berk")

for i in [1, 6, 7, 12]:
    print(i)
    print("berk batuhan")

for i in [1, 2, 3, 4]:
    print(i*i)

"""while loop (while döngüsü)"""

#döngüyü kontrol eden değişkenşn artırılma ya da azaltılma işlemi
#şart

i = 1
while i<5:
    print(i)
    i = i+1


i = 4
while i>0:
    print(i)
    i -= 1

i=0
while i<4:
    print("Ezber yok!", end=" ")
    j = 0
    while j<4:
        print("Mantık Var!", end=" ")
        j += 1
    i += 1

sayılar = [10, 20, 30, 40, 50]
index = 0
while index < len(sayılar):
    print(index, sayılar[index])
    index += 1

toplam = 0
i = 1
while i<= 10:
    toplam += i
    i += 1
print("toplam", toplam)

toplam = 0
i = 40
while i<= 50:
    toplam += i
    i += 1
print("toplam", toplam)

# 1-200 arasındaki sayılardan 5 ve 7 ye bölünebilenler

i = 1
while i<=200:
    if i % 5 == 0 and i % 7 == 0:
        print(i)
    i += 1

# 1 den n e kadar olan sayıların toplamını bulan program

n = int(input("1 den kaça kadar olan sayılarnı tplamını istiyorsunuz"))
i = 1
toplam = 0
while i<=n :
    toplam = toplam + i
    i += 1
print("toplam", toplam)

# Bir önceki örneğin farklı bir çözümü

toplam = 0
while n>=0:
    toplam += n
    n -= 1
print("toplam", toplam)


# 5 ve 7 ye bölünemeyen sayılar

while i <= 200:
    if i % 5 != 0 and i % 7 != 0:
        print(i)
    i += 1

i = 0
while i< 6:
    print("&", end=" ")
    j = 0
    while j < 5:
        print("#", end=" ")
        j = j+1
    print()
    i = i+1

i = 0
while i < 6:
    j = 0
    while j< 5:
        print("&", end=" ")
        j += 1
    print()
    i += 1



günler = ["pazartesi" , "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"]

i = 0
while i < 7:
    print(günler[i], end=" ")
    j = i+1
    while j<=31:
        print(j, end=" ")
        j += 7
    print()
    i += 1


# Kullanıcının girdiği sayının sayı değerlerinin toplamını fulan fonksiyon
"""sayı= int(input("lütfen bir sayı giriniz"))

sayıdeğerleri = []

while sayı>0:
    sayıdeğeri = sayı % 10
    sayı // 10
    sayıdeğerleri.append(sayıdeğeri)
print(sayıdeğerleri)

"""

# Faktoriyelini öğrenmek istediğiniz sayıyı giriniz
try:
    n = int(input("faktoriyelini bulmak istediğiniz sayıyı giriniz"))
    i = 1
    sonuc = 1
    if n>=0:
        while i < n:
            sonuc = sonuc*i
            i += 1

        print("{}!=".format(n),sonuc)
    else:
        print("adamı hasta etme")
except ValueError:
    print("lütfen bir tam sayı giriniz")


# Kullanıcının yemek seçimleri doğrultusunda toplam tutarı kullanıcıya söyleyen programı yazınız.
print( """1. Adana/Urfa 20tl
        2. Beyti 25tl
        3. Tantuni 30tl
        4. Çorba 10tl
        5. Tatlı 15tl
        6. İçecek 5 tl
        7. Çıkış""")
toplamTutar = 0
while True:
    secim= int(input("lütfen seçiminizi tuşlayınız"))
    if secim > 0 and secim < 7:
        adet = int(input("kaç edet alırsınız"))
    if secim==1:
        toplamTutar+=20*adet
    elif secim==2:
        toplamTutar+=25*adet
    elif secim==3:
        toplamTuar+=30*adet
    elif secim==4:
        toplamTutar+=10*adet
    elif secim==5:
        toplamTutar+=15*adet
    elif secim==6:
        toplamTutar+=5*adet
    elif secim==7:
        print("siparişiniz için teşekkür ederiz")
        print("Toplamda odenecek tutar:{}".format,toplamTutar)
        break
