#Her generator iterable bir objedir
#yield => verim, ürün

def sayiUret():
    yield 1
    yield True
    yield "Berk Batuhan Devran"

print(sayiUret())
print(list(sayiUret()))


"""ORNEK1 """

#İLK 100 SAYİYİY ÜRETEN GENERATOR

def ilkBinSayi():
    i=0
    while i<=1000:
        yield i
        i+=1

sayilar = ilkBinSayi()
print(list(sayilar))

sayilar2 = ilkBinSayi()
print(next(sayilar2))
print(next(sayilar2))
print(next(sayilar2))


"""ORNEK2 """
#bİR DİZİNİN DEĞERLERİNİN İSTENİLEN KATINI ÜRETEN PROGRAM

def katiniUret(sayilar, kati):
    for sayi in sayilar:
        yield sayi * kati
liste = [2,3,5,6]
print(list(katiniUret(liste,4)))

#peki fonksiyon kullanmadan yapabilir miyiz
listeUcKati = (sayi*3 for sayi in liste)
print(listeUcKati)
print(tuple(listeUcKati))

listeSekizKati = tuple(sayi*8 for sayi in liste)
print(listeSekizKati)


"""Ornek3"""