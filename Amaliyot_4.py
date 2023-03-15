#11.02.2023
#Foydalanuvchi kiritgan sonning kvadrati va kubi.
#son=int(input('Istalgan son kiriting:\n'))
#son_kvadrati=f"{son} ning kvadrati {son**2} ga teng"
#son_kubi=f"{son} ning kubi {son**3} ga teng"
#print(son_kvadrati)
#print(son_kubi)

#Foydalanuvchini yoshini so'rab, uning tug'ilgan yilini aniqlash.
#yosh=int(input('Tug\'ilgan yoshingizni kiriting: '))
#tyil=2023-yosh
#print("Siz "+str(tyil)+" yilda tug'ilgansiz")

#Ikki soning ayirmasi, yig'indisi, ko'paytmasi va bo'linmasi
son_1=float(input("Birinchi soni kiriting: "))
son_2=float(input("Ikkinchi soni kiriting: "))
son_yig=f"{son_1}+{son_2}={son_1+son_2}"
son_ayr=f"{son_1}-{son_2}={son_1-son_2}"
son_kup=f"{son_1}*{son_2}={son_1*son_2}"
son_bul=f"{son_1}:{son_2}={son_1//son_2}"
print(son_yig)
print(son_ayr)
print(son_kup)
print(son_bul)
print(type(son_bul))
print(type(son_ayr))
