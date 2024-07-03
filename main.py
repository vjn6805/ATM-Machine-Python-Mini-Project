#ATM Machine Python Mini Project

#importing modules
import time
import pyttsx3
import os
import pickle

#defining a function for voice output
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)  #0-male 1-female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  #makeing the speach audible
    
#function for storing userdata (name and pin)
def load_user_data():
    with open("namepin.bat", 'rb') as file1:
        return pickle.load(file1)
    
#function for updating details in file
def save_user_data(user_data):
    with open("namepin.bat", 'wb') as file1:
        pickle.dump(user_data, file1)
        
# Function for recording a transaction
def record_transaction(username, transaction):
    user_data = load_user_data()
    if 'transactions' not in user_data[username]:
        user_data[username]['transactions'] = []
    user_data[username]['transactions'].append(transaction)
    save_user_data(user_data)
    


#Function for startup screen
def startup():
    #this will be shown first
    print("""
          \t\t\t-------------------------------------------------------------------------------
          
          \t\t\t                        WELCOME TO NATIONAL BANK ATM
             
          \t\t\t-------------------------------------------------------------------------------
             
          \t\t\t                          Please Insert Your Card 
          """)
    
    #Voice Functionality
    time.sleep(1)
    speak("Welcome to National Bank ATM")
    speak("Please Insert Your Card")
    time.sleep(2)
    
    print("""\t\t\t\t                              Card Verified!!                                         """)
    speak("Card Verified Succesfully")
    
#Function for verification of PIN
def verification():
    user_data = load_user_data()
    
    print("")
    speak("Please enter your Name and PIN")
    
    for attempt in range(3):
        name = input("\t\t\t\t\t\t\t\tEnter Name: ").lower()
        pin = int(input("\t\t\t\t\t\t\t\tEnter PIN: "))
        print()
        
        # Verification logic
        if name in user_data and user_data[name]['pin'] == pin:
            print("\t\t\t\t\t         Verification Successful. Welcome {}!".format(name))
            speak("Verification Successful. Welcome {}!".format(name))
            return name
        else:
            print()
            speak("Verification Failed! Try Again")
            print("\t\t\t\t\t\t     Verification Failed. Please Try Again")
            
    
    # If all attempts fail
    print("\t\t\t\t\t\t    Too Many Attempts. Verification Failed")
    speak("Too many attempts. Please try again later.")
    return None

    print()
    
#if verification succesfull after function for choice
def afterlogin():
    print()
    print("""
          \t\t\t-------------------------Please Select One Option------------------------------
          
          \t\t\t                          1.Account Balance Inquiry
          \t\t\t                          2.Cash Withdrwal
          \t\t\t                          3.Cash Deposit
          \t\t\t                          4.Pin Change
          \t\t\t                          5.Transaction History
          \t\t\t                          6.Exit
          
          \t\t\t-------------------------------------------------------------------------------
        """)
    speak("Please Select one Option")
    #selecting the option
    choice =int(input("""
                      \t\t\t\t             Enter : """))
    print()
    return choice

#function for account balance inquiry
def accbalanceinq(username):
    user_data = load_user_data()
    balance = user_data[username]['balance']
    print("""
          \t\t\t                     Your Account Balance is: Rs.{:.2f}                                  """.format(balance))
    
    speak("Your account balance is: Rupees{:.2f}".format(balance))
    record_transaction(username, f"Balance Inquiry: Rs.{balance:.2f}")
    
# Function for cash withdrawal
def cash_withdrawal(username):
    user_data = load_user_data()
    balance = user_data[username]['balance']
    print("""
          \t\t\t                    Your Current Balance is: Rs.{:.2f}                                  """.format(balance))
    speak("Your current balance is: Rupees{:.2f}".format(balance))
    print()
    
    speak("Enter amount to withdraw")
    amount = float(input("""\t\t\t\t\t              Enter amount to withdraw : """))
    
    
    if amount > balance:
        print("""
          \t\t\t                    Insufficient Balance.Transaction Falied                                  """)
        speak("Insufficient balance. Transaction Failed.")
    else:
        user_data[username]['balance'] -= amount
        save_user_data(user_data)
        print("""
              \t\t\t        Transaction Successful. Your new balance is: Rs.{:.2f}                    """.format(user_data[username]['balance']))
        speak("Transaction Successful. Your new balance is: Rupees{:.2f}".format(user_data[username]['balance']))
        record_transaction(username, f"Withdrew: Rs.{amount:.2f}")
        
#function for cash deposit
def deposite(username):
    user_data = load_user_data()
    balance = user_data[username]['balance']
    
    print("""
          \t\t\t                    Your Current Balance is: Rs.{:.2f}                                  """.format(balance))
    speak("Your current balance is: Rupees {:.2f}".format(balance))
    print()
    
    speak("Enter amount to deposit")
    amount = float(input("""\t\t\t\t\t              Enter Amount to Deposit : """))
    
    
    user_data[username]['balance'] += amount
    save_user_data(user_data)
    print("""
              \t\t\t        Transaction Successful. Your new balance is: Rs.{:.2f}                    """.format(user_data[username]['balance']))
    speak("Transaction Successful. Your new balance is: Rupees{:.2f}".format(user_data[username]['balance']))
    record_transaction(username, f"Deposited: Rs.{amount:.2f}")
    
# Function for PIN change
def pin_change(username):
    user_data = load_user_data()
    print("")
    speak("Please enter your current PIN")
    current_pin = int(input("""\t\t\t\t\t            Please enter your current PIN : """))
    
    
    if user_data[username]['pin'] == current_pin:
        speak("Enter your new PIN")
        new_pin = int(input("""\t\t\t\t\t                Enter your new PIN : """))
        user_data[username]['pin'] = new_pin
        save_user_data(user_data)
        print("""
              \t\t\t\t\t               Pin Changed Succesfully                 """)
        speak("PIN Change Successful!")
    else:
        print("""
              \t\t\t              Incorrect Current PIN. PIN Change Failed.              """)
        speak("Incorrect Current PIN. PIN Change Failed.")
        
# Function for transaction history
def transaction_history(username):
    user_data = load_user_data()
    transactions = user_data[username].get('transactions', [])
    
    if not transactions:
        print("""
              \t\t\t-------------------------No Transaction Found------------------------------""")
        speak("No transactions found.")
    else:
        print("""
              \t\t\t-------------------------Transaction History------------------------------""")
        for transaction in transactions:
            print("\t\t\t\t\t", transaction)
        print("""
              \t\t\t--------------------------------------------------------------------------""")
        speak("Here is your transaction history.")


#main function
def main():
    startup()
    user=verification()
    if user:
        while(True):
            choice=afterlogin()
            if(choice==1):
                accbalanceinq(user)
            elif(choice==2):
                cash_withdrawal(user)
            elif(choice==3):
                deposite(user)
            elif (choice==4):
                pin_change(user)
            elif(choice==5):
                transaction_history(user)
                time.sleep(4)
            elif(choice==6):
                print("""
                    \t\t\t-----------------------Thank You----------------------------
                        
                    \t\t\t                      For Any Queries
                    \t\t\t                    Dial - 18001800123
                    \t\t\t                  Log on to - www.NATM.com
                    """)
                speak("THANK YOU for using national Bank ATM")
                 
                exit()

#calling the main function    
main()

    
    