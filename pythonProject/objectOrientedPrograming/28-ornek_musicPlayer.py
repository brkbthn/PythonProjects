
class MusicPlayer:
    #ses seviyesi [0-10]
    def __init__(self, durum:bool = False, sarkiListesi = [], ses = 0): #defaul değeri olmayan parameetreler default değeri olanlardan daha önce yazılmak zorundadır
        self.durum = durum
        self.sarkiListesi = sarkiListesi
        self.ses = ses

    def bilgileriGoster(self):
        print(f'Durum: {"Tv açık" if self.durum == True else "TV kapalı"}, {self.sarkiListesi}, {self.ses}')
        #{"Tv açık" if self.durum == True else "TV kapalı"} tv acık yaz eğer self.drurum true ise, else yaz tv.durum kapalı ise

    def sesArtir(self):
        if self.ses < 10:
            self.ses +=1
            print("ses seviyesi guncellendi, son durum: ", self.ses)
        else:
            print("max seviye: ", self.ses)

    def sesAzalt(self):
        if self.ses < o:
            self.ses -= 1
            print("ses seviyesi guncellendi, son durum: ", self.ses)
        else:
            print("min seviye: ",self.ses)

    def sesKapat(self):
        self.ses = 0
        print("ses seviyesi: ",self.ses)

    def powerOnOf(self):
        # if self.durum:
        #     self.ses = False
        #     print("Music Player kapatıldı")
        #
        # else:
        #     self.ses = True
        #     print("Music PLyer açıldı")

        self.durum = not self.durum  # daha şekil:)

    def sarkiListesiOlustur(self, sarkiListesi:list):
        self.sarkiListesi = sarkiListesi

    def sarkiListesiGoruntule(self):
        # print("sarkilistesi: ", *self.sarkiListesi)
        print("sarkilistesi: ",  self.sarkiListesi if len(self.sarkiListesi) > 0 else "sarkı yok")

    def sarkiListesiGuncelle(self, sarkiListesi):
        secenek = input(print("onceki sarki listesi temizlensin mi? 1=Evet , 2=Hayır"))
        if secenek==1:
            self.sarkiListesi = sarkiListesi
        elif secenek == 2:
            pass
        else:
            print("lutfen gecerli bir rakam sayi giriniz...")

    def sarkiListesiniSil(self):
        self.sarkiListesi = []

    def __len__(self):
        """
        Sarkı listesinde kac tane sarki oldugunu soyler
        :return: sarki listesindeki sarki sayisi
        """
        return len(self.sarkiListesi)

    def __gt__(self, other):
        """
        iki müzik oynatıcısında bulunan şarkı listelerindeki şarkı sayılarını kıyaslar
        :param other:
        :return:
        """
        if len(self.sarkiListesi) > (other.sarkiListesi):
            return True
        else:
            return False

    def __del__(self):
        print("music player sistemden kaldirildi")

m1 = MusicPlayer(True, ['a', 'b'], 1)
m2 = MusicPlayer(['c', 'd'], 5)
m3 = MusicPlayer(False, ses = 2,  sarkiListesi = ['c', 'd','R','t'])
m4 = MusicPlayer(durum = False, ses = 9, sarkiListesi = ['x', 'y']) # positional arguman her zaman keyword argumandan sonra gelir

m1.bilgileriGoster()
m2.bilgileriGoster()
m3.bilgileriGoster()
m4.bilgileriGoster()

m4.sesArtir()
m4.sesArtir()

m4.sarkiListesiGoruntule()

# __len__ magic methodunu güncelledik şimdi iki farklı şekilde çağıralım
print(len(m3))
print(m1.__len__())

# __gt__ magic methodunu güncelledik şimdi iki farklı şekilde çağıralım
print(m1 > m2)
print(m1.__gt__(m2))


#__lt__ magic methodunu güncellemesek bile __gt__ nedeniyle "<" operatörü çalişir ama fonksiyonu çağirisak sistem tanımlı olmadığını belirtir

