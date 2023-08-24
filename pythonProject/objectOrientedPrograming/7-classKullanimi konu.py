#Konu- Objelerin güncellenmesi ve karşılaştırılması

#Her öğrencinin ad, soyad ve numara bilgisi vardır
#Numaralar 8 haneli olacaktır
#Numaraların ilk 2 hanesi okula girdiği yılı sonraki 3 hanesi bölüm numarasını son 3 hanesi de öğrenci kayıt sırasını temsil etmektedir
#isim ve soyisim bilgisi girlmek zorundadır, defauşt numara 00000000 olmalıdır
#isim ve numara bilgisi güncellenebilmelidir
#Karşılaştırma işlemi 2 öğrencinin okula kayıt yaptırdığı seneler üzerinden olacaktır
#Karşılaştırılan öğrencilerin birbirlerine göre okula önce ya da sonra girdiği bilgisi verilecektir

class Ogrenci:
    def __init__(self, isim,  soyisim, numara = "00000000"):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
    def guncelle(self, isim="", soyisim="", numara=""): # crtl+/ ile toplu yorum atıp kaldırabilirsin
        if isim !="":
            self.isim = isim
        if soyisim !="":
            self.soyisim
        if numara != "":
            self.numara = numara
    def karsilastir(self, digerOgrenci):
        if int(self.numara) == 0 or int(digerOgrenci.numara) == 0:
            print("bir veya birden fazla öğrencinin numarası bulunmamaktadır.")
        else:
            o1numara = int(int(self.numara)/1000000) # ikinci kez int yapmamızın sebebi bölme işlemi sonrasında otomatik olarak floata cast olması
            o2numara = int(int(digerOgrenci.numara)/1000000)

            if o1numara == o2numara:
                print("{} isimli ogrenci {} isimli ogrenciyle aynı sene okula girmiştir".format(self.isim,digerOgrenci.isim))
            elif o1numara > o2numara:
                print("{} isimli ogrenci {} isimli ogrenciden sonra okula girmiştir".format(self.isim, digerOgrenci.isim))
            else:
                print("{} isimli ogrenci {} isimli ogrenciden sonra okula girmiştir".format(digerOgrenci.isim, self.isim))





ogrenci1 = Ogrenci("Berk Batuhan", "Devran", "21052610")
ogrenci2 = Ogrenci("Mehmet", "Kabakçı", "12345678")

ogrenci1.karsilastir(ogrenci2)

ogrenci2.isim = "asfafasdsg"
print(ogrenci2.isim) #şeklinde güncelleme şimdilik yapılabilir

ogrenci1.sinif = "3" #şeklinde yeni özellik de eklenebilir, model dışına çıkabildik
print(ogrenci1.sinif)