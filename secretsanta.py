# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 17:42:38 2021

@author: dylan
"""
people = [
    "Grandma",
    "Pam",
    "Amber",
    "Mike",
    "Ian",
    "Bobby",
    "Mace",
    "Marcy",
    "Erika",
    "Dylan",
    "Kyle"]

import random
def secretsanta(givers):
    count = 0
    while count != len(givers) - 1:
        takers = []
        Nums = []
        for giver in range(len(givers)):
            NewNum = False
            while NewNum == False:
                NewNum = True
                    #generating random number
                Num = random.randint(0, len(givers)-1)
                    #making sure number is not self
                if givers[Num] == givers[giver]:
                    NewNum = False
                    #making sure no numebr has been reused
                for n in range(len(Nums)):
                    if Nums[n] == Num:
                        NewNum = False
            Nums.append(Num)
            takers.append(givers[Nums[giver]])
            
            #Making sure it's a complete loop of all people instead of smaller loops
        count = 0
        i = 1
        while takers[i] != givers[1]:
            count += 1
            i = Nums[i]
        #printing results
    lengths = []
    for giver in givers:
        lengths.append(len(giver))
    Max = max(lengths)
    Max = max(Max, len("Giver Name"))
    print(str(' ')*(Max-len(str("Giver Name"))),"Giver Name","\t","Receiver Name")
    print("-------------------------------------")
    for i in range(len(givers)):
        print(str(' ')*(Max-len(str(givers[i]))),givers[i],"\t",takers[i])
            
secretsanta(people)                 