sayilar = [2,3,4,5,6]
# for sayi in sayilar:
#     print(sayi)
# print("-----------------------")
# for sayi in sayilar.__iter__():
#     print(sayi)  #aynı iş yapılıyor


sayilar = iter(sayilar)
# print(sayilar[0]) #diyemeyiz çünkü sayilar objesinin liste yapısı bozuldu
print(sayilar.__next__())
print(sayilar.__next__())
print(sayilar.__next__())
print(sayilar.__next__())

sayilar = [12, 13, 14, 15, 16]
for sayi in sayilar:
    print(sayi, sayilar[0], end=' -')
print('\n')
print(30*'*')

sayilarIter  =iter(sayilar)
sayi = sayilarIter.__next__()
print(sayi, sayilar[0])

sayi = sayilarIter.__next__()
print(sayi, sayilar[1])

sayi = sayilarIter.__next__()
print(sayi, sayilar[2])

#sayi = sayilarIter.__next__()
sayi = next(sayilarIter)#şeklinde de kullanılabilir
print(sayi, sayilar[3])

# Buradan da anlaşılacağı üzere for dögüsü bizim ona göderdiğimiz listenin ana yapısını
# bozmadan yeni bir iterable obje oluşturup unun izerinden next işlemi yapıyor

"""ORNEK1"""

#İLK 100 DOĞAL SAYİYİ VEREN SİNİF


class IlkYuzSayi:
    def __init__(self):
        self.sayi = 0
    def __iter__(self):
        return self #kendisini return ederek kendisini iterable hale getirdi
    def __next__(self):
        if self.sayi <=100:
            sayi = self.sayi #önce asyinin ilk değeri alınıyor
            self.sayi +=1 #sonra sayi değeri arttırılıyor (iterasyon mantığı)
            return sayi
        raise StopIteration #hata fırlatma


sayilar = IlkYuzSayi()

print(40*'-')

"""ORNEK2"""
#PRESENTATİON(sunum dosyası) sınıfının iterable olmasını sağlama
#Presentation sınıfı slides isminde bir field'i  vardır. Bu field liste halinde
#slideların isimlerini tutmaktadır
#slayt isimleri liste sonuna kadar döndürülmektedir



class Presentation:
    def __init__(self, slides:list=[]):
        self.slides = slides
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.slides):
            index = self.index
            self.index += 1
            return self.slides[index]
        raise StopIteration


p1 = Presentation(['giris', 'gelisme', 'sonuc'])
for slide in p1:
    print(slide)
#next(p1) #diyerek indexi kendimiz arttırarak for döngüsüne girmesini engelleyebiliriz veya istediğimiz indexten başlatabiliriz
p1.index = 0 #diyerek indexi yeniden sıfırlayabiliriz