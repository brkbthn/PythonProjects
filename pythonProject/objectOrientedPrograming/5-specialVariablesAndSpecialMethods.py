#Special Variables ve Special Methods (Magic)
class Araba:
    """
        Araba özellikleri görüntülenir ve güncellenir
    """

a1 = Araba()

print(__name__) #ana dosyada mı yoksa modül içerisinde mi çalıştığımızı öğrenmemizi sağlar
print(a1.__class__)#ilgili objenin hangi sınıfa ait olduğunu söyler   p--> property demektir yani değikendir  f-->funtion demektir
print(a1.__doc__) #class içerisindeki dökümantasyonu yazdırır dökümantasyan """    """ içerisine yazılır
