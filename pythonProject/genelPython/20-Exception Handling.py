"""Errors"""
#Exceptiın (olağandışılılık, istisna)
#Handling(İşleme, idare etme)
#1-)Compile time error(program çalışmadan(derleme(enterpreter derler)) hatanın çıkması)
    #Syntactial Errors
#2-)Logical Error
    #Wrong output
#3-)Run time Error(program çalışırken hatanın çıkması)
    #Divide by zero

#statement
    #Normal(warning, programın çalışmasını engellemez)
    #Critical (error, program çalışmaz)

"""pythonda karşılaşılabilcek hatalar"""

#ValueError (değer hatası)

try:
    sayi1 = int(input("lütfen bir tamsayı giriniz"))
    sayi2 = int(input("lütfen bir tane daha tamsayı giriniz"))
    #raise Exception
    #raise ValueError
    print(f'{sayi1}/{sayi2}={sayi1/sayi2}') #raise ValueError
#except Exception: diyerek genel bir hata alma işlemi de yapılabilir
# except (ZeroDivisionError, ValueError): iki veya daha fazla hatayı parantez içinde de alabiliriz
#     print("lütfen tam sayı giriniz ve sıfıra bölme işlemi yapmayınız")
except ValueError:
    print("Lütfen tamsayı giriniz")
except ZeroDivisionError:
    print("hiçbir reel sayı sıfıra bölünmez lütfen 2. sayıyı sıfırdan farklı giriniz")
except Exception:
    print("bir sorunla karşılaştık")

"""Exception bilgisi görüntüleme ve finally anahtar keliesi"""

rakam1 = 8
rakam2 = 0

try:
    #critical statement oluştuğu anda Throw an exception(bir hata fırlatılır )
    print(rakam1/rakam2)
except Exception as exc: #exc:exception yerine errorun e si veya hatanın h'sini kullanabilirisin
    print("sıfır ile bölme işlemi yapılamaz. Çıkan hata: ", exc)
# eğer biz try buloğundan önce bir dosya çmışssak ve hata almışssak dosya açık kalmış demektir bu durumda
# sonuç olarak yapılacak işlemlerin tanımlanabilmesi için finally anahtar kelimesi kullanılır
finally:
    print("dosya kapatıldı")



"""Programımıza aykırı  durumları handle etme"""

def faktoriyel(n):
    if n<0 or type(n) != int:
        raise ValueError("bir sayının faktoriyelini almak için o sayının doğal sayı olması gerekir")
    if n==0:
        return 1
    return n * faktoriyel(n-1)

#peki yukarıda yakaladığımız hatayı nasıl handle ederiz. Burada zaten hatayı yakalayıp valueError orlarak not düştüğümüz için
# Exception as e dedimizde kendi yazdığımız not karşımıza gelecktir
try:
    print(faktoriyel(5.5))
except Exception as e:
    print(e)


"""DURUMA GÖRE KENDİ EXCEPTİON'IMINIZ NASIL FIRLATIRIZ """

sayi = 500
if sayi > 100:
    raise Exception("sayı 100'den büyüktür") #throw exception

isim = "batuhan"
if not type(isim) is str:
    raise TypeError("string değer değildir")