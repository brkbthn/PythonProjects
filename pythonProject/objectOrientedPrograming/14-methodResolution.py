class A:
    def metot1(self):
        print("method1-a sınıfı")
    def metot2(self):
        print("method2")

class B(A):
    def metot1(self):
     print("method1-b sınıfı")

    def metot3(self):
     print("method4")

class C(B):
    pass
x = B()
x.metot1() # b sınıfının method1 i çalışır, çağırılan metotu alt sınıftan en üs sınıf olan (object) sınıfına kadar arar ilk bulduğunu çalıştırır

print(B.mro()) #  [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

# java da çoklu kalıtım yokken pythonda vardır ancak coklu kalıtım uygularken kaltıtım sıralamalrının methot resolution'a uygun olması çelişki oluşmaması gerekir
# C->B->A iken A->B veya A->C vb olamaz (MRO) hatası alırız

