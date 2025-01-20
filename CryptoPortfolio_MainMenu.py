from Opt1_DisplayAllCurrency import opt1
print(70*'-')
print('     Class 02 \n     1. Kim \n     2. Chee')
print(70*'-')
print('     Cryptocurrency Portfolio Application Main Menu')
print(70*'-')
print('1. Display Cryptocurrency\n2. Add Cryptocurrency\n3. Amend Cryptocurrency\n4. Remove Cryptocurrency\n5. Crypto Portfolio Statement\n6. studentfunction1\n7. studentfunction2\nE. Exit Main Menu')
print(70*'-')
while True:
    opt = input('Select an option: ')
    if opt.lower() == 'e':
        break
    else:
        if int(opt) >= 1 or int(opt) <=7:
            break
        else:
            print('Only numbers 1-7 or E allowed')
            continue


#if opt == 1:
#    opt1()
#elif opt == 2:
#blah