#13.02.2023
#Amaliyot_6 Ro'xtlar ustida amallar
davlatlar=['O\'zbekiston', 'Xitoy', 'AQSH', 'Germaniya', 'Singapur', 'Rossiya', 'Ispaniya', 'Meksika']
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
juft_sonlar=list(range(120,1200,2))
#print(juft_sonlar)
print(sum(juft_sonlar))
print(max(juft_sonlar)-min(juft_sonlar))
print(len(juft_sonlar))
print(juft_sonlar[:20])
print(juft_sonlar[260:280])
print(juft_sonlar[520:])

taomlar=['Shurva', 'Osh', 'Quvurilgan baliq', 'Qovurilgan tuxum', 'Shirchoy']
print(taomlar)
nonushta=taomlar[:]
print(nonushta)
nonushta.remove('Osh')
nonushta.remove('Shurva')
nonushta.remove('Quvurilgan baliq')
nonushta.append('Blinchik')
nonushta.append('Shirbrinch')
print(taomlar)
print(nonushta)
nonusha=tuple(nonushta)
print(nonushta)
print(type(nonushta))
nonushta[0]='qaymoq va non'
print(nonushta)
son=(1, 2, 5)
      
