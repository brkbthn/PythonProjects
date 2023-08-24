"""CONTROL STATEMENTS(İF ELİF ELSE)"""
#Indentetion(GİRİNTİ)
# İf li ifadeden sonra : koyulmalıdır alt satırda kod en az bir tane boşluk bırakılarak yazılmalıdır
# if den zonra yazılan kod dizisi aynı hizada olmalıdır
# eğer if in hemen altındaki satıra kod yazılmayacaksa pass yazılarak hata almak engellenmelidir


if False:
    print('2. if blogu')

sayi = 5

if sayi>0:
    print(sayi,"pozitiftir")
if sayi<0:
    print (sayi,"negatiftir")
if sayi == 0:
    print(sayi, "nötrdür")


yaş = int(input("lütfen yaşınızı giriniz"))

if yaş>18:
    print("reşitisiniz")
if yaş<18 and yaş>0:
    print("reşit değilsiniz")
if yaş<0:
    print("lütfen yaşınızı doğru giriniz")

sayı = 8
sonuç = sayı % 2
if sonuç==0:
    print("sayı çifttir")
if sonuç==1:
    print("sayı tektir")

if sonuç == 0:
    print("sayı çifttir")
else: # sonucun 0 olmadığı her durum
    print("sayı tektir")

if yaş>=18:
    print("reşitsiniz")
else:
    if yaş>0:
        print("reşit değilsiniz")
    else:
        print("lütfen yaşınızı doğru giriniz")

vize = 49
final = 50
if final>=50:
    ort = vize*0.4+final*0.6
    if ort>50:
        print("hadi yine iyisin")
    else:
        print("başka bahara koçum")

yaş = 22


if yaş>18:
    print("reşitsiniz")
elif yaş>0 and yaş<=18:
    print("reşit değilsiniz")
else:
    print("lütfen yaşınızı doğru giriniz")


"""Örnek"""
#Kullanıcıdan 1 ve 4 arasında bir tamsayı alan ve bu sayının  nasıl okunduğunu gösteren programı yazınız

sayı = int(input("lütfen 1-4 arasında bir rakam giriniz"))
if sayı==1:
    print("bir")
elif sayı==2:
    print("iki")
elif sayı==3:
    print("üç")
elif sayı==4:
    print("dört")
else:
    print("lütfen istenilen aralığa uygun bir sayı giriniz")

    """Örnek"""
# Girilen ayın hangi mevsimde olduğunu gösteren programı yazınız

ay = input("lütfen bir ay ismi giriniz")
ay = ay.replace('I','ı')
ay = ay.replace('İ','i')
ay = ay.lower()
if ay=="aralık" or ay=="ocak"or ay=="şubat":
    print("kış")
elif ay=="mart" or ay=="nisan" or ay=="mayıs":
    print("ilkbahar")
elif ay=="haziran" or ay=="temmuz" or ay=="ağustos":
    print("yaz")
elif ay=="eylül" or ay=="ekim" or ay=="kasım":
    print("sonbahar")
else:
    print("lütfen bir ay ismi giriniz")

"""örnek"""
# 6 katlı bir binanın her katında 3 daire bulunmaktadır. Girilen daire numarasına gre o dairenin kat numarasını veren programı yazınız.

daireno = int(input("lütfen 1-18 arası bir sayı giriniz"))
if daireno==1 or  daireno==2 or daireno==3:
    print(1)
elif daireno==4 or  daireno==5 or daireno==6:
    print(2)
elif daireno==7 or  daireno==8 or daireno==9:
    print(3)
elif daireno==10 or  daireno==11 or daireno==12:
    print(4)
elif daireno==13 or  daireno==14 or daireno==15:
    print(5)
elif daireno==16 or  daireno==17 or daireno==18:
    print(6)
else:
    print("lütfen isneilen aralığa uygun bir sayı giriniz")


"""örnek"""
#pilotluk sınavında adayların ilk aşamayı geçebilmeleri için kadınların 1.60 erkeklerin 1.70 boy sınırını geçmeleri istenmektedir..

boy= int(input("lütfen boyunuzu giriniz"))
cinsiyet= str(input("lütfen cinsiyetinizi giriniz"))
if cinsiyet == "Kadın" :
    if boy>=160:
        print("Mülakatı geçtiniz")
    else:
        print("Elendiniz")
elif cinsiyet == "erkek" :
    if boy>=170:
        print("mülakatı geçtiniz")
    else:
        print("elendiniz")

"""Örnek"""
#Kullanıcıdan aldığı paket sayısına göre ödeyeceği tutarı gösteren programı yazınız.
#Bir toptan satış mağazası
#  100 paket ve üzeri için satın alımda paket başına 10 tl
#  61-99 paket arası satın alımda paket başına 12 tl
#  30-60 paket arası satın alımda oaket başına 15 tl
#  1-29 paket arası satın alımda paket başına 20 tl  alıyorsa... programı yazınız.

paketsayısı= int(input("kaç paket alacaksınız?"))
toplamtutar= None
if paketsayısı>=100:
    toplamtutar = paketsayısı*10
elif paketsayısı>=61:
    toplamtutar = paketsayısı*12
elif paketsayısı>=30:
    toplamtutar = paketsayısı*15
elif paketsayısı>=1:
    toplamtutar = paketsayısı*20
else:
    print("lütfen adam gibi bir sayı giriniz")


if toplamtutar is not None:
    print("Ödemeniz gereken toplam tutar {}".format(toplamtutar))
else:
    print("ödemeniz gereken biir tutar bulunmamaktadır")
    
### Kullanıcı 3 kenar bilgisi girmeli ve eğer bu 3 kenarla bir üç kenarla bir üçgen çizilebiliyorsa
# bu üçgenin, ikizkenar ya daçeşitkenar olup olmadığını konsolda gösteren programı yazınız.

kenar1, kenar2, kenar3 = int(input("lütfen kenar 1 uzunluğu giriniz")), int(input("lütfen kenar 2 uzunluğu giriniz")), int(input("lütfen kenar 3 uzunluğu giriniz"))



if abs(kenar1-kenar2) < kenar3 and kenar3 and kenar3 < kenar1+kenar2:
   if kenar1 == kenar2 and kenar1== kenar3:
       print("Eşkenar Üçgen")
   elif  kenar1 == kenar2 or kenar2== kenar3 or kenar1==kenar3:
       print("İkizkenar üçgen")
   else:
       print("Çeşitkenar üçgen")
else:
    print("Bu üç kenar ile bir üçgen çizilemez")

# Bir önecki örneğin set veri tipi ile çözülmesi

kenar1, kenar2, kenar3 = int(input("lütfen kenar 1 uzunluğu giriniz")), int(input("lütfen kenar 2 uzunluğu giriniz")), int(input("lütfen kenar 3 uzunluğu giriniz"))
kenarlar = set([kenar1, kenar2, kenar3]) # set bir değeri iki defa depolamaz
print(kenarlar)
if abs(kenar1-kenar2) < kenar3 and kenar3 and kenar3 < kenar1+kenar2:
    if len(kenarlar)==1:
        print("eşkenar üçgen")
    elif len(kenarlar)==2:
        print("ikizkenar üçgen")
    else:
        print("çeşitkenar üçgen")