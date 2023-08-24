def toplama(a,b):
    return a+b

def carpma(a,b):
    return a*b

def islem(f1, f2, islemAdi):
    if islemAdi == "toplama":
        print(f1(2,3))
    elif islemAdi == "carpma":
        print(f2(2,4))
    else:
        print("geçersiz deger")


islem(toplama, carpma, "carpma")
islem(toplama, carpma, "carpmaa")