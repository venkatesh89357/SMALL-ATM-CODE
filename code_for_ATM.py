print(" Welcome To BANK OF BARODA")
i=0
#taking aone username and password to login the app
username = "venkatesh"
password = "venkatesh@1234"
#pin=122122
input_username = input("Enter your username: ")
#converting them into lowercase letters
input_username1 = input_username.lower()
input_password = input("Enter your password: ")
input_password1 = input_password.lower() 
if input_username1 == username and input_password1 == password:     #checking weather the username and password are correct or not
    print("Login successful")
else:
    print("Login failed")
    while(True):
        i+=1       #Decreasing the no.of chances incase if login gets failed and if five chances are expired the program gets terminated
        print("Please try agian!..")
        print("You have anly five chances to login!..")
        print("You have used" , i ," Chances")
        input_username = input("Enter your username: ")
        input_password = input("Enter your password: ")
        if input_username == username and input_password == password:
            print("Login successful")
            break
        else:
            print("Login Failed!")
        if(i==4):      #checking weather the no.of attempts are expired or not
            print("Your chances has expired! and you consumed your five attempts to login!")
            print("Please Try Again After some time")
            exit(0)
#Taking the accounts dataset in which it contains all the data about account number, balance, pin, name etc....
#Here we are taking only two account numbers and you can take any number of account numbers which can have it's own data
accounts = {
"12345": {"name": "VENKATESH", "balance": 1000, "pin":122122},
"67890": {"name": "MAHESH", "balance": 2000, "pin":1234}
}
#Creating one Docstring which is used further
menu = """
ATM
1. Check balance
2. Transfer funds
3. Quit
"""
#Iterating the loop infinite times until it gets terminated through the "break" statement
while True:
    print(menu)
    option = int(input("Enter an option: "))

    if option == 1:
        account_number = input("Enter your META MASK account number: ")
        if account_number in accounts:
            account=accounts[account_number]
            pin = account["pin"]
            input_pin=int(input("Enter your pin:"))
            if input_pin == pin:
               #account = accounts[account_number]
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
            account = accounts[from_account_number]
            pin = account["pin"]
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
