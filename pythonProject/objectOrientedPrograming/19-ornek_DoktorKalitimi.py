class Doktor:
    def __init__(self, isim, soyisim, maas, izinHakki):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.izinHakki = izinHakki

    def maasGuncelle(self, maas):
        self.maas = maas

    def bilgileriGoster(self):
        print(self.isim, self.soyisim, self.maas, self.izinHakki)

class Uzman(Doktor):
    def __init__(self, isim, soyisim, maas, departman, araba):
        super().__init__(isim, soyisim, maas, 30) #uzman doktorun izin hakkı sabit ve 30
        self.departman = departman
        self.araba =araba
    def arabaDegistir(self, araba):
        print("araba degistirildi")
        self.araba = araba

    def bilgileriGoster(self, hepsi:bool=True): # hepsi degiskeninin kullanim sekline dikkat et default olarak true ve yazilimciyi uyarmak için
        # boolean türünde olduğu belirtilmiş ancak boolean türünde deger gelmese de sistem hata vermez(default atama yapılmadıgını varsayalım=
        """

        :param hepsi: Objenin bütün özelliklerinin gösterilmesi için kullanilir
        :return:
        """
        if hepsi == True:
            super().bilgileriGoster()
        print(self.departman, self.araba)

class Pratisyen(Doktor):
    def __init__(self, isim, soyisim, maas, nobetGunleri:list):
        super().__init__(isim, soyisim, maas, 20) #pratisyen doktorun izin hakkı sabit ve 20
        self.nobetGunleri = nobetGunleri

    def bilgileriGoster(self):
        print(self.isim, self.soyisim, self.maas, self.araba, self.izinHakki, *self.nobetGunleri)

    def nobetListesiniGuncelle(self, nobetGunleri):
        print("nobet listesi guncellendi")
        self.nobetGunleri = nobetGunleri


u1 = Uzman(isim="Alperen Mehmet",soyisim="Yildiz", maas=99000,  araba="mercedes", departman="plastik cerrahi")
u2 = Uzman(isim="Zeynel Abidin",soyisim="Navgasin", maas=99000,  araba="audi", departman="dis ve cene cerrahisi")
u3 = Uzman(isim="Batuhan", soyisim="Basat", maas=99000, araba="bmw", departman="jinekoloji")

p1 = Pratisyen("Taner", "Aki", 12345, nobetGunleri= ['sali', 'cuma'])
p2 = Pratisyen("Pinar", "Tufan", 67890, nobetGunleri= ['pazartesi' , 'persembe'])


u1.bilgileriGoster(True)
u2.bilgileriGoster(False)
u3.bilgileriGoster(True)