# # # # # #vek=int(input("Jaký je tvůj věk?\n"))
# # # # # #rok=90-vek
# # # # # #mesic=12*rok
# # # # # #tyden=52*rok
# # # # # #den=365*rok
# # # # # #print(f"Do konce zivota ti zbývá {rok} roků {mesic} měsíců, {tyden} dnů a {den} dnů")
# # # # # #print("Vítejte v kalkulátoru na výpočet plateb.")
# # # # # #platba=int(input("Kolik je celková platba\n"))
# # # # # #spropitne=int(input("Kolik dáte dýško (v %)?\n"))
# # # # # #kazdy=int(input("Kolik lidí platí?\n"))
# # # # # #ucet=int(((platba/100)*spropitne)+platba)/2
# # # # # #print(f"Každý člověk by měl zaplatit {ucet}")

# # # # # #print("Vítejte na horské dráze")
# # # # # #vyska=int(input("Jaká je vaše výška v cm?\n"))
# # # # # #if vyska >=87:
# # # # # #print("Ano, můžete jet")
# # # # # #else:
# # # # # #print("Ne, nemůžete jet")
  
# # # # # #print("Kdy je potřeba vyměnit zimní pneu.")
# # # # # #pneu = int(input("Kolik je nyní stupňů?\n"))
# # # # # #if pneu<=4:
# # # # # #print ("Přezuj!"
# # # # # #elif pneu>8:
# # # # # #  print("Nemusíš přezout!")
# # # # # #else:
# # # # # #print("Seď doma!!!")
# # # # # #a=int(input("Zadej první číslo\n"))
# # # # # #b=int(input("Zadej druhé číslo\n"))
# # # # # #c=int(input("Zadej třetí číslo\n"))
# # # # # #soucet=(a+b+c)
# # # # # #print("Výsledek je " + str(soucet))
# # # # # #prumer=((a+b+c)/3)
# # # # # #print("Průměr je " + str(prumer))

# # # # # #  vyska= float(input("Zadejte výšku v metrech.\n"))
# # # # # # vaha=int(input("Zadejte váhu v kg"))
# # # # # # bmi = vaha/(vyska*vyska)
# # # # # # if bmi<18:
# # # # # #     print(f"Vaše BMI je {bmi}, mate Under")
# # # # # # elif bmi>18.5:
# # # # # #     print(f"Vaše BMI je {bmi}, mate normal")
# # # # # # elif bmi<25:
# # # # # #     print(f"Vaše BMI je {bmi}, mate over")
# # # # # # else:
# # # # # #     print("ero")
# # # # # # try:
# # # # # #   apples=int(input("enter the amount of apples you have"))
# # # # # #   if apples < 0:
# # # # # #              raise Exception
# # # # # #              print("you have", apples,"apples")
# # # # # # finally:
# # # # # #              print("end")
# # # # # # try:
# # # # # #   pocet=30
# # # # # #   mnozstvi=int(float(input("zadej mnozstvi")))
# # # # # #   pomer=pocet/mnozstvi
# # # # # #   print("Zadej celé číslo int")
# # # # # # except ValueError:
# # # # # #   print("Dělení nulou nelze")
# # # # # # except ZeroDivisionError:
# # # # # #   print("You cannot divide the delivery into 0 parts")

# # # # # # rychlost=100
# # # # # # if rychlost<80:
# # # # # #   print("jedeš pomalu") 
# # # # # #   print("pokuta")
# # # # # # elif rychlost>80 and rychlost<100:  
# # # # # #   print("jedeš akorát")
# # # # # # else:
# # # # # #   print("jedeš rychle")

# # # # # # a = 50
# # # # # # if a<60:
# # # # # #    print("ok")
# # # # # # else:
# # # # # #   print("not ok") 

# # # # # # a = 50
# # # # # # a =("Zadej číslo")
# # # # # # if a == 50:
# # # # # #  print("funguje")
# # # # # #  print("......")
# # # # # # print("test")
# # # # # # a=50
# # # # # # print(a>40)
# # # # # # a = 60
# # # # # # print(a==50)

# # # # # # bmi=input("Zadejte svou výšku v metrech\n")
# # # # # # bmi_1=input("Zadejte svou váhu v kg\n")
# # # # # # bmi_2=int(bmi_1)/float(bmi)**2
# # # # # # bmi_2=int(bmi_2)
# # # # # # print(bmi_2)
# # # # # # if bmi_2<18:
# # # # # #   print("podváha ")
# # # # # # elif bmi_2<=25:
# # # # # #   print("norma")
# # # # # # elif bmi_2<=30:
# # # # # #   print("nadváha")
# # # # # # else: 
# # # # # #   print("tlustoch")
# # # # # #{}  ALTGR a B, N

# # # # # #x=1
# # # # # #x+=1#x=x+1
# # # # # #print(x)
# # # # # #print(round(8/3,2))

# # # # # #name= "David"
# # # # # #age=35
# # # # # #print("Jmenuji se "+ (name) + "a je mi " + (str(age)) + "let")
# # # # # #print(f"Jmenuji se {name} a je mi {age} let")

# # # # # # def digits(cislo):
# # # # # #     cislo_str = str(cislo) 
# # # # # #     return len(set(cislo_str)) == len(cislo_str) 
# # # # # # count=0
# # # # # # for cislo in range(100, 10000):
# # # # # #     if digits(cislo):
# # # # # #         count += 1
# # # # # # print(f"Počet celých čísel v rozsahu 100 až 9999, která mají různé číslice je {count}")

# # # # # # text = "Ahoj Sisi"
# # # # # # textik = text.replace("Sisi", "Rendy")
# # # # # # print(textik)

# # # # # # for x in [10, 14, 21]:
# # # # # #     if x % 7 == 0:
# # # # # #         print("celer")

# # # # # # zadane_slovo = input(f'zadej slovo ktere chces vypsat: ')
# # # # # # for _ in zadane_slovo:
# # # # # #     print(_)

# # # # # # spravneHeslo = 'pes'
# # # # # # counter = 3
# # # # # # while counter>0:
# # # # # #     heslo=input(f'pocet pokusu je {counter} a zadej heslo ')
# # # # # #     if heslo == spravneHeslo:
# # # # # #         print('uhodl jsi heslo')
# # # # # #         break
# # # # # #     counter-=1
# # # # # #     if counter==0:
# # # # # #         print(f'dosel ti pocet pokusu')

# # # # # def napis_hlasku(nazev, skore):
# # # # #     """Popíše skóre. Název má být přivlastňovací přídavné jméno."""

# # # # #     print(nazev, 'skóre je', skore)
# # # # #     if skore > 1000:
# # # # #         print('Světový rekord!')
# # # # #     elif skore > 100:
# # # # #         print('Skvělé!')
# # # # #     elif skore > 10:
# # # # #         print('Ucházející.')
# # # # #     elif skore > 1:
# # # # #         print('Aspoň něco')
# # # # #     else:
# # # # #         print('Snad příště.')

# # # # # napis_hlasku('Tvoje', 256)
# # # # # napis_hlasku('Protivníkovo', 5)

# # # # for i in range(1, 10):
# # # #     for j in range(1, 10):
# # # #         print(i * j, end="\t")
# # # #     print("\n")

# # # patro = 1
# # # energy = 70
# # # print("Jsem v ",patro,"." + "patro")
# # # while patro != 5:
# # #     krok = 0
# # #     while krok != 20:
# # #         krok += 1
# # #         energy -= 1
# # #         if energy == 0:
# # #             print("Jsem unavená, odpočinu si.")
# # #             energy += 70
# # #     patro += 1
# # #     print("Teď jsem na ", patro, "patře")
# # # print("Dostal jsem se na místo.")   

# # #-----NÁSOBILKA------------
# # print("Malá násobilka:")
# # for i in range(1,11):
# #   for j in range(1,11):
# #     print(i,"*",j,"=",i*j)

