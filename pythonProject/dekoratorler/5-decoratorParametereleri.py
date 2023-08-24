def do_twice(func):
    def wrapper_do_twice(*args, **kwargs): #değişken sayida parametre gönderme sorunu çözüldü
        return func(*args, **kwargs)
        #func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def hello():
    print("hello")

@do_twice
def greet(msg):
    print("hello ", msg)

@do_twice
def return_greeting(name):
    print("greeting func")
    return "hello, {}".format(name)

# hello()
# greet("batuhan")
return_greeting("berk")
print(return_greeting("berk")) #return edilen değeri alamadık (None) dedi, bu sorunu ortadan kaldırmak için wrapper içinde
#fonksiyonu return ettirmeliyiz