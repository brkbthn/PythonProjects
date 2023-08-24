class Hayvan:

    def seslen(self):
        print("hayvanlar ses cıkartır")

class Kedi(Hayvan):
    def seslen(self):
        print("MİYAVV")

class Kopek(Hayvan):
    def seslen(self):
        print("HAV HAV")

kedi1 = Kedi()
kopek1 = Kopek()

kedi1.seslen()
kopek1.seslen()