"""Arithmetic operators"""
a=4
b=3
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division
print(a%b) #Moduls
print(a**b) #Exponensiations
print(a//b) #Floor division

"""Assigment Operators"""
#  = , +=, -=, *=, /=, %=, //=, **=

c = 5
isim = "batuhan"
print(c,isim)

c = c+3
print(c)

c += 3
print(c)

d = 10
print(d)
d = d-3
print(d)
d -= 3
print(d)

e = 15
print(e)
e *=4
print(e)

g = 75
g %=15
print(g)

h = 5
h **=2
print(h)


# temp

"""sayı1 = 10
sayı2 = 20
print("sayı1 {} sayı2 {}".format(sayı1,sayı2))
temp = sayı2
sayı2 = sayı1
sayı1 = temp
print("sayı1 {} sayı2 {}".format(sayı1,sayı2))

# temp kullanmadan
sayı1 = 10
sayı2 = 20
print("sayı1 {} sayı2 {}".format(sayı1,sayı2))
sayı1,sayı2 = sayı2,sayı1
print("sayı1 {} sayı2 {}".format(sayı1,sayı2))

# Örnek
#Kare ve dikdörtgenin alanını hesaplayan program
kenar1 = float(input("lütfen hesaplamak istediğiniz dikdörtgenin 1. kenarını giriniz."))
kenar2 = float(input("lütfen hesaplamak istediğiniz dikdörtgenin 2. kenarını giriniz."))
print("dikdörtgenin alanı: {}".format(kenar1*kenar2))
print("dikdörtgrnin çevresi: {}".format(2*(kenar1+kenar2)))

# Örnek
#Çemberin alanı ve çevresini bulan program yazınız
r = float(input("çemberin yarıçapını giriniz"))
print("çevre:",2*(3.14)*r)
print("alan:",(3.14)*r**24)

# Örnek
#Silindirin hacmini hesaplayan program
r,h = float(input("lütfen silindirin taban yarıçapını giriniz")),float(input("lütfen silindirin yüksekliğini giriniz"))

print("Hacim:",(3.14)*r*r*h)

# Örnek
#ikinci dereceden denklemlerin köklerini bulan program

a = float(input("kareli terimin katsayısını giriniz"))
b = float(input("x li terimin katsayısını giriniz"))
c = float(input("x^0 li terimin katsayısını giriniz"))
delta = b**2-4*a*c
print("a*x*x+b*x+c")
print(delta)
print("Delta sıfırdan küçükse kökler sanaldır")
print("kök1:",(-b-(delta**0.5))/2*a)
print("kök2:",(-b+(delta**0.5))/2*a)

# Örnek
#Beş basamaklı sayının rakam değerleri toplamı
a = float(input("1.basamak"))
b = float(input("2.basamak"))
c = float(input("3.basamak"))
d = float(input("4.basamak"))
e = float(input("5.basamak"))
print("rakamlar toplamı:",a+b+c+d+e)
"""




"""Comparison Operators"""
#  ==  !=  <  >  <=  >=

a = 10
b = 15
c = 20
d = 20
print(a==b)
print(a!=b)
print(c == d)
print(c != d)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print("{} > {}".format(a,b),a>b)

isim = "batuhan"
print(isim=="batuhan")
print(isim=="berk")
print("A">"B")# Harfleri 1 den başlayarak numaralandırdığını düşün
print("batuhan">"berk")
print("devran"<"berk")
print("F">"f") # büyük harfler küçük farflerden önce gelir #ascıı tablosunu incele
print("Batuhan"<"batuhan")

# .lower()  ,  .upper() # bütün harfleri büyük ya da küçük harflere çevirir
print("BATUHAN".lower())
print("Batuhan".lower()<"batuhan")
print("Batuhan".lower()=="batuhan")
print("Batuhan"<"batuhan") # alt tuşuna basıp mausla yeni yerler seçersen imleç sayısını artırabilirsin

# Logical Operators
# OR  Tablosu  (veya)
# OR  | k1 k2 | s
#------------------
#     | 0  0 |0
#     | 0  1 |1
#     | 1  0 |1
#     | 1  1 |1

k1 = 5<6
k2 = 7<8
print(k1,k2)
print(k1 or k2)

a,b = 10,15
print(a<15 or b<20)
print(a>15 or b<20)
print(a<15 or b>20)
print(a>15 or b>20)


# AND tablosu  ( ve )
# AND | k1 k2 | s
#------------------
#     | 0  0 |0
#     | 0  1 |1
#     | 1  0 |1
#     | 1  1 |1

k1 = 5<6
k2 = 7<8
print(k1,k2)
print(k1 and k2)

a,b = 10,15
print(a<15 and b<20)
print(a>15 and b<20)
print(a<15 and b>20)
print(a>15 and b>20)

# NOT (değili) (True)'=  false  (False)'=True
anahtar = True
print("anahtar", anahtar)
anahtar = not anahtar
print("anahtar", anahtar)


# 0=false   0 dışındaki her değer true
sayı1 = 0
print(not sayı1)
sayı2 = 5
print(not sayı2)
#bool()
print(bool(-1))
print(bool(0))
print(bool(1.1))
print(bool("ahmet")) # içi dolu str ler true boş olnalar false, içinde boşluk olanlar true
print(bool(""))
print(bool(" "))

# KISA DEVRE
# ASSOCİATİVİTY
# OR  Tablosu  (veya)
# OR  | k1 k2 | s
#------------------
#     | 0  0 |0
#     | 0  1 |1
#     | 1  0 |1
#     | 1  1 |1

# AND tablosu  ( ve )
# AND | k1 k2 | s
#------------------
#     | 0  0 |0
#     | 0  1 |1
#     | 1  0 |1
#     | 1  1 |1

print(2<3 or 3<4 or 4<5 or 5<6)
print(2<3 or 3<4 or 4<5 or 5<6)
print(2>3 or 3>4 or 4>5 or 5>6)
print(2>3 or 3>4 or 4>5 or 5>6)
print(2<3 or 3>4 or 4<5 or 5<6)


print(2<3 and 3<4 and 4<5 and 5<6)
print(2<3 and 3<4 and 4<5 and 5<6)
print(2>3 and 3>4 and 4>5 and 5>6)
print(2>3 and 3>4 and 4>5 and 5>6)


sayı = int(input("ltfen 1-15 arasında sayı giriniz"))
sonuç = sayı>=11 and sayı<=15
print(sonuç)
# ÖRNEK
# Kullanıcı giriş belgelerini sorgulama

"""bir davette içeriye giriş için bir şifre belirlenmiştir. Bu şifre "BATUHAN ACADAMY" dir. Ayrıca davete giriş için
kişinin 18 yaşı dahil olmak üzere 18-30 yaş arasında olması gerekmektedir. Kullanıcıdan yaş,şifre ve veli bilgilerini 
alarak u kullanıcının içerigirip giremeyeceğinş gözlemleyiniz."""

"""şifre = input("şifreyi giriniz")
yaş = int(input("yaşınızı giriniz"))
sonuç = (şifre=="BATUHAN ACADEMY" and  18<=yaş<30)  or (şifre=="BATUHAN ACADEMY" and yaş<30 and veli=="evet")
veli = input("Veliniz yanınızda mı?")
print(sonuç)"""

""" UNARY OPERATORS  (TEK TERİMLİ OPERATÖRLER)"""
# +  -
print(1+++++++2)
sayı=+++++5
print(sayı)
sayı=-sayı
print(sayı)
sayı=--sayı
print(sayı)
""" IDENTITY OPERATORS(BENZERLİK OPERATÖRLERİ)"""
#type(tip) ve value(değer) kontrolü
print(5 == 5)
#print(5 is 5)
print(type(5) is type(5) and 5==5)
#print(5 = 5.0)
#print(5 is 5.0)
print(type(5) is type(5.0) and 5 == 5.0)

print((2<3) == True)
print((2<3) is True)



print(5 == 5)
print(5 is not 5)
print(type(5) is not type(5) or  5 != 5)
print(5 == 5.0)
print( 5 is not 5.0)
print(type(5) is not type(5.0) or 5 != 5.0)

print(type(16) is type(16) and 16==16)
print(type(16) is type(16.0) and 16==16.0)
print(type(16) is type(15) and 16==15)

## is yerine isinstance kullan
print(isinstance(99,int))
print(isinstance(19.0,float))


print(isinstance(16,type(16)) and 16==16)
print(isinstance(16,type(16.0)) and 16==16.0)
print(isinstance(16,type(15)) and 16==15)



print(type(16) is not type(16) or 16!=16)
print(type(16) is not type(16.0) or 16!=16.0)
print(type(16) is not type(15) or 16!=15)

print(not isinstance(16,type(16))  or 16!=16)
print(not isinstance(16,type(16.0)) or 16!=16.0)
print(not isinstance(16,type(15))  or 16!=15)

#kullanıcıdan iki kelime alıp ıdentitiy operatörlerle kıyasla

k1,k2 = input("1.Kelime") , input("2.Kelime")   # tip+değer >is  değer>==
print(k1==k2)
print(k1 is k2)
print(k1 != k2)
print(k1 is not k2 )

"""Bitwise operators"""

print(3&2) #bitwise and
print(9 | 14) #bitwise or
print(~2)#bitwise not (compliment) -A=A'+1
print(6^5)#bitwise xor "aynıysa 0 farklıysa 1
print(7>>2)#bitwise right shift
print(3<<2)#bitwise rihgt shift


#Membership Operators
liste = [1,2,3]
print(liste)
print(1 in liste)
print(4 in liste)
print(1 not in liste)
kelimelistesi = ["berk","batuhan","devran"]
print("berk" in kelimelistesi)
print("batuhan" not in kelimelistesi)



"""NUMBER SYSTEM CONVERSİON"""

#Binay(ikilik taban)
print(bin(11))
print(bin(2))
print(bin(2*2))
print(bin(2*2*2*2))

#Decimal(onluk taban)
print(10)
print(10*10)
print(10*10*10)

#Octal(sekizlik taban)
print(oct(26))
print(oct(8))
print(oct(8*8))
print(oct(8*8*8))
print(oct(8*8*8*8))

#Hexadecimal(on altılık taban)
print(hex(11))
print(hex(12))
print(hex(13))
print(hex(14))
print(hex(15))
print(hex(16))


print(0b10)
print(0o10)
print(0x10)

#örnek:Kullanıcının girdiği sayıyı 2, 8 ve 16 tabanına karşılık gelen değerlerin çıktısını verenprogramı yaz!
sayı=int(input("lütfen bir sayı giriniz"))
print("binary {}".format(bin(sayı)))
print("octal {}".format(oct(sayı)))
print("hexadecimal {}".format(hex(sayı)))
