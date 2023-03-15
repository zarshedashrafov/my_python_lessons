#12.02.2023
#Amaliyot_5
#Ro'yxatlar bilan ishlash (LIST)

ismlar=["Azamat", "Daler", "Shaxboz"]
print('Assalomu Alaykum '+ismlar[0]+' ishlaring yaxshimi.')
print(ismlar[-1]+ ' jura vaqtad hastmi?')
print('Salom '+ ismlar[-2]+ ' korot nag\'zmi doru darkor bud')
sonlar=[25, -9, 5.3, 9]
sonlar.append(3)
print(sonlar)
sonlar[0]=7
print(sonlar)
sonlar.insert(2, 8)
print(sonlar)
t_shaxslar=['Mirzo Ulug\'bek', 'At Termiziy', 'Abu Bakr Siddiq']
z_shaxslar=['Ilon Mask', 'Shavkat Mirziyoyev', 'Vladimir Putin']
print('Men tarixiy shaxslardan '+t_shaxslar[2]+' bilan, zamonaviy shaxslardan esa '+z_shaxslar[1]+' bilan suhbat qilishni istar edim')
frends=[]
frends.append('Azamat')
print(frends)
frends.append('Daler')
frends.append('Xushbaxt')
frends.append('Islom')
frends.append('Manucher')
frends.append('Fozil')
print(frends)
frends.remove('Fozil')
print(frends)
frends.append('Ikrom')
frends.insert(0, 'Shaxboz')
frends.insert(3, 'Farrux')
print(frends)
mehmonlar=[]
mehmonlar.append(frends.pop())
mehmonlar.append(frends.pop())
mehmonlar.append(frends.pop())
mehmonlar.append(frends.pop())
mehmonlar.append(frends.pop())
mehmonlar.append(frends.pop())
mehmonlar.append(frends.pop())
mehmonlar.append(frends.pop())
print(frends)
print(mehmonlar)
