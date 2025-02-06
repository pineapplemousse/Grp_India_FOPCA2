from Opt1_DisplayAllCurrency import opt1
from Opt2_AddCurrency import opt2
from Opt3_AmendCurrency import opt3
from Opt4_RemoveCurrency import opt4
from Opt5_PortfolioStatment import opt5
from Opt6_ShuWei import opt6
from Opt7_Lohith import opt7

def mainmenu():
    while(True):
        print(70*'-')
        print('     Class 02 \n     1. Kim \n     2. Chee')
        print(70*'-')
        print('     Cryptocurrency Portfolio Application Main Menu')
        print(70*'-')
        print('1. Display Cryptocurrency\n2. Add Cryptocurrency\n3. Amend Cryptocurrency\n4. Remove Cryptocurrency\n5. Crypto Portfolio Statement\n6. Convert Currency (Shu Wei)\n7. Comparison Graph (Lohith)\nE. Exit Main Menu')
        print(70*'-')

        opt = str(input('Select an option: '))
        
        if opt.lower() == 'e':
            break
        else:
            try:
                if opt == '1':
                    print('You selected option 1: Display Cryptocurrency')
                    opt1()
                elif opt == '2':
                    print('You selected option 2: Add Cryptocurrency')
                    opt2()
                elif opt == '3':
                    print('You selected option 3: Amend Cryptocurrency')
                    opt3()
                elif opt == '4':
                    print('You selected option 4: Remove Cryptocurrency')
                    opt4()
                elif opt == '5':
                    print('You selected option 5: Crypto Portfolio Statement')
                    opt5()
                elif opt == '6':
                    print('You selected option 6: Convert Currency (Shu Wei)')
                    opt6()
                elif opt == '7':
                    print('You selected option 7: Comparison Graph (Lohith)')
                    opt7()
                
            except ValueError:
                print('Invalid input. Please enter a number between 1-7 or E.')

mainmenu()