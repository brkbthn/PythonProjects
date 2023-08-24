"""Break anahtar kelimesi"""

sayı = 0
while True:
    print(sayı)
    if sayı == 100:
        break
    sayı += 1

while True:
    n = float(input("lütfen bir sayı giriniz( çıkış değeri 0 dır)."))
    print("{}karesi = {}".format(n,n*n))
    if n ==0:
        print("programı kullandığınız için teşekkür ederiz")
        break


# Bir stringi belirlenen bir harfe kadar yaz be bu harfin stringin kaçıncı indexinde olduğunu bulan program.

index = 0
for harf in "Berk Batuhan":
    if harf == "K" or harf =="k":
        print("{} harfi {}. indexte bulunmaktadır".format(harf,index))
        break
    index += 1
"""Enumerate Anahtar kelimesi"""

enum = enumerate("BerK Batuhan")
print(enum)
print(list(enum))

for index, harf in enumerate("Berk Batuhan"):
    if harf.lower() == "k":
        print("{} harfi {}. indexte bulunmaktadır".format(harf, index))
        break

enum = enumerate("berk batuhan", 5)
print(enum)
print(list(enum))

# Şifreyi doğru girmesi için kullanıcıya 3 hak tanıyan programı yazınız.
# Doğru girmediği sürece şifre talep edecek, 3 defa yanlış girerse oturum sonlanacak.

secret_pass = "A1"
count_pass = 3

while True:
    sifre = input("lütfen sifreyi giriniz")
    if sifre==secret_pass:
        print("Sisteme Hoşgeldiniz")
        break
    count_pass -= 1
    if count_pass <= 0:
        print("şiifre girme hakkınız bitti.")
        break

# Defter satan bir e-ticaret sitesinde defter satın almak isteyen bir müşteriye kaç adet defter almak istediğini soran
# ve kullanıcıdan istediği defter sayısını stokla kontrol ederek kullanıcıya tepki veren programı yazınız.
# 5 defter alırsa 5 defa "1 adet defter sepete eklendi" desin. (stok miktarı başlangıçta 10 olsun)

stokMiktarı = 10
istenenDefterSayısı= int(input("lütfen satın almak istediğiniz defter sayısını giriniz"))
SepeteEklenenDefterSayısı= 0

for i in range(1,istenenDefterSayısı+1):
    if i>stokMiktarı:
        print("stopta istediğiniz adette defter bulunmamaktadır")
        break
    SepeteEklenenDefterSayısı +=1
    print("1 Adet Defter Sepete Eklenmiştir")
print(SepeteEklenenDefterSayısı,"adet defter sepete eklendi")



"""Continue anahtar kelimesi"""
for sayı in range(1,250):
     if sayı%5 ==0:
         print(sayı,end=" ")
print()

for sayı in range(1,250):
    if sayı % 5 !=0:
        continue
    print(sayı,end=" ")

# 1 ,le 100 arasındaki sadece 35 e bölüebilen saıları continue anahtar kelimesi yardımıyla yazdıınız.

for i in range(1,1001):
    if i % 35!=0:
        continue
    print(i,end=" ")

# Banka Atm örneği
"""Kartın bir şifresi vardır
Kartın bakiyesi 500 Tl'dir.
3 defa yanlış şifre girilince kart bloke olacaktır.
Atm' nin işlem menüsünde para çekme, para yatırma, bakiye sorgulama ve kart iade işlemleri yapımaktadır."""

sıfre= int(input("lütfen 4 basamaklı şifrenizi giriniz!"))




