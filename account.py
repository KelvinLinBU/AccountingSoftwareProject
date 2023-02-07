#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Account:
    """This is the helper class that represents an account"""
    
    def __init__(self, amount, name, category):
        """constructor for the account class"""
        self.amount = amount
        self.name = name
        self.category = category
    