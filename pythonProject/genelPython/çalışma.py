sayı1 = 140
sayı2 = 14
print(sayı1-sayı2)
print(sayı1+sayı2)
print(sayı1*sayı2)
print(sayı1/sayı2)
print(sayı1%sayı2)

sayı1 = 19
sayı2 = 1919
print(sayı1-sayı2)
print(sayı1+sayı2)
print(sayı1*sayı2)
print(sayı1/sayı2)
print(sayı1%sayı2)

# değişkenler harf ya da alttre ile başlarlar

# true ya da false
print("123isim".isidentifier())
print("isim123".isidentifier())
print("print".isidentifier())
"""her ne kadar print fonksiyonuna true dese de bu bizim print fonksiyonuna yai değer atayabileceğimiz 
 anlamına gelmez. Bu nednle pythonda daha önce tanımlanan fonksiyon ya da metodlara değer atayamayız."""

sayı1 = 19
sayı2 = 1919
print("çıkarna",sayı1-sayı2)
print("toplama",sayı1+sayı2)
print("çarpma",sayı1*sayı2)
print("bölme",sayı1/sayı2)
print("mod alma",sayı1%sayı2)

# id() değişkenin depolandığı adresi sorgulama
sayı1 = 500
sayı2 = 500
print(sayı1)
print(id(sayı1))
print(id(sayı2))

# type() değişkenin tipini sorgulamaya yarar
tamsayı = 19
kesirlisayı = 19.19
print(type(tamsayı))  # int--> integer tamsayı
print(type(kesirlisayı)) # float---> kesirli sayı
print(19*3)
print(tamsayı*3)
print(tamsayı+kesirlisayı)
print("{}+{}={}".format(tamsayı,kesirlisayı,kesirlisayı+tamsayı))


# string ---> str
isim = "Berk Batuhan"
soyisim = "Devran"
print(isim,soyisim)

fullname = isim+ " "+soyisim
print(fullname)


# len fonksiyonu
print(len(fullname))

fullname = "Berk Batuhan Devran"
print(fullname[0])
print(fullname[18])
# fullname[0] = "M"   bu şekilde işlem yapılamıyor
print(fullname[0:9])# 0 dahil 9 dahil değil

yeniisim= "M"+fullname[1:3]+"T"
print(yeniisim)

yenifullname = yeniisim+fullname[4:19]
print(yenifullname)
yenifullname = yeniisim+fullname[4:]
print(yenifullname)

# 0123... = -... -5,-4,-3,-2,-1
print(fullname[-1])
print(fullname[-19])
print(len(yenifullname))



#len---> length
print(fullname[-len(fullname)])
print(fullname[len(fullname)-1])


print(fullname[:])
print(fullname[0:18:2])
print(fullname[-19:])
print(fullname[0:4:1])
print(fullname[0:4:])
print(fullname[0:4:2])
print(fullname[::-1])
print(fullname[18::-1])