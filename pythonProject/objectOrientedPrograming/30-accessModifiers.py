class sporcu():
    def __init__(self, ad, brans, altin, gumus, bronz):
        self.ad = ad
        self.brans = brans
        self.__altin = altin #private = artık bu bilgi doğrudan erişilebilir değildir getter setter kullanılabilir
        self._gumus = gumus #protected = sadece aynı pakaet içerisinden erişim var
        self.bronz = bronz  #public = farklı paketler tarafınfan erişilebilir
    def atlet_bilgisi(self):
        return "sporcu adı : {}, Branşı : {}".format(self.ad , self.brans) #formatın içindeki değerleri self ile getirdiğini unutmamalsın
    def getAltin(self):
        altınSayisi = self.__altin
        return "altın madalya sayısı: {}".format(altınSayisi)

atlet1 = sporcu("batuhan", "100 metre", 2, 3, 9)
print(atlet1.ad, atlet1.brans)
print("bronz madalya sayisi: ", atlet1.bronz) #public = bronz
print("gumus madalya sayisi: ", atlet1._gumus) # '_' cekmeden intelicence da gözükmedi
print(atlet1.getAltin())