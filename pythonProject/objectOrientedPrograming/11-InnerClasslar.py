class Musteri: #outhor class (dış sınıf)
    def __init__(self, musteriNo, isim, soyad, bakiye, hesapTuru):
        self.musteriNo = musteriNo
        self.isim = isim
        self.soyad = soyad
        # self.bakiye = bakiye
        # self.hesapTuru  =hesapTuru
        self.hesap = self.Hesap(bakiye, hesapTuru) # inner classı ana classın bir parçası haline getirdik
    def bilgileriGoster(self):
        print(self.musteriNo, self.isim, self.soyad)
        # self.hesap.bilgileriGoster()

    class Hesap: #inner class   veritabanı işlemlerindeki normalizasyona benzer mantık
        def __init__(self, bakiye = 0, hesapTuru = "hesap türü tanimlanmdi"):
            self.bakiye = bakiye
            self.hesapTuru = hesapTuru
        def bilgileriGoster(self):
            return self.bakiye, self.hesapTuru


m1 = Musteri(1, "Berk Batuhan", "Devran", 40000, "tl")
m2 = Musteri(2, "Mehmet", "Kabakcı", 120000, "dolar")

m1.bilgileriGoster()
m2.bilgileriGoster()

#sadece iç sınıfın bilgilerini görmek için
print(m1.hesap.bilgileriGoster()[0])
print(m1.hesap.bilgileriGoster())

print("1.müsterinin hesap bilgileri: ", m1.hesap.bilgileriGoster())
print("2.müsterinin hesap bilgileri: ", *m2.hesap.bilgileriGoster()) # * ile unpack ettik

# direkt müsteri nesnesi üzerinden hesap bilgilerine ulaşıp konsola bastirabiiliriz
print(m1.hesap)
print(m1.hesap) # ikisi de bir nesne dir
print(m2.hesap.hesapTuru)
print(m2.hesap.bakiye)


#Müşteri tanımlamadan hesap açılabilir mi?

hesap3 = Musteri.Hesap(5000, "euro")
print(hesap3.bilgileriGoster()) #evet açılabilir