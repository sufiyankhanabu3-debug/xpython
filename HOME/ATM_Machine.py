print(20*"=", "ATM machine", 20*"=")
pin = int(input(" Enter PIN: "))
pin_pass = 995696
Money = 100

if pin == pin_pass:
    while True:
        print(" ")
        print("  1) Add Money")
        print("  2) Withdraw Money")
        print("  3) Check Balance")
        print("  4) Exit")
        choose = input("Choose: ")

        if choose == "1":
            amount = int(input("Enter Amount: "))
            Money = Money + amount
            print("Total Money", Money)
        elif choose == "2":
            amount = int(input("Enter Amount: "))
            if amount > Money:
                print("Insufficient balance!")
            else:
                Money = Money - amount
                print("Money Left", Money)
        elif choose == "3":
            print("Total Balance:", Money)
        elif choose == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice, try again.")
else:
    print("Password is Wrong!")