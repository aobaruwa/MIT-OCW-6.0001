# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 11:49:30 2018

@author: BARUWA1
"""
#    def getCombo(sequence, group)


#def getAllSubsets(sequence):
#    Lists = []
#    
#    lst[0] = []
#    seq = ([] + list(sequence))
#    if len(lst) == 1:
#        return lst
#
#    else:
#        for e in range(len(seq)):
#            without = seq[0 :e] + seq[e + 1 :]
#            only = e
#
#def getAllSubsets(sequence):
sequence = [1,2,3,4]
elem = [[]]
#    buffer = []
temp = elem
print (temp)

seq = elem + list(sequence)
print(seq)
#    without = seq[0 :i] + seq[i + 1 :]
#    
for i in range(len(sequence)):    
#    if i == 0:
#        temp += elem
#        print(temp)
#    else:
#            temp.append[seq[i]]
    for t in temp:
        temp.append(seq[i] + t)

print(temp)       
    

                
                
                
                
                