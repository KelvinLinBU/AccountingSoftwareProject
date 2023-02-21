#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from balancesheet import BalanceSheet
from account import Account
from retainedearnings import RetainedEarnings

def display_menu_software():
    """prints the options for the accounting software"""
    print()
    print('(0) Quit the program')
    print('(1) Start the balance sheet software')
    print('(2) Start the statement of retained earnings software')
    
def display_menu_balancesheet():
    """prints the options for the balance sheet software"""
    print()
    print('(0) Quit the program')
    print('(1) Add/Modify an Account')
    print('(2) Remove an Account')
    print('(3) List of valid accounts')
    
def AccountingSoftware():
    """The function that starts the accounting software project"""
    while True:
        display_menu_software()
        choice = int(input('Enter your choice: '))
        print()
        if choice == 0:
            break
        if choice == 1:
            BalancesheetStart()
        if choice == 2:
            RetainedEarningsStart()
        else: 
            print('Invalid Choice! Try Again')
            
def BalancesheetStart():
    """The function that starts the balance sheet project"""
    company_name = str(input('Enter your company name: '))
    date = str(input('Enter the date: '))
    balancesheet = BalanceSheet(company_name, date)
    while True:
        print()
        print(balancesheet)
        print()
        display_menu_balancesheet()
        choice = int(input('Enter your choice: '))
        print()
        if choice == 0:
            break
        if choice == 1:
            amount = eval(input('Enter the amount (can also be negative): '))
            name = input('Enter the account name: ')
            balancesheet.add_to(amount, name)
        if choice == 2:
            name = input('Enter the account name: ')
            balancesheet.remove(name)
        if choice == 3:
            balancesheet.print_account_options()
        else:
            print('Invalid Choice! Try Again')
            
def RetainedEarningsStart():
    """The function that starts the statement of retained earnings project"""
    company_name = str(input('Enter your company name: '))
    date = str(input('Enter the date: '))
    beginning_retained_earnings = int(input('Enter your beginning retained earnings: '))
    net_income = int(input('Enter your net income/loss: '))
    dividends_declared = int(input('Enter your dividends declared: '))
    statement = RetainedEarnings(company_name, date, beginning_retained_earnings, net_income, dividends_declared)
    print()
    print(statement)
    print()
    
   
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            