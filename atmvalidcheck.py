current_balance=int(input("enter the current balance"))
moneytowithdraw=int(input("enter the money to withdraw"))
if current_balance>moneytowithdraw and moneytowithdraw%100==0:
    print("isvalid")
else:
        print("not valid")
        #output
#enter the current balance10000
#enter the money to withdraw4500
#isvalid
    
