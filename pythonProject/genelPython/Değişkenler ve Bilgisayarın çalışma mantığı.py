

sayi1 = 1400
sayi2 = 412
print(sayi1+sayi2)
print(sayi1-sayi2)
print(sayi1*sayi2)
print(sayi1/sayi2)
print(sayi1%sayi2)

sayi1 = 5
sayi2 = 15

print(sayi1+sayi2)
print(sayi1-sayi2)
print(sayi1*sayi2)
print(sayi1/sayi2)
print(sayi1%sayi2)

#değişkenler alttre yada alfabe harferiyle başlar
___batuhan = "deneme"
print(___batuhan)

# değişken nasıl oluşturulur?  print("değişken ismi".isidentifier())
print("batuhan".isidentifier())
#önceden tanımlanmış anahtar kelimeleri değişken olarak atayamazsın.

sayi1 = 159
sayi2 = 12
print(sayi1+sayi2)
print(sayi1-sayi2)
print(sayi1*sayi2)
print(sayi1/sayi2)
print(sayi1%sayi2)


sayi1 = 1000
print("sayı1",sayi1)

# değişkenler nerede depolanıyr?
sayi1 = 500
sayi2 = 500

print(sayi1)
print(id(sayi1))
print(id(sayi2))
print(id(500))
#python interpreter inde bütün sayılar depolanmıştır bu nedenle bir sayıya değişken atandığında python interpreterindeki
#adres ram e iletilir sayı ve değişken aynı adreste depolanır


#everything is an object
tamsayi = 10
kesirliSayi = 15.5
print(type(tamsayi)) #int-> integer -> tamsayı
print(type(kesirliSayi)) #float-> kesirli sayı


print(tamsayi*3)
print(tamsayi+kesirliSayi)
format("{}+{}={}".format(tamsayi,kesirliSayi,tamsayi+kesirliSayi))


#str --> string -> karakter dizisi
isim = "batuhan"
print(type(isim))
print(id(isim))
isim = "berk"
print(id(isim))

print("berk batuhan devran")
isim = "berk batuhan"
soyisim = "devran"
print(isim,soyisim)

isim = "batuhan"
soyisim = "devran"
print(isim, soyisim)

fullname = isim + " "+soyisim
print(fullname)

# len() boşluk dahil hakrakter sayısını verir
print(len(fullname))

# fullname[1,2,...]
fullname = "Berk Batuhan Devran"
print(fullname)
print(fullname[0])


print(fullname[1:4])  # 1dahil ve 4. karakter dahil değil
değişmişisim = 'M'+fullname[1:4]+'EL'
print(değişmişisim)

fullname = değişmişisim+" "+fullname[5:]
print(fullname)

# 0--->18
# -19---->-1
fullname = "Berk Batuhan Devran"
print(len(fullname)) # len()---> lenght
print(fullname[18])
print(fullname[-1])
print(fullname[-19])

# len----length

print(fullname[-len(fullname)])
print(fullname[-1])
print(fullname[len(fullname)-1])

print(fullname)
print(fullname[1:])
print(fullname[5:])
print(fullname[:])
print(fullname[0:5])
print(fullname[-19:-14])
print(fullname[-6:])

# atlamalı yazdırma

print(fullname[0:5:1])
print(fullname[0:5:2]) # ikişer atlamalı yazdırmak
print(fullname[0:18:2]) # ikişer atlamalı yazdırmak


# tersten yazdırma

print(fullname[::-1])
print(fullname[18::-1])
print(fullname[0:5])
print(fullname[3::-1])


import sys
sayi1 = 12
print(sys.getsizeof(sayi1))
sayi1 = 123
print(sys.getsizeof(sayi1))
sayi1 = 1234
print(sys.getsizeof(sayi1))
sayi1 = 12345
print(sys.getsizeof(sayi1))
sayi1 = 123456
print(sys.getsizeof(sayi1))
sayi1 = 1234567
print(sys.getsizeof(sayi1))
sayi1 = 12345678
print(sys.getsizeof(sayi1))
sayi1 = 1234567812345678
print(sys.getsizeof(sayi1))
sayi1 = 12345678123456781234567812345678
print(sys.getsizeof(sayi1))
print(sys.getsizeof(sayi1),"bytes")

sayi1 = 10
sayi2 = 10
sayi3 = 10
print("sayi1 adres: {} sayi2 adres: {} sayi3: {}".format(id(sayi1),id(sayi2),id(sayi3)))

isim1 = "batuhan"
isim2 = "batuhan"
print("isim1:{} isim2:{}".format(id(isim1),id(isim2)))


sayi3 = 19
sayi4 = sayi3
print(id(sayi1),id(sayi2),id(19),sep="--")
del sayi3
del sayi4

# print(sayı3)
# print(sayı4)


############## KONU= Typ conversion (Tip dönüşümü)

#print(15+"naber")---> hatalı
print("15"+"naber")
print("yaşınız"+str(30))   # integer ifade string çevrildi
sayı1 = 5
sayı2 = 5.5
karakterler = "185"
print(int(karakterler)+sayı1)  # + ifadesi aynı tür karakterleri toplar
# integer e çevirilen ifadenin içinde sadece sayı olmalıdır
print(float(int(karakterler)+sayı1))
sayı1 = float(5)
print(sayı1)
sayı2 = int(5.5)
print(sayı2)
print(17//6) # //=int()

print(3*"5")
print(3*str(5))
print(int(str(555)*2))
print(int(3*str(5))*3)
print(float(str("189.2"))*2)
## ALT*SHIFT yapıp tön tuşarıyla istenilen ifadeyi oynatabiliriz, istenilirse bu maus ile seçim yapılarak çoklu da yapılabilir

#print(int("55.6"))    hatalı çünkü type dönüşümü yapılırken içeri gerçekten dönüştürülen type ye uymalı burada içeri float

"""
isim = input("lütfen bir isim giriniz")
print("isminiz:",isim)

sayi1 = int(input("lütfen 1. sayıyı giriniz")) !! input() un içerisi str olarak çıkar
sayi2 = int(input("lütfen 2. syıyı giriniz"))
print("sonuç:",sayi1+sayı2)

karakter = input("lütfen erkekseniz E kadınsanız K harfine basınız")
print(karakter)
karakter = input("lütfen erkekseniz E kadınsanız K harfine basınız")[0]
print(karakter)
"""
#exception handling
try:
    sayi1 = int(input("lütfen 1. sayıyı giriniz"))
    sayi2 = int(input("lütfen 2. syıyı giriniz"))
    print("sonuç:",sayi1+sayı2)
except:
    print("lütfen bir sayı değeri giriniz")


sayi1 = float(input("Lütfen 1.sayıyı giriniz"))
sayi2 = float(input("lütfen 2. sayıyı giriniz"))
sayi3 = float(input("lütfen 3. sayıyı girin"))

print("{}+{}+{}={}".format(sayi1,sayi2,sayi3,sayi1+sayi2+sayi3))
print("{}-{}-{}={}".format(sayi1,sayi2,sayi3,sayi1-sayi2-sayi3))
print("{}*{}*{}={}".format(sayi1,sayi2,sayi3,sayi1*sayi2*sayi3))
print("{}/{}/{}={}".format(sayi1,sayi2,sayi3,sayi1/sayi2/sayi3))
print("({}+{}+{})/3={}".format(sayi1,sayi2,sayi3,(sayi1+sayi2+sayi3)/3))
##round()

print("({}+{}+{})/3={}".format(sayi1,sayi2,sayi3,round((sayi1+sayi2+sayi3)/3,2)))


