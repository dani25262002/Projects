
import mysql.connector
mydb=mysql.connector.connect( 
     host="localhost", 
     user="root", 
     password="dani",
     database="atm"
    ) 
mycursor=mydb.cursor() 
#Database:
# mycursor.execute("create database atm")
# print("db created successfully")


# def Create_table():
#      mycursor.execute("create table account(name varchar(255),pin int,phone_number varchar(255),account_balance int(255))")
#      print("TABLE CREATED SUCCESSFULLY")
# Create_table()

# def ADD_VALUE():
#      sql="insert into account(name,pin,phone_number,account_balance)values(%s,%s,%s,%s)"
#      val=("DANI",1234,7418146377,50000)
#      mycursor.execute(sql,val)
#      print("DATA INSERTED SUCCEFULLY")
#      mydb.commit()
# ADD_VALUE()

# def ADD_NEW_VALUE(name,pin,phone_number,account_balance):
#      sql="insert into account(name,pin,phone_number,account_balance)values(%s,%s,%s,%s)"
#      val=(name,pin,phone_number,account_balance)
#      mycursor.execute(sql,val)
#      print("DATA INSERTED SUCCEFULLY")
#      mydb.commit()
# ADD_NEW_VALUE(name=str(input("Enter the Account Name:")),pin=int(input("Enter the ATM PIN:")),phone_number=int(input("Enter the Phone Number:")),
# account_balance=int(input("Enter the Account Balance:")))


print("****************************WELCOME TO BangBank ATM***********************")

print("Please Select the Transaction process")

class OPTION:
    def option(self):
      print(">>1. Withdraw")
      print(">>2. Balance")
      print(">>3. Deposit")
      print(">>4. Other Services")
      print(">>5. Exit")
o=OPTION()

class OPTION1:
    def option1(self):
        print(">>1. Change PIN")
        print(">>2. Change Phone Number")
o1=OPTION1()         

class Withdraw:
    def WITHDRAW(self):
        try:
            w_amount=int(input("Enter Amount to be Withdraw:"))
            pin=int(input("Enter the PIN:"))
            a="select account_balance from account where pin=%s"
            data=(pin,)
            mycursor=mydb.cursor()
            mycursor.execute(a,data)
            myresult=mycursor.fetchone()
            ATM=myresult[0]-w_amount
            sql="UPDATE account SET account_balance=%s WHERE pin=%s"
            val=(ATM,pin)
            mycursor.execute(sql,val)
            print(f"{w_amount} Withdrawed Successfully")
            print(f"The Total Balance is:{ATM}")
            mydb.commit()
        except:
            print("***Please Enetr the PIN Number Correctly***")     
            w.WITHDRAW()
w=Withdraw()    

class Deposit:
    def DEPOSIT(self):   
        try:
            d_amount=int(input("Enter Amount to be Deposit:"))
            pin=int(input("Enter the PIN:"))
            a="select account_balance from account where pin=%s"
            data=(pin,)
            mycursor=mydb.cursor()
            mycursor.execute(a,data)
            myresult=mycursor.fetchone()
            ATM=myresult[0]+d_amount
            sql="UPDATE account SET account_balance=%s WHERE pin=%s"
            val=(ATM,pin)
            mycursor.execute(sql,val)
            print(f"{d_amount} Deposited Successfully")
            print(f"The Total Balance is:{ATM}")
            mydb.commit()
        except:
            print("***Please Enetr the PIN Number Correctly***") 
            d.DEPOSIT()   
d=Deposit()

class Current_Balance:
    def CURRENT_BALANCE(self):
        try:
            pin=int(input("Enter the PIN:"))
            a="select account_balance from account where pin=%s"
            data=(pin,)
            mycursor=mydb.cursor()
            mycursor.execute(a,data)
            myresult=mycursor.fetchone()
            print(f"The Current Balance is:{myresult}")
            mydb.commit()
        except:
            print("***Please Enetr the PIN Number Correctly***")     
c=Current_Balance()

class OTHER_SERVICE():
    def CHANGE_PIN(self):
        try:
            pin=int(input("Enter the PIN:"))
            mycursor.execute("SELECT pin FROM account")
            rows=mycursor.fetchall()
            if (pin,) in rows:
                sql="UPDATE account set pin=%s WHERE pin=%s"
                try:
                    new_pin=int(input("Enter the New PIN:"))
                    val=new_pin
                    mycursor.execute(sql,[val,pin])
                    print("PIN Number Changed Sucessfully")
                    mydb.commit()
                except:
                    print("***Please Enter the PIN Number Correctly***")
                    s.CHANGE_PIN()
            else:
                print("***Please Enter the PIN Number Correctly***")
                s.CHANGE_PIN()         
        except:
            print("***Please Enter the PIN Number Correctly***")
            s.CHANGE_PIN()               
    
    def CHANGE_PHONE_NUMBER(self):
        try:
            pin=int(input("Enter the PIN:"))
            mycursor.execute("SELECT pin FROM account")
            rows=mycursor.fetchall()
            if (pin,) in rows:
                sql="UPDATE account set phone_number=%s WHERE phone_number=%s"
                def new_num():
                    try:
                        current_phone_number=int(input("Enter the Current Phone Number:"))
                        new_phone_number=int(input("Enter the New Phone Number:"))
                        val=new_phone_number
                        mycursor.execute(sql,[val,current_phone_number])
                        print("Phone Number will be Changed in 24 hours")
                        mydb.commit()
                    except:
                        print("***Please Enter the Phone Number Correctly***")
                        new_num() 
                new_num()
            else:
                print("***Please Enter the PIN Number Correctly***")
                s.CHANGE_PHONE_NUMBER()   
        except:
            print("***Please Enter the PIN Number Correctly***")
            s.CHANGE_PHONE_NUMBER()
s=OTHER_SERVICE()                  
            
class PROCESS(OPTION,OPTION1,Withdraw,Deposit,Current_Balance,OTHER_SERVICE):
    def process(self): 
        o.option()
        user=int(input("Enter your option:"))
        if   user==1:
            w.WITHDRAW()
            print("***Thank you for your Service***")
            p.process()
        elif user==2:
            c.CURRENT_BALANCE()    
            print("***Thank you for your Service***")
            p.process()
        elif user==3:
            d.DEPOSIT()
            print("***Thank you for your Service***")
            p.process()
        elif user==4:
            s=OTHER_SERVICE()
            o1.option1()
            user1=int(input("Enter your option:"))
            if user1==1:
             s.CHANGE_PIN()
             print("***Thank you for your Service***")
             p.process()
            elif user1==2:
             s.CHANGE_PHONE_NUMBER()
             print("***Thank you for your Service***")
             p.process()
            else:
                print("***Enter the option from [1] [2]***")
                p.process() 
        elif user==5:
            print("***Thank you for your Service***")
            quit() 
        else:
            print("***Enter the option from [1] [2] [3] [4] [5]***") 
p=PROCESS() 
p.process()                 