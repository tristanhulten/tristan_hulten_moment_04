sidor = []

sida1 = int(input("Ange rektangelns första sida"))
sida2 = int(input("Ange rektangels andra sida"))

area = sida1*sida2
data = [sida1, sida2, area]

if sida1 == sida2:
    print("Felaktigt svar, är båda sidor lika lång blir figuren en kvadrat istället för en rektangel.")
    data.append("Kvadrat")
else:
    print(f"Din area är {area} ") 
    print("Höjden | Volymen")
for i in range(1,11):
    print(i, "|",i*area)

ny = input("vill du göra en ny uträkning (Y/N)?")

sidor.append(data)


 
