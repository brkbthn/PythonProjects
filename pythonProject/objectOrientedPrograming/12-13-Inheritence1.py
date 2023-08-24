# Inheritence

# Bir sınıfın başka bir sınıfta bulunan değişken ve davranışları kullanmasıdır

print(issubclass(list,object))# list sınıfı object sınıfının bir alt class ı mıdır

print(isinstance(5.5, int)) #bir nesnenin bir class a ait olup olmadığını sorgulamaya yarar
print(isinstance(4.4, object))
print(isinstance(4, object))

class A:
    def metot1(self):
        print("method1")
    def metot2(self):
        print("method2")

class B(A):
    def metot3(self):
     print("method3")

    def metot4(self):
     print("method4")


x = A()
y = B()

print(x)
print(y)

y.metot1()
y.metot2()
y.metot3()
y.metot4()
