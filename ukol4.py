def nasobeni():
    seznam = (input("Zadej celá čísla: "))
    seznam = list(seznam)
    print(seznam)
    counter = 1
    for i in (seznam):
        counter *= int(i)
    print(counter)
nasobeni()

#  4.

# def vymaz():
#     n = input("Zadej celá čísla:")
#     n = list(n)
#     o = input ("Zadej číslo, které chceš smazat:")
#     count = 0
#     while o in n:
#         n.remove(o)
#         count+=1
#     print(n) 
#     vysledek=(f"Počet smazaných čísel je: {count} ")
#     print(vysledek)
    
# vymaz()       
# 5.
# def slouceni():
#     seznam1=input("Zadej seznam celých čísel: ")
#     seznam1 =list(seznam1)
#     print(seznam1)
#     seznam2=input("Zadej druhý seznam celých čísel: ")
#     seznam2 =list(seznam2)
#     print(seznam2)
#     seznam1.extend(seznam2)
#     print (seznam1)
# slouceni()    


