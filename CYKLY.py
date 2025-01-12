# for i in range(5):
#     print("Nikdy nebudu odsazovat o tři mezery!")
# for i in ("ahoj","nazdar","čau"):
#     print(i + "!")   

# count = 0
# count1 = 0
# for i in range(1,11):
#     if i % 2 != 0:
#         print(f"číslo {i} je liché.")
#         count+=1
#     else:
#         print(f"číslo {i} je sudé.")
#         count1+=1
# print(f"Počet lichých znaků v řetězcí je {count}")
# print(f"Počet sudých znaků v řetězcí je {count1}")  

#....Bmi.....
# vyska = float(input("Zadej vyšku v metrech:\n"))
# vaha = int(input("Zadej váhu v kilogramech:\n"))
# bmi= vaha/(vyska**2) 
# if (bmi)<18.5:
#     print(f"Tvoje BMI je {round(bmi)}. Jsi housenka")
# elif (bmi)<24.99:
#     print(f"Tvoje BMI je {round(bmi)}. Normalka")
# elif (bmi)>25:
#     print(f"Tvoje BMI je {round(bmi)}. Jsi eliša")
# #print (f"Tvoje BMI je {round(bmi)}.")
# count = 3
# heslo = input("Zadej heslo: \n")
# while heslo.lower == "pes":
    
#     print("Heslo je dobře!") 
#     break
# correct_password = "pes"  
# user_password = ""  

# while user_password != correct_password:
#     user_password = input("Zadejte heslo: ")  
#     if user_password != correct_password:
#         print("Nesprávné heslo, zkuste to znovu.")  

# # print("Heslo je správné!")
# pokus = 3
# print("Zadej cislo:\n")

# while True:
#     cislo = int(input())
#     if cislo >= 10:
#         print("Ano číslo je v pořádku.")
#         break
#     else:
#         print("Špatně, zadej znovu!!: ")
#         pokus-=1
#     if pokus == 0:
#         print ("hovno")
#         break
        
# s = 'nazdarek'
# t = s  # s and t point to the same string
# t = s[2:3]  # now t points to the new string 'll'
# print(s)  # prints 'Hello' as s is not changed
# print(t)  

# s = 'Hello'
# print(s.find('e'))
# # 1
# print(s.find('ll'))
# # 2
# print(s.find('L'))
# # -1

# s = input("Zadej vetu na test palindrom:\n")
# veta = s[0:]
# print(veta)
# palindrom = s[::-1]
# print(palindrom)
# if veta.lower() == palindrom.lower():
    
#     print("Ano, je to palindrom.")
# else:
#     print("Není to palindrom.")
