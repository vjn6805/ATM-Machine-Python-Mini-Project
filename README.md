# ATM-Machine-Python-Mini-Project
## Overview
This repository contains a simple ATM Machine project written in Python. The project simulates the basic functionalities of an ATM machine including balance inquiry, cash withdrawal, cash deposit, PIN change, and transaction history.

## Features
* __Voice Assistance :__ Provides voice feedback using the pyttsx3 library.
* __User Authentication :__ Validates user credentials (name and PIN) from a stored data file.
* __Balance Inquiry :__ Displays the current account balance.
* __Cash Withdrawal :__ Allows users to withdraw cash if sufficient balance is available.
* __Cash Deposit :__ Enables users to deposit cash into their account.
* __PIN Change :__ Provides an option to change the account PIN.
* __Transaction History :__ Keeps a record of all transactions performed

## Prerequisites
Before running the project, ensure you have the following installed:

* __Python 3.x__ - pyttsx3 library for text-to-speech functionality.
* pickle module for data serialization

## Project Structure
* __main.py:__ Main script containing the entire project code.
* __pininfo.py:__ Script that contains the information of user (name, PIN,balance)
* __namepin.bat:__ Binary file used for storing user data (name, PIN, balance, transactions).

## Main Functionalities
* __Startup Screen:__ Displays the welcome message and prompts for card insertion.
* __Verification:__ Authenticates the user by verifying the entered name and PIN.
* __Account Balance Inquiry:__ Displays the current balance of the user's account.
* __Cash Withdrawal:__ Allows the user to withdraw cash after checking for sufficient balance.
* __Cash Deposit:__ Enables the user to deposit cash into their account.
* __PIN Change:__ Allows the user to change their account PIN after verifying the current PIN.
* __Transaction History:__ Displays the user's transaction history.

## Usage
* Clone the repository to your local machine.
```bash
git clone https://github.com/your-username/ATM-Machine-Python-Mini-Project.git
cd ATM-Machine-Python-Mini-Project
```
* Install the required libraries.
```bash
pip install pyttsx3
```
* Ensure the namepin.bat file exists in the same directory as ATM.py.
* Run the project.







