
print(int.__add__(7,8))#toplama
print(float.__add__(5.6,6.7))#toplama

print(int.__sub__(10,2))#çıkarma
print(int.__mul__(6,7))#carpma

print(int.__truediv__(16,9))
print(int.__floordiv__(16,9))

print(int.__divmod__(10,3)) # (tam kısım, kalan kısım)

print(str.__mul__("*", 30))

print([1,2,4].__len__()) #liste uzunluğunu verir

print(int.__ge__(5, 3)) #büyüklük karşılaştırma  greater than  (>= operatörü)
print(int.__ge__(5, 13))
print(int.__ge__(13, 13))

print(int.__lt__(4,6)) # (<=)


print(float.__le__(12.3, 14.5)) # lower or equal  (<=)