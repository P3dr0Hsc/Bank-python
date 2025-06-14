import os
import time
import random
from keygen import ab

#code

password1 = []

enterpassword = True

pwd = True

bank = False

file = "bank/config.txt"

balance = 50

extract = []

def replace_password():
    pwd = False
def bank():
    while True:
            time.sleep(0.5)
            print("[1] deposit")
            print("[2] withdraw")
            print("[3] see balance")
            print("[4] exit")
            print("[5] change password")
            try:
                print()
                opcbank = int(input("enter your option: "))
            except:
                print("only numbers!!! Try Again...")
                
            
            if opcbank == 1:
                with open(file, "r") as file_handle:
                    lines = file_handle.readlines()

                balance_line = lines[2].strip()
                balance = int(balance_line.split("=")[1].strip())
                try: 
                    amount = int(input("How much do you want to deposit? "))
                    balance += amount
                except:
                    print("only numbers!!! Try Again...")

                lines[2] = f"balance = {balance}\n"

                with open(file, "w") as file_handle:
                    file_handle.writelines(lines)

                print(f"Deposit successful! New balance: {balance}")
                

            elif opcbank == 2:
                with open(file, "r") as file_handle:
                    lines = file_handle.readlines()

                balance_line = lines[2].strip()
                balance = int(balance_line.split("=")[1].strip())
                try:
                    amount = int(input("How much do you want to withdraw? "))
                except:
                    print("only numbers!!! Try Again...")

                if amount > balance:
                    print("Insufficient balance.")
                    
                else:
                    balance -= amount
                    lines[2] = f"balance = {balance}\n"

                    with open(file, "w") as file_handle:
                        file_handle.writelines(lines)

                    print(f"Withdrawal successful! New balance: {balance}")
                    
            if opcbank == 3:
                with open(file, "r") as arquive:
                    liness = arquive.readlines()
                    print(liness[2])
                    
            if opcbank == 4:
                print("leaving! until next time...")
                pwd = False
                break
                
            if opcbank == 5:
                with open(file, "r") as arquive:
                    lines = arquive.readlines()
                    lines[0] = f"password = \n"
                    lines[1] = f"pswrd = True\n"
                    with open(file, "w") as f:
                        f.writelines(lines)
                replace_password()
                break
                                               
if os.path.exists(file):
        with open(file, "r") as arquive:
            for numberline, line in enumerate(arquive, 1):
                if numberline == 2:  
                    if line.strip() == "pswrd = True":
                        pwd=True
                    else:
                        pwd = False
                    if line.strip() == "pswrd = False":
                        pwd = False

else:
    print("arquive not founder.")

def password():

    if os.path.exists(file):
        with open(file, "r") as f:
            lines = f.readlines()

        acesspassword = input("Enter your password: ")

        line_pass = lines[0].strip()  
        password_save = line_pass.split("=")[1].strip()

        if acesspassword == password_save:
            print("Password correct!")
            bank()
            return True
        else:
            print("password distinct! try again...")
            time.sleep(1.5)
            password()
            return False
            
while pwd:
    print("=== attention  you will never see this again ===")
    print(" [1] create password ")
    print(" [2] random password ")
    try: 
        opcpassword = int(input("enter your option: "))
    except:
        print("only numbers!!! Try Again...")
    if opcpassword == 1:
        createpassword = input("enter your password: ")
        password1.append(createpassword)
        with open(file, "r") as arquive:
            lines = arquive.readlines()
        if createpassword == lines[0]:
            print("senha igual a antiga")
            bank()
        
        lines[0] = f"password = " + createpassword + "\n"
        lines[1] = f"pswrd =" + "False" + "\n"

        with open(file, "w") as f:
            f.writelines(lines)
        bank()
        
    if opcpassword == 2:
        with open(file, "r") as arquive:
            lines = arquive.readlines()
        
        lines[0] = f"password = {ab}\n"
        password1.append(ab)

        lines[1] = f"pswrd = False\n"
        print(f"{ab} Mark this password because you won't see it anymore!!!")
        time.sleep(10)
        with open(file, "w") as f:
            f.writelines(lines)
        bank()
while enterpassword:
    password()
    enterpassword = False 