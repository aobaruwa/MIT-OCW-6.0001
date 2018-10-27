# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 22:02:50 2018

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

annual_salary = float(input("Enter your starting annual salary: "))
per_cent_portion = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

portion_down_payment = 0.25 * total_cost


x = portion_down_payment
c = 0.0
a = annual_salary

months = 0
portion_saved = per_cent_portion * a/ 12.0

# continue to save until current savings is less than or equal to down_payment
while c <= x:
    
    portion_saved = per_cent_portion * a/ 12.0
    c += (c *r/12) + (portion_saved)
    months +=1
    if months % 6 == 0:      
        a += a * semi_annual_raise
    print("c =", c)

print ('Number of months: ', months, "c =", c)


    


    
    


