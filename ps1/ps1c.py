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


# prompt user for his annual_salary
annual_salary = float(input("Enter your starting annual salary: "))

current_savings = 0.0
r = 0.04
total_cost = 1000000.0
portion_down_payment = 0.25 * total_cost
semi_annual_raise = 0.07


x = portion_down_payment
c = 0.0
a = annual_salary              
epsilon = 100
months = 0
steps = 0


low_guess = 0.0
high_guess = 10000
percent_portion = (low_guess + high_guess) / 2.0

while True:
    #guess and Check if a particular percentage is too big or too small and fix it as needed
    while months < 36:
        
        portion_saved = percent_portion * a/ (12.0 * 10000)
        c += (c *r/12) + (portion_saved)
        months +=1
        if months % 6 == 0:      
            a += a * semi_annual_raise
        if c >= x:
            #print("Just too much!", "months =", months," percent =", percent_portion)
            steps += 1
            high_guess = percent_portion 
            break
        #low_guess = percent_portion

        # print(months,"  low_guess =", low_guess,  "percent_portion =", percent_portion,"high_guess =",high_guess, "c =", c)
    if c < x:
       #print("Just too small!", "months =", months," percent =", percent_portion)
       low_guess = percent_portion
       steps += 1
    percent_portion = (low_guess + high_guess) / 2.0
    c = 0.0
    months = 0
    a = annual_salary    
        
    #low_guess = percent_portion 
    if percent_portion >= 9500:
        print("It is not possible to pay the down payment in three years.")
        break
     
    if abs(c - x) <= 100 or abs(high_guess - low_guess) < 0.5 :
        
        #print("low_guess =", low_guess/10000, "high_guess =", high_guess/10000, "c =", c, "months =",months)
        print("Best savings rate: {:,.4f}".format(percent_portion/10000))
        print("Steps in bisection search:", steps)
        break
    



    

    


