#inputs som låter användaren skriva in längden på sidor
sida1 = int(input("Ange rektangelns första sida"))
sida2 = int(input("Ange rektangels andra sida"))

#area = längd 1 multiplicerat med längd 2
area = sida1*sida2

#är sida 1 och sida 2 blir rektangeln en kvadrat
if sida1 == sida2:
    print("Felaktigt svar, är båda sidor lika lång blir figuren en kvadrat istället för en rektangel.")
else:
    print(f"Din area är {area} ") 
    print("Höjden | Volymen")
for i in range(1,11):
    print(i, "|",i*area)