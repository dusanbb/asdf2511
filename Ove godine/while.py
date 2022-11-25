import random

baterija = 90

while baterija > 0:
    print("mozes koristiti telefon.", baterija, "%")
    baterija -= random.randint(5, 20)

print ("baterija je prazna")
