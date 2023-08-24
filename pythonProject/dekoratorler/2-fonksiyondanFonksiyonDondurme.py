def usalma(number):

    def inner(power):
        return number ** power
    return inner

two = usalma(2) #usalma'nın number değerinde 2 döndürülen fonksiyonun içindeki number değeridir
print(two(2))



def yeki_Sorgula(page):
    def inner(role):
        if role == "admin":
            return "{} rolunun {} sayfasına ulasabilir.".format(role, page)
        else:
            return "{} rolun {} sayfasına ulaşamaz.".format(role, page)
    return inner

user1 = yeki_Sorgula("product manager")
print(user1("admin"))



def islem(islemAdi):
    def toplam(*args):
        sonuc = 0
        for i in args:
            sonuc += i
        return sonuc

    def carpma(*args):
        sonuc = 1
        for i in args:
            sonuc *= i
        return sonuc

    if islemAdi == "toplama":
        return toplam
    else:
        return carpma

toplamaIslemi = islem("toplama")
print(toplamaIslemi(2,3,4,5,6))
