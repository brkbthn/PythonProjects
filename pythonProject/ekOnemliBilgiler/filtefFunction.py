#filter() filtrelenen veriler döner (return bool olduğunda True ise filtrelenmis listeye değeri ekler)

sayilar = [1, 2, -3, 4, 6, -29, 7, -5, 55, 45]

def pozitifMi(sayi):
    return sayi > 0

pozitifSayilar = list(filter(pozitifMi,sayilar))
negatifSayilar = [sayi for sayi in sayilar if sayi not in pozitifSayilar]
negatifSayilar2 = list(filter(lambda sayi: sayi < 0, sayilar))

pozitifSayilar.sort(reverse=True)
print(pozitifSayilar)
print(negatifSayilar)
print(negatifSayilar2)