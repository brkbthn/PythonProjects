"""import math
print(math.sqrt(16))

# as = alias
import math as m
print(m.sqrt(16))

from math import * #artık sadece fonksiyon ismi tazılarak kullanılabilir
print(sqrt(16))

from math import sqrt
print(sqrt(16))

from math import sqrt, factorial, floor, ceil
print(factorial(5))
print(floor(8,9))
print(ceil(9,1))"""

from math import sqrt
def sqrt(*args):
    return "Bu fonksiyon overide edilmiştir"
print(sqrt(64))

import math
help(math)
print(dir(math))

import hesap
toplam = hesap.topla(5,6)
print(toplam)
daireCevre = hesap.daireCevreHesapla(8)
print(daireCevre)
daireAlan = hesap.daireCevreHesapla(7)
print(daireAlan)
print("---------------------------------------------------")
#Konu: Special Variable olan __name__ değişkeninin işlevi
#       _name_ ana modülde kullanıldığında __main__ değerine sahiptir
#       Fakat başka modül import edildiğinde ve o modülde __name__ kullanıldıysa o zaman
#       kullanılan modülün ismine sahiptir.

#HATIRLATMA: Bir modül import edildiğinde edinilen modüldeki kodlar kullanıldığı modülüniçerisine yerleştirilir.

import hesap as h
print(h.__name__)
print(__name__)
print("--------------------------------------------------")
#ÖRNEK: Sayı tahmini oyunu/Bilgisayar 1-50 arasında 1 sayı tutacak ve kullanıcı bu sayıyı
# tahmin etmeye çalışacak
# Kullanıcının tahmin etmesi için sadece 5 hakkı vardır
# Program oyun başlamadan önce 5 saniye beklemede kalmalıdır.(sleep)
#1-) time modülünün içerisinde bulunan sleep fonksiyonundan faydalanılacaktır.
# sleep metodunun ne işe yaradığını ve nasıl çalıştığını kontrol edin.
#2-) random modülünün randint fonksiyonundan faydalanılacaktır.
# randint fonksiyonun ne işe yaradığını ve nasıl çalıştığını kontrol edin.

from time import sleep
from random import randint
print("Sayı tahmin oyunu başlıyor, lütfen bekleyiniz")
sleep(2)
sayi = randint(0,50)
print(sayi)
tahminHakkı = 5
while True:
    if tahminHakkı > 0:
        tahmin = int(input("lütfen tahmininizi giriniz"))
        tahminHakkı -=1

        if tahmin < sayi:
            print("lütfen sayıyı arttırınız")
        elif tahmin > 0:
            if tahminHakkı > 0:
                print("lütfen sayıyı azaltınız")
        else:
            print("kazandınız")
    else:
        print("tahmin hakkınız kalmamıştır")
        break

