# Nokta sınıfı için operatörlede overloading gerçekleştirme

from math import sqrt
class Nokta:
    sayac = 0 #static değişkendir

    def __init__(self,x,y):
        self.x = x
        self.y = y
        Nokta.sayac += 1

    #  + operatörü
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Nokta(x,y) #yeni nokta constructor ile olusturuldu

    # > operatötü
    # Noktanın orijine olan uzaklığını hesaplamak için;
    def __gt__(self, other):
        uzunluk1 = sqrt(self.x*self.x + self.y*self.y)
        uzunluk2 = sqrt(other.x * other.x + other.y * other.y)
        if uzunluk1 > uzunluk2:
            return True
        else:
            return False

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __len__(self):
        if self.x > 0 and self.y >0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        elif self.x == 0 and self.y== 0:
            return 'y üzerinde'
        elif self.y == 0:
            return 'x üzerinde'
    # deconstructor metot : (yıkıcı metot) = obje ramdan silince cağirilir
    def __del__(self):
        print(f'{self} noktası düzlemden kaldırıldı')
        Nokta.sayac -= 1
        #Program bittikten hemen sonra oluşturulan nesneler otomatik olarak ram den kaldirilir
        # yani __del__ fonksiyonu otomatik de çalışır biz de çağırabiliriz


n1 =  Nokta(3,4)
n2 = Nokta(12,5)
# print((n1+n2).x , (n1+n2).y)

print(f'({n1.x},{n1.y}) + ({n2.x},{n2.y}) = ({(n1+n2).x}, {(n1+n2).y})')
#bir nesneye atanmayan değerler kullanıldıktan hemen sonra program bitmeden bellekten silinir
n3 = n1 + n2

print((n2.__gt__(n1))) # print(n2 > n1)  aynı anlama gelir

print(n1 < n2) # __gt__ fonksiyonu tanımlanmışsa '<' ifadesi __lt__ olmadan calisabilir ama
print(n1.__lt__(n2)) # compiler konsola "NotImplemented" çıktısı verir çünkü classımızda bu fonksiyonu tanımlamadık

print(n1)   #    __str__ metotu güncellenmeden önce konsoldaki çıktı: <__main__.Nokta object at 0x00000263688779D0>
print(n2)   # güncellendikten sonra kondolda n2 nin değerleri yazdırıldı


print(n1.__len__())
n3  = Nokta(0,0)
print(n3.__len__()) # print(len(n3)) ile aynı anlama gelir ancal bu kullanım şeklinde srtring döndürülemez o nedenle __len__
# fonksiyonunun return değerlerinde srting kullanmıyor olmalıyız

del n1
del n2
del n3

n11 = Nokta(1,1)
n12 = Nokta(1,2)
n13 = Nokta(1,3)
n14 = Nokta(1,4)
n15 = Nokta(1,5)
print("düzlemde bulunan nokta sayisi: ", Nokta.sayac) # neden konsolda 5 değil de 11 yazdı? : anlık oluşup silinenler nedeniyle constructor calisti ve
# sayac degeri arttı deconstructor'un icerisine sayac -= 1 yazarsak sistemde bulunan nesne sayısını anlık oluşup silinenler fazlalık yapmayacak şekilde
# öğrenebiliriz cünkü nesneye bağlanmadığı için kullanıldıktan hemen sonra silinen değerler silinirken de  sayac -= 1 çalışacaktır

print(20*'-',"PROGRAM BİTTİ", 20*'-')