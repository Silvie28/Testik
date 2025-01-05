# # # # #print("Kdy je přestupný rok.")
# # # # #rok = int(input("Zadejte rok.\n"))
# # # # #if rok % rok == 4:
# # # # #   print(f"{rok} je přestupný")
# # # # #else:
# # # # #   print("Není přestupný")
# # # # #
x = int(input("Zadejte první celé číslo.\n"))
y = int(input("Zadejte druhé celé číslo.\n"))
hodnota = (x**y)
print (f"Výsledek umocněné hodnoty je {hodnota}.")

count(result)
cnter = 1
for a in range (100,10000,1):
   a = str(a)
   if a[0] != a[1] or a[0] != a[2] or a[0] != a[3] or a[1] != a[2] or a[1] != a[3] or a[2] != a[3]:
       counter+=1
print(f"Počet čísel, která nemají dvě stejné číslice je {counter}.")
# # # # # print("Nakládáme maso.")
# # # # # cena = 0
# # # # # odpoved = input("Chceš Bůček, Plec, Špek?")
# # # # # if odpoved == "bucek":
# # # # #     cena+=100
# # # # #     print (f"Platíš {cena}")
# # # # # elif odpoved == "plec":
# # # # #     cena+=200
# # # # #     print (f"Platíš {cena}")
# # # # # else:
# # # # #     print(f"Platíš {cena}")

# # # # # for i in range(5):
# # # # #     print ("ahoj")

# # # # for i in "kukkuku":
# # # #        print (i)
    
# # # #for soucet in range(5):
# # # #    print(soucet, soucet + 5)
# # # print(1, 2, 3, sep=', ', end='. ')   
# # # print(1,2,3, sep=", ",end".")
# # # print(1,2,3)
# # #print("prd, čau, konec, ahoj, sep="-", .)
# # print("jablko ", "ahoj ", "kuk ", sep="!", end="?")

# x = int(input("Zadej první číslo."))
# y = int(input("Zadej druhé číslo."))
# for i in (x,y):
#     vysledek = x**y
# print (vysledek)

# counter = 0
# for i in range(100, 1000):
#     cislo = str(i)  
#     if cislo[0] == cislo[1] or cislo[0] == cislo[2] or cislo[1] == cislo[2]:
#          counter +=1
# print(counter)



# cislo= input("Zadejte celočíselnou hodnotu.")
# vysledek =cislo.replace("3"," ").replace("6"," ")
# print (vysledek)

def digits(cislo):
    cislo_str = str(cislo) 
    return len(set(cislo_str)) == len(cislo_str) 
count=0
for cislo in range(100, 10000):
    if digits(cislo):
        count += 1
print(f"Počet celých čísel v rozsahu 100 až 9999, která mají různé číslice je {count}")

# def pozdrav():
#     print("Ahoj, Nazdar, Čau")
# # pozdrav()   
# for i in range(10):
#     pozdrav()

# def pozdrav(pismeno):
#     print(pismeno," Nazdar, Čau")
# pozdrav("ahoj")

# x = int(input("první číslo"))
# y = int(input("Druhé číslo"))
# print(x+y4)
