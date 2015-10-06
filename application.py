"""This application will help the user
to choose the destination that pleases, 
a long list of countries and select the one you like"""

<<<<<<< HEAD
import os
import sys
=======
from collections import OrderedDict
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import os
import sys
import smtplib
import getpass
>>>>>>> 4dd000450406ca2834037bcb354185c69e68b4d0

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
<<<<<<< HEAD
    MENU()
    Clear()
def OnlyCaps():
    print "     >>>Capital<<<\n"
    for i in pais_capital:
        print i.center(20)
    raw_input("Press Enter to Continue")
    MENU()
    Clear()
=======
def OnlyCaps():
    print "     >>>Capital<<<\n"
    for i in pais_capital:
        print pais_capital[i].center(20)
    raw_input("Press Enter to Continue")
    Clear()
    MENU()
>>>>>>> 4dd000450406ca2834037bcb354185c69e68b4d0
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
<<<<<<< HEAD
=======
def CounCapList():
    print """COUNTRY================CAPITAL"""
    for key in pais_capital:
        print key.center(7), pais_capital[key].center(34) +"\n"
    raw_input("press enter")
    MENU()
    Clear()
def orden():
    print """==============================================="""
    print """|Countries                            Capitals|"""
    ordered = OrderedDict(sorted(pais_capital.items(), key=lambda x: x[1:]))
    for key, value in ordered.items():
        print key + "                                        " + value
    raw_input("Press Enter to Continue")    
    Clear()
def email():
    print "Send email by gmail"

    fromaddr = raw_input("Count from gmail: ")
    password = getpass.getpass("Password: ")
    toaddrs = raw_input("to: ")
    #asunto = raw_input("subject, from message: ")
    body = "Countries===========Capitals\n"
    for msg in pais_capital:
        body = body + str(msg).center(20) +str(pais_capital[msg]).center(30) + "\n" 
    msg = MIMEMultipart()
    msg['From'] = fromaddr #This saves the mail of the sender
    msg['To'] = toaddrs  #This saves the mail of the receiver
    msg['Subject'] = "Countries and Capitals"  #This saves the subject
    msg.attach(MIMEText(body, 'plain')) #This saves the message

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(fromaddr,password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
        print "yes"
        raw_input("press enter")
    except (smtplib.SMTPAuthenticationError):
        print "No se envio nada"
def EXIT():
    raw_input("press enter to continue")
    sys.exit()
>>>>>>> 4dd000450406ca2834037bcb354185c69e68b4d0
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
<<<<<<< HEAD
        elif DATA == "4":
            CountriesCapitalLists()
        elif DATA == "5":
            Ordered()
        elif DATA == "6":
            Mail()
=======
        elif DATA == "4" or DATA == "All":
            CounCapList()
        elif DATA == "5":
            orden()
        elif DATA == "6":
            email()
>>>>>>> 4dd000450406ca2834037bcb354185c69e68b4d0
        elif DATA == "7" or DATA == "exit":
            EXIT()
        else:
            print "I can't understand you, please select a valid option"
            raw_input("Press enter to insert another option\n")
            os.system("cls")
            os.system("clear")    
MENU()