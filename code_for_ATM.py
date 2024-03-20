print(" Welcome To BANK OF BARODA")
i=0
username = "venkatesh"
password = "venkatesh@1234"
pin=122122
input_username = input("Enter your username: ")
input_username1 = input_username.lower()
input_password = input("Enter your password: ")
input_password1 = input_password.lower() 
if input_username1 == username and input_password1 == password:
    print("Login successful")
else:
    print("Login failed")
    while(True):
        i+=1
        print("Please try agian!..")
        print("You have anly five chances to login!..")
        print("You have used" , i ," Chance")
        input_username = input("Enter your username: ")
        input_password = input("Enter your password: ")
        if input_username == username and input_password == password:
            print("Login successful")
            break
        else:
            print("Login Failed!")
        if(i==4):
            print("Your chances has expired! and you consumed your five attempts to login!")
            print("Please Try Again After some time")
            exit(0)
accounts = {
"12345": {"name": "VENKATESH", "balance": 1000},
"67890": {"name": "MAHESH", "balance": 2000}
}

menu = """
ATM
1. Check balance
2. Transfer funds
3. Quit
"""
while True:
    print(menu)
    option = int(input("Enter an option: "))

    if option == 1:
        account_number = input("Enter your META MASK account number: ")
        if account_number in accounts:
            input_pin=int(input("Enter your pin:"))
            if input_pin == pin:
                account = accounts[account_number]
                print("Account Holder's Name:", account["name"])
                print("Balance:", account["balance"])
            else:
                print("Invalid pin!")    
        else:
            print("Invalid account number")
    elif option == 2:
        from_account_number = input("Enter your account number: ")
        to_account_number = input("Enter the recipient's META MASKaccount number: ")
        if from_account_number in accounts and to_account_number in accounts:
            from_account = accounts[from_account_number]
            to_account = accounts[to_account_number]
            transfer_amount = float(input("Enter the Etherteum amount to transfer: "))
            input_pin = int(input("Enter your pin:"))
            if input_pin == pin:
                if transfer_amount > from_account["balance"]:
                    print("Insufficient funds")
                else:
                    from_account["balance"] -= transfer_amount
                    to_account["balance"] += transfer_amount
                    print("Transfer successful")
                    print("Your balance is", from_account["balance"])
            else:
                print("Invalid Pin!")        
        else:
            print("Invalid account number")
    elif option == 3:
        print("--Thanks for using the BANK OF BARODA--")
        break
