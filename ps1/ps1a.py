# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 02:56:44 2018

@author: BARUWA1
"""

# total_cost, portion_down_payment = 0.25
# current_savings = "$0"
# annual return r=current_savings*r/12
# r = 0.04
# annual salary
# portion_saved
# increment in savings = r*(1 + annual-salary/12)

current_savings = 0.0
r = 0.04

annual_salary = float(input("Enter your annual salary: "))
per_cent_portion = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25 * total_cost
portion_saved = per_cent_portion * annual_salary/ 12

x = portion_down_payment
c = 0.0
a = annual_salary
epsilon = 500
months = 0

# Body of while loop
while c <= x:
     c += (c *r/12) + (portion_saved)
     months +=1
     print ("current_savings = ", c, "         iteration: ", months)

print ('Number of months: ', months)

    
    


