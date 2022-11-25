osoba = ['Sofija', 25, 'plava', False]

for x in range (len(osoba)):
    print(osoba[x])

for osobina in osoba:
    print(osobina)

voce_i_povrce = ['jabuka', 'beli luk', 'crni luk', 'banana', 'mandarina','lubenica', 'krastavac']
for stavka in voce_i_povrce:
    print (stavka)
for i in range(len(voce_i_povrce)):
    print(voce_i_povrce[i])
for indeks, vrednost in enumerate(voce_i_povrce):
    print('Indeks:', indeks, 'Stavka:', vrednost)

automobili = ['Citroen','BMW','Opel','KIA','Yugo']

for x, y in enumerate(automobili):
   if len(y) == 3:
    print(y)
    #print('Pozicija:', x, 'Auto:',y)
automobili.append('Mercedes')
automobili[2] = 'Opel Astra'
automobili[3] = 'Kia Sporage'
print(automobili)
del automobili[3]
print(automobili)
automobili.remove('BMW')
print(automobili)

automobili[0]
broj_opela = 0 
for indeks in range(len(automobili)):
    if automobili[indeks] == 'Opel':
        print('Evo ga Opel')
        broj_opela += 1

print ('Imam ', broj_opela, 'na placu.')

automobili.clear()
print(automobili)







automobili = ['Mazda','BMW','Jeep','KIA','Audi']

automobili_akcija = []

for i in range(len(automobili)):
    if i == 1 or i== 2 or i== 3:
        automobili_akcija.append(automobili[i])
print(automobili_akcija)

automobili_akcija = automobili[1:4] 
print(automobili_akcija)








