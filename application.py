"""This application will help the user
to choose the destination that pleases, 
a long list of countries and select the one you like"""

import os
import sys

dic = {}
coun = []
cap = []
pais_capital = {}
def ask():
    pre = raw_input("Do you want insert another country y/n \n")
    pre.lower()
    if pre == "y" or pre == "yes":
        country()
    elif pre == "n" or pre == "no":
        MENU()
def OnlyCount():
    print "     >>>Country<<< \n"
    for key in pais_capital:
        print key.center(20)
    raw_input("Press enter to Continue")
    MENU()
    Clear()
def OnlyCaps():
    print "     >>>Capital<<<\n"
    for i in pais_capital:
        print i.center(20)
    raw_input("Press Enter to Continue")
    MENU()
    Clear()
def country():
    os.system("cls")
    os.system("clear")
    var = True
    while var == True:
        Count = raw_input("Please insert a Country \n")
        Count = str(Count).title()
        if  Count.isalpha() == True or " " in Count:
            pais_capital[Count] = Count
            var = False
        else:
            print "I don't understand the instruction"
            var = True
            raw_input("Press Enter to Continue")
    var2= True       
    while var2 == True:        
        capi = raw_input(">>>Please insert a Capital<<<\n")
        capi = capi.title()
        if  capi.isalpha() == True or " " in capi:
            pais_capital[Count] = capi
            var2 = False
        else:
            print "I don't understand the instruction"
            var2 = True   
    ask()
    MENU()
def Clear():
    os.system("cls")
    os.system("clear")
def MENU():
    while True:
        os.system("cls")
        os.system("clear")
        print """////////////////////////////////////////"""
        print """/       COUNTRIES AND CAPITALS         /"""
        print """////////////////////////////////////////"""
        print "  1) Insert a Country"
        print "  2) Countries list"
        print "  3) Capitals list"
        print "  4) Countries and Capital list"
        print "  5) Countries and Capitals ordered by Capital"
        print "  6) All by mail"
        print "  7) Exit"
        DATA = raw_input(">>>Select an Option<<<\n")
        DATA = DATA.lower()
        if DATA == "1" or DATA == "country":
            country()
        elif DATA == "2" or DATA == "Countries":
            OnlyCount()
        elif DATA == "3" or DATA == "Capitals":
            OnlyCaps()
        elif DATA == "4":
            CountriesCapitalLists()
        elif DATA == "5":
            Ordered()
        elif DATA == "6":
            Mail()
        elif DATA == "7" or DATA == "exit":
            EXIT()
        else:
            print "I can't understand you, please select a valid option"
            raw_input("Press enter to insert another option\n")
            os.system("cls")
            os.system("clear")    
MENU()