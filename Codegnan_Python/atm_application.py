#mini project
#application name --> ATM Machine
while True:
    account_balance = 100000
    print("------------------------------------------------------Insert the card-----------------------------------------------------------")
    card = input("Enter card : ")
    password = int(input("Enter password : "))
    if card == "c":
        print("Welcome Pooja")
        if password == 1234:
              print("Choose option:  Balance enquiry , Withdraw")
              options = input("Choose options:")
              if options == "Balance enquiry":
                  print("Your account balance: ", account_balance)
              elif options == "Withdraw":
                  amount_to_withdraw = (int(input("Enter amount: ")))
                  print("Successful withdrawl")
                  print("Remaining Balance: ",account_balance - amount_to_withdraw)
              else:
                print("Invalid Options")
        else:
            print("Incorrect Password")
    else:
        print("Invalid card !! \nInsert Correct Card..!")          
