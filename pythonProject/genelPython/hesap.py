from math import pi
def topla(a,b):
    """
    iki değerin toplanmasını sağlar
    :param a: ilk sayı
    :param b: ikinci sayı
    :return:
    """
    return a+b
def daireCevreHesapla(r):
    """
    Bir dairenşn çevresini hesaplamaya yarar
    :param r: Darirenin yarıçapı
    :return:
    """
    return 2*pi*r
def daireAlanHesapla(r):
    """
    Bir dairenin alanını hesaplamaya yarar
    :param r: Dairenin yarıçapı
    :return:
    """
    return pi*r*r
if __name__ == "__main__":
    print("hesap modülünün ana bloğu burasıdır")