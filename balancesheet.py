from account import Account

class BalanceSheet:
    """This is the class for a balance sheet used in financial accounting"""

    def __init__(self, company_name, date):
        """This is the constructor for the balance sheet class"""
        self.company_name = company_name
        self.date = date
        self.current_assets_list = []
        self.fixed_assets_list = []
        self.current_liabilities_list = []
        self.long_term_liabilities_list = []
        self.equities_list = []
        self.current_assets = ['Cash', 'Accounts Receivable', 'Inventory', 'Prepaid Expenses','Prepaid Liabilities', 'Marketable Securities', 'Other Short Term Investments', 'Cash Equivalent']
        self.fixed_assets = ['Land', 'Buildings', 'Machinery', 'Furniture', 'Vehicles', 'Accumulated Depreciation', 'Goodwill', 'Investment'] 
        self.current_liabilities = ['Accounts Payable', 'Notes Payable', 'Accrued Expense', 'Taxes Payable', 'Credit Card Debt', 'Accrued Expenses']
        self.long_term_liabilities = ['Long Term Debt', 'Bank Debt', 'Other Long Term Notes Payable']
        self.equities = ['Preferred Stock', 'Common Stock', 'Retained Earnings']
        
    def __repr__(self):
        """returns a string representation of the balance sheet"""
        s = self.company_name + '\n'
        s += 'Balance Sheet' + '\n'
        s += "As of: " + self.date + '\n' 
        s += '-----------------------------------------------------------' + '\n'
        s += 'ASSETS' + '\n'
        s += 'Current Assets:' + '\n'
        for x in range(len(self.current_assets_list)):
            s += self.current_assets_list[x].name + '   ' + str(self.current_assets_list[x].amount) + "\n"
        s += '\n' + 'The total current assets balance is: ' + str(self.current_asset_balance()) + "\n" + '\n'
        s += 'Fixed Assets: ' + '\n'
        for x in range(len(self.fixed_assets_list)):
            s += self.fixed_assets_list[x].name + '   ' + str(self.fixed_assets_list[x].amount) + "\n"
        s += 'The total fixed assets balance is: ' + str(self.fixed_asset_balance()) + "\n" + '\n'
        s += 'The total asset balance is: ' + str(self.fixed_asset_balance() + self.current_asset_balance()) + '\n'
        s += '-----------------------------------------------------------' + '\n'
        s += 'LIABILITIES' + '\n'
        s += 'Current Liabilities:' + '\n'
        for x in range(len(self.current_liabilities_list)):
            s += self.current_liabilities_list[x].name + '   ' + str(self.current_liabilities_list[x].amount) + "\n"
        s += '\n' + 'The total current liabilities balance is: ' + str(self.current_liabilities_balance()) + "\n" + '\n'
        s += 'Long Term Liabilities: ' + '\n'
        for x in range(len(self.long_term_liabilities_list)):
            s += self.long_term_liabilities_list[x].name + '   ' + str(self.long_term_liabilities_list[x].amount) + "\n"
        s += 'The total long term liabilities balance is: ' + str(self.long_term_liabilities_balance()) + "\n" + '\n'
        s += 'The total liabilities balance is: ' + str(self.current_liabilities_balance() + self.long_term_liabilities_balance()) + '\n'
        s += '-----------------------------------------------------------' + '\n'
        s += "OWNER'S EQUITIY" +'\n'
        s += 'Equities:' + '\n'
        for x in range(len(self.equities_list)):
            s += self.equities_list[x].name + '   ' + str(self.equities_list[x].amount) + "\n"
        s += '\n' + 'The total equities balance is: ' + str(self.equities_balance()) + "\n" + '\n'
        s += 'The total equities and liabilities is: ' + str(self.current_liabilities_balance() + self.long_term_liabilities_balance() + self.equities_balance())
        s += '\n'
        if (self.fixed_asset_balance() + self.current_asset_balance()) == self.current_liabilities_balance() + self.long_term_liabilities_balance() + self.equities_balance():
            s += 'The total assets and total liabilities and shareholders equities balance'
        else:
            s += 'The total assets and total liabilities and shareholders equities do not balance'
        return s
    
    def current_asset_balance(self):
        """returns the current asset balance"""
        total = 0
        if self.current_assets_list == []:
            return total
        else:
            for x in range(len(self.current_assets_list)):
                total += self.current_assets_list[x].amount
            return total

    def fixed_asset_balance(self):
        """returns the fixed asset balance"""
        total = 0
        if self.fixed_assets_list == []:
            return total
        else:
            for x in range(len(self.fixed_assets_list)):
                total += self.fixed_assets_list[x].amount
            return total
        
    def current_liabilities_balance(self):
        """returns the current liabilities balance"""
        total = 0
        if self.current_liabilities_list == []:
            return total
        else:
            for x in range(len(self.current_liabilities_list)):
                total += self.current_liabilities_list[x].amount
            return total
    
    def long_term_liabilities_balance(self):
        """returns the long term liabilities balance"""
        total = 0
        if self.long_term_liabilities_list == []:
            return total
        else:
            for x in range(len(self.long_term_liabilities_list)):
                total += self.long_term_liabilities_list[x].amount
            return total
    
    def equities_balance(self):
        """returns the equities balance"""
        total = 0
        if self.equities_list == []:
            return total
        else:
            for x in range(len(self.equities_list)):
                total += self.equities_list[x].amount
            return total
        
    def categorize(self, name):
        """returns 1 for current asset, 2 for fixed asset, 3 for current liability, 4 for long term liability, 5 for equity"""
        if name in self.current_assets:
            return 1
        elif name in self.fixed_assets:
            return 2
        elif name in self.current_liabilities:
            return 3
        elif name in self.long_term_liabilities:
            return 4
        elif name in self.equities:
            return 5
        return -1

    def add_to(self, amount, name):
        """adds to the assets, liabilities, equities section of a balance sheet"""
        category = self.categorize(name)
        if category == -1:
            print('This account does not exist')
        elif isinstance(amount, int) != True:
            print('The amount is invalid')
        elif self.is_in_balance_sheet(name) == True:
            if category == 1:
                for x in range(len(self.current_assets_list)):
                    if name == self.current_assets_list[x].name:
                        if (self.current_assets_list[x].amount + amount) > 0:
                            self.current_assets_list[x].amount += amount
                        else:
                            print('Cannot have a negative value for an account!')
            if category == 2:
                for x in range(len(self.fixed_assets_list)):
                    if name == self.fixed_assets_list[x].name:
                        if (self.fixed_assets_list[x].amount + amount) > 0:
                            self.fixed_assets_list[x].amount += amount
                        else:
                            print('Cannot have a negative value for an account!')
            if category == 3:
                for x in range(len(self.current_liabilities_list)):
                    if name == self.current_liabilities_list[x].name:
                        if (self.current_liabilities_list[x].amount + amount) > 0:
                            self.current_liabilities_list[x].amount += amount
                        else:
                            print('Cannot have a negative value for an account!')
            if category == 4:
                for x in range(len(self.long_term_liabilities_list)):
                    if name == self.long_term_liabilities_list[x].name:
                        if (self.long_term_liabilities_list[x].amount + amount) > 0:
                            self.long_term_liabilities_list[x].amount += amount
                        else:
                            print('Cannot have a negative value for an account!')
            if category == 5:
               for x in range(len(self.equities_list)):
                   if name == self.equities_list[x].name:
                       if (self.equities_list[x].amount + amount) > 0:
                           self.equities_list[x].amount += amount
                       else:
                           print('Cannot have a negative value for an account!')
        else:
            print('name is not in balance sheet')
            if amount < 0:
                print('You cannot have a negative value for an account!')
            else:
                account = Account(amount, name, category)
                if account.category == 1:
                    self.current_assets_list += [account]
                elif account.category == 2:
                    self.fixed_assets_list += [account]
                elif account.category == 3:
                    self.current_liabilities_list += [account]
                elif account.category == 4:
                    self.long_term_liabilities_list += [account]
                elif account.category == 5:
                    self.equities_list += [account]
                
    def is_in_balance_sheet(self, name):
        """helper function for add_to to check to see if account is already in balance sheet"""
        category = self.categorize(name)
        if category == 1:
            for x in range(len(self.current_assets_list)):
                if name == self.current_assets_list[x].name:
                    return True
        if category == 2:
            for x in range(len(self.fixed_assets_list)):
                if name == self.fixed_assets_list[x].name:
                    return True
        if category == 3:
            for x in range(len(self.current_liabilities_list)):
                if name == self.current_liabilities_list[x].name:
                    return True
        if category == 4:
            for x in range(len(self.long_term_liabilities_list)):
                if name == self.long_term_liabilities_list[x].name:
                    return True
        if category == 5:
           for x in range(len(self.equities_list)):
               if name == self.equities_list[x].name:
                   return True
        return False
        
    def remove(self, name):
        """removes from the account"""
        category = self.categorize(name)
        if category == -1:
            print('No such account exists')
        elif isinstance(name,str) == False:
            print('The name is invalid')
        elif category == 1:
            for x in range(len(self.current_assets_list)):
                if name == self.current_assets_list[x].name:
                    self.current_assets_list.remove(self.current_assets_list[x])
        elif category == 2:
            for x in range(len(self.fixed_assets_list)):
                if name == self.fixed_assets_list[x].name:
                    self.fixed_assets_list.remove(self.fixed_assets_list[x])
        elif category == 3:
            for x in range(len(self.current_liabilities_list)):
                if name == self.current_liabilities_list[x].name:
                    self.current_liabilities_list.remove(self.current_liabilities_list[x])
        elif category == 4:
            for x in range(len(self.long_term_liabilities_list)):
                if name == self.long_term_liabilities_list[x].name:
                    self.long_term_liabilities_list.remove(self.long_term_liabilities_list[x])
        elif category == 5:
           for x in range(len(self.equities_list)):
               if name == self.equities_list[x].name:
                   self.equities_list.remove(self.equities_list[x])
        
    def print_account_options(self):
        """prints the account options"""
        print('These are the options to choose from: ')
        print('Assets')
        print('The options for current assets are: ')
        for x in range(len(self.current_assets)):
            print(self.current_assets[x])
        print()
        print('The options for fixed assets are: ')
        for x in range(len(self.fixed_assets)):
            print(self.fixed_assets[x])
        print()
        print('Liabilities')
        print('The options for current liabilities are: ')
        for x in range(len(self.current_liabilities)):
            print(self.current_liabilities[x])
        print()
        print('The options for long term liabilities are: ')
        for x in range(len(self.long_term_liabilities)):
            print(self.long_term_liabilities[x])
        print()
        print('Equities')
        print('The options for equities are: ')
        for x in range(len(self.equities)):
            print(self.equities[x])
        


