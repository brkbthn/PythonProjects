#METHOD RESOLUTION ORDER

#Hiyerarşiye göre sıralama

class X:
    pass
class Y:
    pass
class Z:
    pass
class A(X,Y):
    pass
class B(Y,Z):
    pass
class M(B,A,Z): # çoklu kaltımda önce yazılan sınıfın önceliği daha fazladır
    pass


print(M.mro())