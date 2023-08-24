#Class kullanılarak oluşturulan oBjelerin özelliklerinin özelleştirlmesi

class Araba:
    #initialization(başlatma/kurucu metot/constructor)
    def __init__(self, marka, model, yil, bakim = True): #init üzerine crl+click yaparsan yaratılan nesneleri görebilirsin  // self oluştulmak istenen objeyi simgeler
        self.marka = marka
        self.model = model
        self.yil = yil
        self.bakim = bakim
        print("obje oluşturuldu") #init metodunu çağırdıysan içerisini mutlaka doldurmak zorundasın ya da pass dersin
    def ozellikleriniGoster(self):
        print("Özellikler;")
        print(self.marka, self.model, self.yil, end=" ")
        self.bakimDurumunuGoster()
    def bakimDurumunuGoster(self):
        if self.bakim == True:
            print("bakimi yalımistir")
        else:
            print("bakim yapilmamistir")

araba1 = Araba("mercedes", "cls400", 2022  )
araba2 = Araba("bmw" ,"5.30" ,2022, False )
print(araba2.marka)

araba1.ozellikleriniGoster()
araba1.ozellikleriniGoster()
print("*************************************")
araba1.bakimDurumunuGoster()
araba2.bakimDurumunuGoster()

#Her nesne heap memory de depolanır
#Objenin memory de kapladığı alanın oyutu barındırdığı atributelerin toplam boyutuna göre belirlenir