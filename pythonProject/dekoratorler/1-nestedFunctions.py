def greeting(name):
    print('hello', name)

# greeting("ali")
# print(greeting)

sayHello = greeting

print(sayHello) #<function greeting at 0x0000023971C6E430>
print(greeting) #<function greeting at 0x0000023971C6E430>    ikiside aynı adreste

sayHello("ali") #çalıştı
del sayHello
greeting("ali") #sayHallo zaten greeting fonksiyonunu referans ettiği için asıl fonksiyon çalışmaya devam eder


#encapsulation
def outer(num1):
    print("outer")
    def inner_increment(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)

outer(10)
#içteki fonksiyon doğrudan çağırılamaz, derleyici not defind hatası verir


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if not number >= 0:
        raise ValueError("your value must be natural number")
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * factorial(number-1)
    return inner_factorial(number)


try:
    print(factorial("4"))

except Exception as ex:
    print(ex)

