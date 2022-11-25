#          0        1      2      3 
osoba = ["Sofija", 20, "plava", True]
print (osoba)

print(osoba[0])
print("Godine:", osoba[1])

automobili=["Opel","Citroen","Mercedes"]
print(automobili[1])
#       012345
kurs = 'python'

print(kurs[0])
print(kurs[1])
print(kurs[2])
print(kurs[3])
print(kurs[4])
print(kurs[5])

duzina = len(kurs)

for x in range(len(kurs)):
    print("Na poziciji:",x ,kurs[x])

ustanova = "IT Academy"





for indeks in range(len(ustanova)):
    print(ustanova[indeks])

primer = 'zadatak1'

for k in range (len(primer)):
    print(primer[k],end="")

print('')
    

broj_karaktera = len(primer)
indeks = 0

while indeks < broj_karaktera:
    print(primer[indeks])
    indeks += 1 

print('asdf')

korisnicko_ime = 'admin'
uneto_kor_ime = input("Unesi korisnicko ime:").lower()


if korisnicko_ime == uneto_kor_ime.lower():
    print('Dobrodosli')
else:
    print('Pogresni podaci')
    
