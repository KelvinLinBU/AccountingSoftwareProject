#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class RetainedEarnings:
    """This is the class for the statement of retained earnings used in financial accounting"""
    
    def __init__(self, company_name, date, beginning_retained_earnings, net_income, dividends_declared):
        """This is the constructor for the RetainedEarnings class"""
        self.company_name = company_name
        self.date = date
        self.beginning_retained_earnings = beginning_retained_earnings
        self.net_income = net_income
        self.dividends_declared = dividends_declared
        
    def __repr__(self):
        """Returns the string representation of the Retained Earnings Object"""
        s = self.company_name + '\n'
        s += 'Statement of Retained Earnings' + '\n'
        s += "As of: " + self.date + '\n' 
        s += '-----------------------------------------------------------' + '\n'
        s +='Beginning Retained Earnings: ' + str(self.beginning_retained_earnings) + '\n'
        if self.net_income > 0:
            s += 'Plus: Net Income ' + str(self.net_income) + '\n'
        else:
            s += 'Plus: Net Loss ' + str(self.net_income) + '\n'
        s += 'Beginning Retained Earnings + Net Income(Loss): ' + str((self.beginning_retained_earnings + self.net_income)) + '\n'
        s += 'Less: Dividends Declared ' + str(self.dividends_declared) + '\n'
        s += 'Retained Earnings ' + self.date + ': ' + str(self.ending_retained_earnings())
        return s
        
    def ending_retained_earnings(self):
        """returns the ending balance of retained earnings"""
        var = self.beginning_retained_earnings + self.net_income
        var -= self.dividends_declared
        return var
        