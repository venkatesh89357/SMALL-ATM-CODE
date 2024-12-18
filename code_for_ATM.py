# Generating an ATM code for simple amount transfer and to check balance

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
    # If the option is one then it means the user wants to check balance in his account
    if option == 1:
        # Asking the user's account number
        account_number = input("Enter your META MASK account number: ")
        # Checking the account number entered by the user whether it's there in that particular bank account or not, Incase if the account number is not there in bank dataset then it will return "Invalid Account Number"
        
        if account_number in accounts:
            account=accounts[account_number] #getting account number into account for accessing the elements of that account
            pin = account["pin"]         #accessing account pin and keeping it in "pin" variable for further use
            input_pin=int(input("Enter your pin:"))
            if input_pin == pin:
                #if the pin matches then it will display the balance to the user otherwise it will return "Invalid pin"
               #account = accounts[account_number]
                print("Account Holder's Name:", account["name"])
                print("Balance:", account["balance"])
            else:
                print("Invalid pin!")    
        else:
            print("Invalid account number")
    elif option == 2:
        # If option is two which means the user wants to transfer funds to some other account and ask user account number and receiver account number
        from_account_number = input("Enter your account number: ")
        to_account_number = input("Enter the recipient's META MASKaccount number: ")
        # In this we are working on the same database so it checks Whether the account numbers are there or not if that two accounts are present then it will ask amount to transfer otherwise it will return "Invalid Account Numbers" 
        
        if from_account_number in accounts and to_account_number in accounts:
            from_account = accounts[from_account_number]
            to_account = accounts[to_account_number]
            account = accounts[from_account_number]
            pin = account["pin"]

            # Asking pin after entering the amount if pin matches then it checks the entered amount is lessthan of amount which is there in user account, Incase the balance is low then it will return "Low Balance" otherwise funds were transfered
            
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

        # If option is three that means the user wants to exit. so the loop gets terminated and the code ends
        print("--Thanks for using the BANK OF BARODA--")
        break
