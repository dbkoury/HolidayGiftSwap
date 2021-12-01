# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 00:01:20 2021

@author: dylan
"""


import random
import smtplib 

#read excel file into python with names and emails
people = ['Ya Boi', 'Harambe']
email = ['fakeemail@us.gov','tomhanks@aol.com']
emailid = 'EMAIL_ID'
emailpass = 'EMAIL_PASSWORD'

def secretsanta(givers, emails, eid, epass):
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
    
    try: 
        #Create your SMTP session 
        smtp = smtplib.SMTP('smtp.gmail.com', 587) 
    
       #Use TLS to add security 
        smtp.starttls() 
    
        #User Authentication 
        smtp.login(eid,epass)
    
        for i in range(len(givers)):
            #Defining The Message 
            message = "Subject: {}\n\n{}".format("MSBA Gift Swap","Hello " + str(givers[i]) + "!\n\nYour gift swap recipient is " + str(takers[i]) + "\n\nHappy Holidays!")
        
            #Sending the Email
            smtp.sendmail(eid, str(emails[i]),str(message)) 
    
        #Terminating the session 
        smtp.quit() 
        print ("Email sent successfully!") 
    
    except Exception as ex: 
        print("Something went wrong....",ex)
        
        
secretsanta(people,email,emailid,emailpass)
