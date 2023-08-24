# Telefon sınıfını tanımla ve CRUD(create, read, update, delete) işlemlerini içerisine yerleştir

class Telefon:
    def __init__(self, marka, model, isletimSistemi, onTanimliProgramlar):
        self.marka = marka
        self.model = model
        self.isletimSistemi = isletimSistemi
        self.onTanimliProgrmlar = onTanimliProgramlar
    def bilgileriGoster(self):
        print(self.marka, self.model, self.isletimSistemi, self.onTanimliProgrmlar)

    def onTanimliProgramlariGoster(self):
        print(*self.onTanimliProgrmlar) # * sayesinde liste içindeki bütün elemanlar gösterilir

    def onTanimliProgramEkle(self, program):
        self.onTanimliProgrmlar.append(program)
        print("bir program eklendi")
    def onTanimliProgramGuncelle(self, program, new):
        self.onTanimliProgrmlar[self.onTanimliProgrmlar.index(program)] = new
        print("bir program güncellendi")
    def onTanşmlşProgramSil(self,program):
        self.onTanimliProgrmlar.remove(program)
        print("bir program silindi")


t1 = Telefon("samsung", "s20fe", "android", ["rehber", "galeri","kamera"])
t2 = Telefon("iphone", "7s", "ios", ["rehber", "galeri","facebook"])
t3 = Telefon("samsung", "s21", "android", ["mesajlar", "galeri","kamera"])
t4 = Telefon("huawei", "matepro", "huwos", ["rehber", "ayarlar","kamera"])
t5 = Telefon("xiaomi", "mi12", "android", ["instagram", "galeri","kamera"])

t1.bilgileriGoster()
Telefon.bilgileriGoster(t1) #buraya dikkat et
t1.onTanimliProgramlariGoster()
t1.onTanimliProgramEkle("navigasyon")
t1.onTanimliProgramGuncelle("rehber", "ayarlar")
t1.onTanimliProgramlariGoster()
t1.onTanşmlşProgramSil("kamera")
t1.onTanimliProgramlariGoster()