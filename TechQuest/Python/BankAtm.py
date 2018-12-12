print("IBROTECH BANK PLC ATM")
print("")
print("")
def MY_ATM():
    attempt=0
    try:
        while attempt < 3:
            pin=int(input("PLEASE ENTER YOUR 4 DIGIT PIN: ")) 
            if pin==1234:    
                print("ACCESS GRANTED")
                print("")
                print("")
                print("WELCOME DEAR COSTUMER")
                print("")
                print("")
                balance=100000
                request=input("PLEASE SELECT AN OPTION \n \n(a) WITHDRAWAL \n(b) DEPOSIT \n(c) CHECK BALANCE \n(d) QUICKTELLER \n(e) CHANGE PIN \n(f) EXIT\n")
                if (request=="a") or (request=="A"):
                    account=input("PLEASE SELECT AN ACCOUNT TYPE \n(a) SAVINGS \n(b) CURRENT \n(c) CREDIT\n")
                    if (account=="a") or (account=="A"):
                        amount=int(input("Enter the Amount you want to withdraw: "))
                        change=balance-amount
                        print("")
                        print("")
                        if amount>balance:
                            print("INSUFFICIENT FUND")
                        elif amount<=balance:
                            print("TAKE YOUR CASH")
                            print ("your balance is =",change)
                            print("")
                            print("THANK YOU")
                        else:
                            print("please enter amount")

                    elif (account=="b") or (account=="B"):
                        amount=int(input("Enter the Amount you want to withdraw: "))
                        change=balance-amount
                        print("")
                        print("")
                        if amount>balance:
                            print("INSUFFICIENT FUND")
                        elif amount<=balance:
                            print("TAKE YOUR CASH")
                            print ("your balance is =",change)
                            print("")
                            print("THANK YOU")
                        else:
                            print("please enter amount")
                

                    elif account=="c":
                        amount=int(input("Enter the Amount you want to withdraw: "))
                        change=balance-amount
                        print("")
                        print("")
                        if amount>balance:
                            print("INSUFFICIENT FUND")
                        elif amount<=balance:
                            print("TAKE YOUR CASH")
                            print ("your balance is =",change)
                            print("")
                            print("THANK YOU")
                        else:
                            print("please enter amount")
                    else:
                        print("PLEASE SELECT AN ACCOUNT TYPE AND TRY AGAIN")
                    anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                    if (anotherTransaction == "a") or (anotherTransaction == "A"):
                        return MY_ATM()
                    else:
                        print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")

                elif (request=="b") or (request=="B"):
                        account=input("PLEASE SELECT AN ACCOUNT TYPE \n(a) SAVINGS \n(b) CURRENT \n(c) CREDIT\n")
                        if (account=="a")or (account=="A"):
                            deposit=int(input("Enter the Amount you want to Deposit ="))
                            result=balance+deposit
                            print("")
                            print("")
                            print("Your money Has been saved succesfully and your balance now is =",result)
                            print("")
                            print("THANK YOU")
                            
                        elif (account=="b") or (account=="B"):
                            deposit=int(input("Enter the Amount you want to deposit ="))
                            change=balance+deposit
                            print("")
                            print("")
                            print("TAKE YOUR CASH")
                            print("your balance is =",change)
                            print("")
                            print("THANK YOU")
                            
                        elif (account=="c") or (account=="C"):
                            deposit=int(input("Enter the Amount you want to deposit ="))
                            change=balance+deposit
                            print("")
                            print("")
                            print("TAKE YOUR CASH")
                            print ("your balance is =",change)
                            print("")
                            print("THANK YOU")
                        else:

                            print("PLEASE SELECT AN ACCOUNT TYPE AND TRY AGAIN")
                        anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                        if (anotherTransaction == "a") or (anotherTransaction == "A"):
                            return MY_ATM()
                        else:
                            print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")

                            
                elif (request=="c") or (request=="C"):
                        account=input("PLEASE SELECT AN ACCOUNT TYPE \n(a) SAVINGS \n(b) CURRENT \n(c) CREDIT\n")
                        if (account=="a") or (account=="A"):
                            print("YOUR BALANCE IS =",balance)
                            print("")
                            print("THANK YOU")
                        if (account=="b") or (account=="B"):
                            print("YOUR BALANCE IS =",balance)
                            print("")
                            print("THANK YOU")
                        if (account=="c") or (account=="C"):
                            print("YOUR BALANCE IS =",balance)
                            print("")
                            print("THANK YOU")
                        else:
                            print("PLEASE SELECT AN ACCOUNT TYPE AND TRY AGAIN")
                        anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                        if (anotherTransaction == "a") or (anotherTransaction == "A"):
                            return MY_ATM()
                        else:
                            print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")

                            
                elif (request=="d") or (request=="D"):
                        teller=input("PLEASE SELECT FROM THE UNERLISTED OPTIONS \n \n(a) AIRTIME RECHARGE \n \n(b) BANK TRANSFER \n \n(c) PAY BILLS\n")
                        if (teller=="a"):
                            name=input("SELECT THE LINE YOU WISH TO RECHARGE \n(a) AIRTEL \n(b) MTN \n(c) GLO \n(d) ETISALAT\n")
                            if (name=="a"):
                                amount=int(input("PLEASE ENTER THE AMOUNT YOU WANT TO RECHARGE: "))
                                print("")
                                phone=input("PLEASE ENTER THE PHONE NUMBER YOU WANT TO RECHARGE: ")
                                leftover=balance-amount
                                print("")
                                print("NOTIFICATION WILL BE SENT TO YOU SHORTLY")
                                print("")
                                print("")
                                print ("your balance is =",leftover)
                                print("")
                                print("PLEASE TAKE YOUR CARD")
                                print("")
                                print("THANK YOU")
                                
                            elif (name=="b"):
                                amount=int(input("PLEASE ENTER THE AMOUNT YOU WANT TO RECHARGE: "))
                                print("")
                                phone=input("PLEASE ENTER THE PHONE NUMBER YOU WANT TO RECHARGE: ")
                                leftover=balance-amount
                                print("")
                                print("NOTIFICATION WILL BE SENT TO YOU SHORTLY")
                                print("")
                                print("")
                                print ("your balance is =",leftover)
                                print("")
                                print("THANK YOU")
                                
                            elif (name=="c"):
                                amount=int(input("PLEASE ENTER THE AMOUNT YOU WANT TO RECHARGE: "))
                                print("")
                                phone=input("PLEASE ENTER THE PHONE NUMBER YOU WANT TO RECHARGE: ")
                                leftover=balance-amount
                                print("")
                                print("NOTIFICATION WILL BE SENT TO YOU SHORTLY")
                                print("")
                                print("")
                                print ("your balance is =",leftover)
                                print("")
                                print("THANK YOU")
                                
                            elif (name=="d"):
                                amount=int(input("PLEASE ENTER THE AMOUNT YOU WANT TO RECHARGE: "))
                                print("")
                                phone=input("PLEASE ENTER THE PHONE NUMBER YOU WANT TO RECHARGE: ")
                                leftover=balance-amount
                                print("")
                                print("NOTIFICATION WILL BE SENT TO YOU SHORTLY")
                                print("")
                                print("")
                                print ("your balance is =",leftover)
                                print("")
                                print("THANK YOU")
                                
                        
                        if (teller=="b"):
                                    transfer=input("SELECT THE BANK YOU WISH TO TRANFER TO \n \n(a) ACCESS BANK \n \n(b) DIAMOND BANK \n \n(c) FIRST BANK \n \n(d) STANBIC IBTC BANK \n \n(e) FCMB BANK \n \n(f) KEYSTONE BANK \n \n(g) BANK OF THE NORTH \n \n(h) HABIB BANK \n \n(i) UNION BANK \n \n(j) GT BANK \n \n(k) POLARIS BANK \n \n(l) STERLING BANK \n \n(m) ECO BANK \n \n(n) UBA BANK \n \n(o) WEMA BANK \n \n(p) ZENITH BANK\n")
                                    if (transfer=="a"or"b"or"c"or"d"or"e"or"e"or"f"or"g"or"h"or"i"or"j"or"k"or"l"or"m"or"n"or"o"or"p"):
                                        print("")
                                        account=input("PLEASE SELECT AN ACCOUNT TYPE \n(a) SAVINGS \n(b) CURRENT \n(c) CREDIT\n")
                                        if (account=="a")or(account=="b")or(account=="c"):
                                            types=input("WHAT IS THE DESTINATION ACCOUNT TYPE \n(a) SAVINGS \n(b) CURRENT \n(c) CREDIT\n")
                                            if(types=="a")or(types=="b")or(types=="c"):
                                                names=input("PLEASE ENTER THE ACCOUNT NUMBER YOU WISH TO TRANSFER TO: ")
                                                print("")
                                                Num=input("PLEASE ENTER YOUR PHONE NUMBER: ")
                                                print("")
                                                amounts=int(input("PLEASE ENTER THE AMOUNT: "))
                                                print("")
                                                print("PLEASE CONFIRM YOUR DETAILS")
                                                print("")
                                                print("ACCOUNT NUMBER: ",names)
                                                print("PHONE NUMBER: ",Num)
                                                print("AMOUNT: " ,amounts)
                                                print("")
                                                cont=input("DO YOU WISH TO CONTINUE \n(a) YES \n(b) NO\n")
                                                print("")
                                                if cont=="a":
                                                    print("")
                                                    print("TRANSACTION SUCCESFULL")
                                                    print("")
                                                    newBalance=balance-amounts
                                                    print("YOUR BALANCE IS",newBalance)
                                                    print("")
                                                    print("THANK YOU")
                                                else:
                                                    print("TRANSACTION CANCELLED")
                                                    print("")
                                                    return(MY_ATM())
                                                
                                            else:
                                                print("PLEASE SELECT AN OPTION")
                                        else:
                                            print("PLEASE SELECT AN OPTION")
                                    else:
                                        print("PLEASE SELECT AN OPTION")
                                        
                        if (teller=="c"):
                                    bills=input("SELECT THE BILL YOU WANT TO PAY \n(a) PHCN \n(b) WATER BILL \n(c) FIRS \n(d) DSTV \n(e) GOTV\n")
                                    if (bills=="a"):
                                        print("")
                                        number=input("PLEASE ENTER YOUR METER NUMBER: ")
                                        name=input("PLEASE ENTER YOUR SURNAME: ")
                                        price=input("PLEASE ENTER THE AMOUNT: ")
                                        print("PLEASE CONFIRM YOUR DETAILS: ")
                                        print("")
                                        print("METER NUMBER: ",number)
                                        print("SURNAME: ",name)
                                        print("AMOUNT:" ,price)
                                        print("")
                                        cont=input("DO YOU WISH TO CONTINUE \n(a) YES \n(b) NO\n")
                                        print("")
                                        if cont=="a":
                                            print("TRANSACTION SUCESSFULL")
                                        else:
                                            print("TRANSACTION CANCELLED")
                                            print("")
                                            return(MY_YATM())
                                    elif (bills=="b"):
                                        meter=input("PLEASE ENTER YOUR METER NUMBER: ")
                                        name=input("PLEASE ENTER YOUR SURNAME: ")
                                        price=input("PLEASE ENTER THE AMOUNT: ")
                                        print("PLEASE CONFIRM YOUR DETAILS: ")
                                        print("")
                                        print("METER NUMBER: ",meter)
                                        print("SURNAME: ",name)
                                        print("AMOUNT:", price)
                                        print("")
                                        cont=input("DO YOU WISH TO CONTINUE \n(a) YES \n(b) NO\n")
                                        print("")
                                        if cont=="a":
                                            print("TRANSACTION SUCESSFULL")
                                        else:
                                            print("TRANSACTION CANCELLED")
                                            print("")
                                            return(MY_ATM())
                                    elif(bills=="c"):
                                        reg=input("PLEASE ENTER YOUR REGISTRATION NUMBER: ")
                                        name=input("PLEASE ENTER YOUR SURNAME: ")
                                        price=input("PLEASE ENTER THE AMOUNT: ")
                                        print("PLEASE CONFIRM YOUR DETAILS: ")
                                        print("")
                                        print("REGISTRATION NUMBER: ",reg)
                                        print("SURNAME: ",name)
                                        print("AMOUNT:" ,price)
                                        print("")
                                        cont=input("DO YOU WISH TO CONTINUE \n(a) YES \n(b) NO\n")
                                        print("")
                                        if cont=="a":
                                            print("TRANSACTION SUCESSFULL")
                                        else:
                                            print("TRANSACTION CANCELLED")
                                            print("")
                                            return(MY_ATM())
                                    elif(bills=="d")or(bills=="e"):
                                        card=input("PLEASE ENTER YOUR CARD NUMBER: ")
                                        name=input("PLEASE ENTER YOUR SURNAME: ")
                                        price=input("PLEASE ENTER THE AMOUNT: ")
                                        print("PLEASE CONFIRM YOUR DETAILS: ")
                                        print("")
                                        print("CARD NUMBER: ",card)
                                        print("SURNAME: ",name)
                                        print("AMOUNT:" ,price)
                                        print("")
                                        cont=input("DO YOU WISH TO CONTINUE \n(a) YES \n(b) NO\n")
                                        print("")
                                        if cont=="a":
                                            print("TRANSACTION SUCESSFULL")
                                        else:
                                            print("TRANSACTION CANCELLED")
                                            print("")
                                            return(ATM())
                                    else:
                                        print("PLEASE SELECT AN OPTION")
                                        print("")
                                        return (MY_ATM())
                        anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                        if anotherTransaction == "a":
                            return MY_ATM()
                        else:
                            print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")

                    
                elif (request=="e"):
                    oldPin =input("PLEASE ENTER YOUR OLD PIN: ")
                    newPin =input("PLEASE ENTER YOUR NEW PIN: ")
                    confirmPin =input("PLEASE ENTER RE-ENTER YOUR NEW PIN: ")
                    if newPin == confirmPin:
                        pin=confirmPin
                        print("PIN CHANGED SUCESSFULLY")
                        print("THANK YOU")
                    else:
                        print("NEW PIN NOT SAME AS RE-ENTER PIN")

                        
                elif(request=="f"):
                    print("PLEASE TAKE YOUR CARD")
                    print("THANK YOU FOR BANKING WITH US")
                else:
                    print("please select an option")
    
                
            else:
                print("")
                print("INCORRECT PIN PLEASE CALM DOWN AND RE-ENTER YOUR PIN!")
                print("")
                attempt+= 1
        if attempt == 3:
            print("CARD BLOCKED AND RETAINED")
    except KeyboardInterrupt:
        print("closing good bye")
       
print(MY_ATM())

