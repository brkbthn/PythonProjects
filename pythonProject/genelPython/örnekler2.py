ad = "Berk Batuhan"
soyad = "Devran"
yaş = 21
print("{},{},{}".format("ad","soyad","yaş"))
print("{},{},{}".format(ad,soyad,yaş))

takim1 = "FENERBAHÇE"
takim2 = "GALATASARAY"
yenitakim1 = takim1[0:5]+" "+takim1[5:]
yenitakim2 = takim2[0:6]+" "+takim2[6:]
print(yenitakim1)
print(yenitakim2)
print(takim1,takim2,sep="\n")


ad = "berk batuhan"
soyad = "devran"
yaş = 21
yaşş = yaş+1

print(ad,soyad,yaş,yaşş)
print(id(ad),id(soyad),id(yaş),id(yaşş))
print(id(21))
print(id(22))

sayı1 = 16
sayı2 = 19
toplama = sayı1 + sayı2
çıkarma = sayı1 - sayı2
çarpma = sayı1 * sayı2
bölme = sayı1 / sayı2
tambölme = sayı1 // sayı2
modalma = sayı1 % sayı2
üsalma = sayı1 ** sayı2

del sayı1
del sayı2
print(toplama,çıkarma,çarpma,bölme,tambölme,modalma,üsalma,sep=" ")



şimdikizaman = 2020
doğum = 1999
print("yaş:{}".format(şimdikizaman-doğum))


sayi1 = float(input("Lütfen 1.sayıyı giriniz"))
sayi2 = float(input("lütfen 2. sayıyı giriniz"))
sayi3 = float(input("lütfen 3. sayıyı girin"))
try:
    print("{}+{}+{}={}".format(sayi1,sayi2,sayi3,sayi1+sayi2+sayi3))
    print("{}-{}-{}={}".format(sayi1,sayi2,sayi3,sayi1-sayi2-sayi3))
    print("{}*{}*{}={}".format(sayi1,sayi2,sayi3,sayi1*sayi2*sayi3))
    print("{}/{}/{}={}".format(sayi1,sayi2,sayi3,sayi1/sayi2/sayi3))
    print("({}+{}+{})/3={}".format(sayi1,sayi2,sayi3,(sayi1+sayi2+sayi3)/3))

    print("({}+{}+{})/3={}".format(sayi1,sayi2,sayi3,round((sayi1+sayi2+sayi3)/3,2)))
except ValueError:
    print("lütfen bir sayı değeri giriniz")
