def opt3():
 print("-----------------------------------------------")
 opt=input("Select an option:")
 print("No - CryptoCurrency")
 print("---------------------------")
 print("0 - Bitcoin\n1 - Etherum\n2 -Solana\n3 - Decentraland\n4 - The Sandbox\n5 - Dodgecoin\n6 - Shiba Inu")
 print("---------------------------")
 selection=input("Enter 0 to 6 for your selection or E to exit : ")
 if selection=="0" :

 if selection=="E" :
    mainmenu()
 else:
   print("Invalid input.")
   opt3()