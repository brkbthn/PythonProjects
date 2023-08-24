

class Haber:
    def __init__(self, title, description, image):
        self.title = title
        self.description  =description
        self.image = image
    def bilgileriGoster(self):
        print(self.title, self.description, self.image)



x = Haber("lorem", "loram ipsum", "berkb.com/batus/images.png")
# print(x.title)
# # print(x.description)
# # print(x.image)
# x.bilgileriGoster()

class Spor(Haber):
    def __init__(self, title, description, image, video):
        super().__init__(title, description, image)
        self.video = video
    def bilgileriGoster(self):
        super().bilgileriGoster()
        print(self.video)
    def videoOynat(self):
        print("video oynatılıyor...")

# y = Spor("lorem", "loram ipsum", "berkb.com/batus/images.png", "video1.mp4")
# y.bilgileriGoster()


class Finans(Haber):
    def __init__(self, title, description, image, dovizKurlari):
        super().__init__(title, description, image)
        self.dovizKurlari = dovizKurlari

    def dovizKurlariniGoster(self):
        # print("guncel doviz kurlari: ", self.dovizKurlari)
        # print("guncel doviz kurlari: ", self.dovizKurlari.values())
        # print("guncel doviz kurlari: ", self.dovizKurlari.items())
        # print(tuple(self.dovizKurlari.items()))
        for dovizAdi in self.dovizKurlari:
            print(dovizAdi, ":", self.dovizKurlari[dovizAdi])
        print("--------------------------")
        for dovizAdi, dovizDegeri in self.dovizKurlari.items():
            print(dovizAdi, ":", dovizDegeri)

    def dovizKurlariniGuncelle(self, guncel):
        self.dovizKurlari = guncel

    def bilgileriGoster(self):
        super().bilgileriGoster()
        print(self.dovizKurlari)

s1 = Spor(title="Mac beraberlikle sonuclandi", description="Macin berabere bitmesi ardından yapilan aciklama begenilmedi", image="mac.jpg", video="futbol.mp4")
f1 = Finans(title="ekonomi durgun", description="koronavirüs sebebiyle tüm dünyada ekonomik durgunluk devam ediyor", image="ekonomi.png", dovizKurlari= {'dolar': 18, 'euro': 18.5})

s1.bilgileriGoster()
f1.bilgileriGoster()

f1.dovizKurlariniGoster()
f1.dovizKurlariniGuncelle({'dolar': 18, 'euro': 18.5, 'sterlin':20})
f1.dovizKurlariniGoster()

