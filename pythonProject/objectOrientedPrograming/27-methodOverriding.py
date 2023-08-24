
#method overridin = methodu geçersiz kılma


class Bina:
    def __init__(self, binaNo):
        self.binaNo = binaNo

    def adresSoyle(self):
        print("Bina no: ", self.binaNo)

class Daire(Bina):
    def __init__(self, daireNo, binaNo):
        self.daireNo = daireNo
        super.__init__(binaNo)
    def adresSoyle(self): #method overriding
        print("Bina no: ", self.binaNo, "Daire no: ", self.daireNo)

b1 = Bina(3)
d1 = Daire(3,5)

b1.adresSoyle()
d1.adresSoyle()



