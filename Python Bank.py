# Problem: Create a Python program that simulates a simple bank system. 

# The program should allow a user to:

# Create an account
# Deposit money
# Withdraw money
# Check balance
# Exit the program

# Requirements:

# Use a dictionary to store account information (e.g., username, balance).
# Handle exceptions for invalid input, insufficient balance, etc.
# Use functions to organize the code.
# Ensure the user can perform multiple operations until they choose to exit. 

# Expected output:

# Welcome to the Python Bank!
# 1. Create Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. Check Balance
# 5. Exit

# Choose an option: 1
# Enter your username: yash123
# Account created successfully!

# Choose an option: 2
# Enter your username: yash123
# Enter amount to deposit: 5000
# Deposit successful! Your new balance is 5000.

# Choose an option: 3
# Enter your username: yash123
# Enter amount to withdraw: 3000
# Withdrawal successful! Your new balance is 2000.

# Choose an option: 4
# Enter your username: yash123
# Your current balance is 5000.

# Choose an option: 5
# Thank you for using Python Bank!

details = {
    "Username": "",
    "Balance": 0,
}

# Welcome the user!
print(
    """Welcome to the Python Bank!
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Exit"""
)

query = 0

def matchQuery():
    match query:
        case 0:
            print("0 is not a option!")

        case 1:
            username = str(input("Enter your username: "))

            if username != "":
                details.update({"Username": username})
                details.update({"Balance": 0})
                print("Account created successfully!")

            elif username == "":
                print("Username should have atleast 1 character!")

        case 2:
            if details["Username"] == "":
                print("You should first go and create an account!")

            else:
                entered_username = str(input("Enter your username: "))

                if entered_username != details.get("Username"):
                    print("Invalid username!")

                else:
                    deposit_amount = int(input("Enter the amount to be deposited: "))
                    if deposit_amount < 0:
                        print("Depositing amount can't be in negative!")

                    else:
                        details["Balance"] += deposit_amount
                        print(f"{deposit_amount} has been deposited. New Balance: {details['Balance']}")

        case 3:
            if details["Username"] == "":
                print("You should first go and create an account!")

            else:
                entered_username = str(input("Enter your username: "))

                if entered_username != details.get("Username"):
                    print("Invalid username!")

                else:
                    withdrawn_amount = int(input("Enter the amount to be withdrawn: "))

                    if withdrawn_amount <= 0:
                        print("Withdrawal amount must be greater than zero.")

                    elif withdrawn_amount > details["Balance"]:
                        print(f"You have insufficient balance. Your current balance is {details['Balance']}.")

                    else:
                        details["Balance"] -= withdrawn_amount
                        print(f"{withdrawn_amount} has been withdrawn. New Balance: {details['Balance']}")


        case 4:
            if details["Username"] == "":
                print("You should first go and create an account!")

            else:
                entered_username = str(input("Enter your username: "))

                if entered_username != details.get("Username"):
                    print("Invalid username!")

                else:
                    print(f"Your bank balance is {details['Balance']}.")

        case 5:
            print("Thank you for using Python Bank!")
            return "Bye  bye!"

while True:
    try:
        print()
        query = int(input("Choose an option: "))

    except ValueError:
        print("Please tell the number of the option!")
    
    # matchQuery()
    if matchQuery() == "Bye  bye!":
        break