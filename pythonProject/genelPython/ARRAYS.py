import array
sayılar = array.array("i", [-2, 2, 4, -7])
print(sayılar)
import array as arr
sayılar = arr.array("i", [-2, 2, 4, -7])
print(sayılar)

from array import *
sayılar = array("i", [-2, 2, 4, -7])
print(sayılar)
from array import *
sayılar = array("I", [9, 2, 4, 7])  # "I" ==> kesirli sayı ya da negatif sayı eklenemz
print(sayılar)

print(sayılar[0])
print(sayılar.buffer_info()) #arrayın nerede tutulduğunu ve içerisinde kaç tane eleman bulunduğunu verir.
print(sayılar.typecode) # generator tipini sorgular

for index in range(len(sayılar)):
    print(sayılar[index], end=" ")
harfler = array("u", ["f", "b", "s"]) # 9 2 4 7 array('u', 'fbs')
print(harfler)
print(harfler[0])

""" Generators """
from array import *
sayılar = array("i", [-2, 0, 2, 3, 4, 10]) #Generatörler sayesinde ram de yer kaplamadan iş yapılabilir.
print([sayı for sayı in sayılar])
print((sayı for sayı in sayılar)) # generator obje oluşturuldu ramde yer kaplamadı
print(list(sayı for sayı in sayılar))
print(set(sayı for sayı in sayılar))
print(tuple(sayı for sayı in sayılar))
print(sum(sayı for sayı in sayılar))
print(max(sayı for sayı in sayılar))

for sayı in (sayı*sayı for sayı in sayılar):
    print(sayı, end=" ") # Generatorler de bu şekilde kullanılabilir
print()
i = 0
while i < len(list(sayı*sayı for sayı in sayılar)):
    print(list(sayı*sayı for sayı in sayılar)[i], end=" ")
    i += 1
print()

sayılar3 = array(sayılar.typecode, (sayı for sayı in sayılar))
print(sayılar3)

for sayı in sayılar3:
    print(sayı, end=" ")
print()

i = 0
while i < len(sayılar3):
    print(sayılar[i], end=" ")
    i += 1
print()

generator = (sayı*sayı for sayı in sayılar)
i= 0
while i < len(sayılar3):
    print(sayılar[i], end=" ")
    i += 1
print()
""" Kullanıcıdan Array Elemanlarını Alma""" #arr.index()
from array import*
arr = array("i", [])
# printer(arr)
n = int(input("Diziye kaç tane eleman eklemek istiyorsunuz?"))
for i in range(n):
    sayi = int(input("lütfen eklemek istediğiniz sayıyı giriniz"))
    arr.append(sayi)
print(arr)

"""Array içerisindeki elelmanı bulma"""
from array import array
arr = array("i", [2, 5, 8, -1, 0, 8, 76])
aranacakSayı = int(input("lütfen aramak istediğiniz sayıyı giriniz."))

i = 0
for sayı in arr:
    if sayı == aranacakSayı:
        print("{} değeri {}. indekste bulunmaktadır.".format(aranacakSayı, i))
    else:
        print("aradığınız sayı bu array içerisinde bulunmamaktadır.")
        break # ilk bulunan indexte durmasını sağlar
    i += 1

aranacakSayı = int(input("lütfen aramak istediğiniz sayıyı giriniz."))
print("{} değeri {}. indekste bulunmaktadır.".format(aranacakSayı, arr.index(aranacakSayı)))

""" Array İçerisindekş elemanı silme """
arr = array("i", [2, 5, 8, -1, 0, 75, 8, 75])
print(arr)
#Karşılaşılan ilk elemanı silme
arr.remove(8)
print(arr)
#Bütün değerleri silme
for i in arr:
    if i == 75:
        arr.remove(75)
print(arr)
arr = array("i", [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 2])
arr[5] = 100
print(arr)
for index, sayı in enumerate(arr):
    if sayı == 7:
        arr[index] = 100
print(arr)


""" Girilen değerin dizi içerisinde kaç defa geçtiğini bulmak"""

from array import array
arr= array("i", [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 2, 7])
aranacakSayı = int(input("lütfen kaç tane geçtiğini bulmak istediğiniz sayıyı yazınız"))

#1.yol
count = 0

for i in arr:
    if i == aranacakSayı:
        count += 1
print("{} sayısı {} defa geçmektedir.".format(aranacakSayı, count))

#2.yol
aranacakSayıIndex = array("i", [])
for sayı in enumerate(arr):
    if sayı == aranacakSayı:
        aranacakSayıIndex.append(index)
print(aranacakSayıIndex)

#3.yol
print("count metodu: {} sayısı {} defa geçmektedir.".format(aranacakSayı, arr.count(aranacakSayı)))

# ÖRNEK Ekleme, silme ve tersten sıralma işlemlerini metod kullanmadan uygulama.
# 1-) Boş bir dizi oluşturun. Bu diziye 7 tane eleman kullanıcı tarafından eklenecektir.
#     Ekleme işlemini append() metodu kullanmadan gerçekleştirin
# 2-) Bu dizide kullanıcının silmesini istediği değerlerin ailinmesini sağlayın.
#     Silme işlemini remove() metodunu kullanmadan gerçekleştirin.
# 3-) Bu dizinin elemanlarının tersine çevrilmesini sağlayın.
#     Tersine çevirme işlemini reverse() metodunu kullanmadan gerçekleştirin.

# 1
from array import array
dizi = array("i", [])
for i in range(7):
    sayı = int(input("lütfen eklemek istediğiniz sayıyı yazınız!"))
    dizi += array("i", [sayı]) # iki array birbiriyle toplandı
print(dizi)

delVal = int(input("lütfen silmek istediğiniz sayıyı giriniz"))
degerSilinmişDizi = array("i", [])
for i in dizi:
    if i != delVal:
        degerSilinmişDizi += array("i", [i])
dizi = degerSilinmişDizi
print(dizi)
tersDizi = array(len(dizi))
for i in range(len(dizi)-1, -1, -1):
    tersDizi += array("i", [dizi[i]])
dizi = tersDizi
print(dizi)




