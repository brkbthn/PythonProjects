#hazırlamış olduğunuz bir fonksiyondan önce veya sonra otomatik olarak çalistirilmasini istediğiniz bir fonksiyon varsa decorator kullanabilisiniz

def selamlama(fn):
    def wrapper(ad):
        print("hosgeldiiniz")
        fn(ad)
        print("gorusmek uzere")
    return wrapper

@selamlama
def gunaydin(ad):
    #print("hosgeldiiniz")
    print("günaydın benim adım ", ad)
    #print("gorusmek uzere")

@selamlama
def iyiGunler(ad):
    #print("hosgeldiiniz")
    print("iyi günler adım ", ad)
    #print("gorusmek uzere")

#Decorator kullanmdadan
# g = selamlama(gunaydin) # g = wrapper()
#
# g()
#
#
# ig = selamlama(iyiGunler) # ig = wrapper()
#
# ig()


#Decorator ile @....
#eğer içlerinde tekrar olduğu için decorator kullandığımız fonksiyonlarda parametre kullanırsak wrapper ve
# wrapper içinde parametere olarak gönderdiğimiz fonksiyon için de kullanmalıyız
gunaydin("batuhan1")
iyiGunler("batuhan2")


