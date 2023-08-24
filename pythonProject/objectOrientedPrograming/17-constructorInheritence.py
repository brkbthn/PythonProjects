class D:
    def __init__(self):
        print("D constructor")

    def metot1(self):
        print("D metot1")

    def metot2(self):
        print("D metot2")

class E(D):
    def __init__(self): # eğer e için bir constuctor oluşturmazsak E den bir nesne oluşturulurken D nin(bir üst sınıfın) constructor'u calistirlir E de varsa o calistirlir
        super().__init__() #bu şekilde bir üst sınıfın da constructoru calistirilir
        print("E constructor")

    def metot1(self):
        print("E metot1")

