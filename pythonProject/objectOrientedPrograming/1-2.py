#Object oriented programing
#Her şey bir objedir
#Her objenin attributeleri vardır (attribute, property, özellikler)(isim, yaş, göz rengi...)
#Her objenin Behaviour'ları vardır(yürümek, koşmak ...)

#Object oriented dışında
"""
Functional Programing
Procedure oriented Programing => c dili
"""
#Mantığı mevcuttur


#Built_in types (Python içersinde default olarak gelen tipler)

a = 5
print(type(a))
print(type(5))
print(id(a))
print(id(5))
#python ram'in heap bölgesinde a yı tutup 5 i referance eder. 5 zaten defaultta vardır.


b = 5.5
print(type(5.5))
print(type(b))
print(id(5.5))
print(id(b))

c = "naber"
print(c)
print("naber")
print(type(c))
print(type("naber"))
#string havuzunda olan bir elaman yeniden oluşturulmaz refere edilir

n = None
print(None)
print(n)
print(id(n))
print(id(None))

k = True
print(id(True))
print(id(n))

t = (1,2,3)#tuple
print(t)
print(id(t))
print(id((1,2,3)))
#tuple değiştirilemez bir nesne olduğu için aynı id ile geliyor

l = [1,2,3,4]
print(id([1,2,3,4]))
print(id(l))
#liste değiştirilebilir bir veri türü olduğu için farklı bir id ile depolanıyor


d = {1:"berk", 2:"batuhan"}
print(id({1:"berk", 2:"batuhan"}))
print(id(d))
#dictionary değiştirilebilir bir veri türü olduğu için farklı bir id ile depolanıyor

s  = {1,2,3,45,45,45}
print(s)
print(id({1,2,3,45,45,45}))
print(id(s))
#set değiştirilebilir bir veri türü olduğu için farklı bir id ile depolanıyor