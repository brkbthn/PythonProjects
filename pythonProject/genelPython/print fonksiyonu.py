print("bauhan academy")
print("berk batuhan devran")

#kaçış karakteri
print("18\\12\\1999")
print("istanbul\nankara\nizmir") # \n = new line
print("Berk   Batuhan   Devran")
print("Berk\tBatuhan\tDevran")
print('batuhan')
print("berk\"batuhan") # \ ile kaçtık
print('batuhan\'ın melekleri')

# maematiksel ifadeler
print(5+9)
print(11-5)
print(15/3)
print(15//3)  # iki kez bölme işareti bölümün sadece tam kısmını gösterir
print(4*9)
print(15/2+(5*7)-9)

# Üs alma (**)
print(3**3)
print(2**10)
print(1024**0.1)

# Mod alma işlemi (%)
print(100%3)
print(101%4)
print(16%7.5)

#Özel durumlar
print(3.1+4.2)
print(0.1+2.2)


print("Berk Batuhan""  ""Devran")
print("Berk Batuhan","  ","Devran")
print("Berk Batuhan"+"  "+"Devran")
print("Batuhan "*3)

# r= raw string
print("C:\\Users\\batuhan")
print(r"C:\Users\batuhan")

print("Berk" "\n" "Devran")
print("Berk" +"\n"+ "Devran")
print(3*"Batuhan\n")

# ,end="..."
print("Berk Batuhan",end="")
print("DEVRAN")
print("Berk Batuhan",end="XXX")
print("DEVRAN")

# ,sep=""
print("Berk","Batuhan","Devran",sep="")
print("Berk","Batuhan","Devran",sep=" ")
print("Berk","Batuhan","Devran",sep="***")
print("Berk","Batuhan","Devran",sep="***")
print("Berk","Batuhan","Devran",sep="/")
print(19,19,1919,sep="/")
print("019","019","01919",sep="/")
print("019","019","01919",sep=":")

# *
print(*"BATUHAN")
print(*"BATUHAN",sep="/")
print(*"BATUHAN",sep=".")


# .format metodu

print("{}".format(10))
print("{}{}".format(10,25))
print("{} {}".format(10,25))
print("{}+{}={}".format(10,25,10+25))
print("{}+{}={}".format("berk","batuhan","devran"))

# comments    yorumlar
# single line comments  not= ctrl+/ maus ile seçilen kısmı yorum satırı yapar
#print("batuhan")

# multiline comments
"""
print(10+9)
print(14+5)
"""


# TODO print ile alakalı çalışılacak
# TODO hesap makinesi ile ilgii çalışılacak

# help fonksiyonu

help(print)
help(help)

