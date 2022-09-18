from abc import ABC,abstractmethod
from re import A
from unicodedata import category
import random
from optparse import Values
import mysql.connector
mydb=mysql.connector.connect(
     host="localhost",
     user="root",
     password="dani",
     database="hotelmanagement"
     )
mycursor=mydb.cursor()

#------------------------------------------Abstraction----------------------------------------------------
class Summary:
    @abstractmethod
    def Redirection(self):pass
    @abstractmethod
    def Star(self):pass
    @abstractmethod
    def VIP(self):pass
    @abstractmethod
    def Executive(self):pass
    @abstractmethod
    def single(self):pass
    @abstractmethod
    def double(self):pass
    @abstractmethod
    def triple(self):pass
    @abstractmethod
    def quad(self):pass
    @abstractmethod
    def Redirection2(self):pass
    @abstractmethod
    def veg(self):pass
    @abstractmethod
    def Non_veg(self):pass
    @abstractmethod
    def North_indians(sef):pass
    @abstractmethod
    def chinese(self):pass

#------------------------------------------RoomsBooking--------------------------------------------------
#database:
#mycursor.execute("Create database hotelmanagenment")
#print("Database created successfully")
#Tables:
#mycursor.execute("create table Category (category varchar(250),Description varchar(255)) ")
#print("Table created succesfully")
# mycursor.execute("create table user (Name varchar(250),Age int,number int(10),address varchar(250))")
# print("Table created succesfully")
# mycursor.execute("create table star (sl_no int,Package varchar(250),cost_per_day int)")
# print("Table created succesfully")
# mycursor.execute("create table VIP (sl_no int,Package varchar(250),cost_per_day int)")
# print("Table created succesfully")
# mycursor.execute("create table execute (sl_no int,Package varchar(250),cost_per_day int)")
# print("Table created succesfully")

#Category:
# sql="insert into Category(category,Description) values (%s,%s)"
# val=("STAR","star category is for only cine stars and they must have star id.They will be provided special protection with special features.")
#mycursor.execute(sql,val)
#mydb.commit()
# sql="insert into Category(category,Description) values (%s,%s)"
# val=("VIP","VIP category is for only VIPs and they must have VIP card.They will be provided special protection with special features.")
# mycursor.execute(sql,val)
# mydb.commit()
# print("data inserted succesfully.")
# sql="insert into Category(category,Description) values (%s,%s)"
# val=("EXECUTIVE","Executive category is for no star and no vip people.No special protection and features will be provided.")
# mycursor.execute(sql,val)
# mydb.commit()
# print("data added succesfully")

#STAR:
# sql="insert into Star(sl_no,Package,cost_per_day) values (%s,%s,%s)"
# val=("1","Single","100000")
# mycursor.execute(sql,val)
# mydb.commit()
# sql="insert into Star(sl_no,Package,cost_per_day) values (%s,%s,%s)"
# val=("2","double","150000")
# mycursor.execute(sql,val)
# mydb.commit()
# sql="insert into Star(sl_no,Package,cost_per_day) values (%s,%s,%s)"
# val=("3","Triple","200000")
# mycursor.execute(sql,val)
# mydb.commit()
# sql="insert into Star(sl_no,Package,cost_per_day) values (%s,%s,%s)"
# val=("4","Quad","300000")
# mycursor.execute(sql,val)
# mydb.commit()
# print("star data inserted succesfully")

#VIP:
# sql="insert into vip(sl_no,Package,cost_per_day) values (%s,%s,%s)"
# val=("1","Single","10000")
# mycursor.execute(sql,val)
# mydb.commit()
# sql="insert into vip(sl_no,Package,cost_per_day) values (%s,%s,%s)"
# val=("2","double","15000")
# mycursor.execute(sql,val)
# mydb.commit()
# sql="insert into vip(sl_no,Package,cost_per_day) values (%s,%s,%s)"
# val=("3","Triple","20000")
# mycursor.execute(sql,val)
# mydb.commit()
# sql="insert into vip(sl_no,Package,cost_per_day) values (%s,%s,%s)"
# val=("4","Quad","30000")
# mycursor.execute(sql,val)
# mydb.commit()
# print("vip data inserted succesfully")

#Executive:
# sql="insert into execute(sl_no,Package,cost_per_day) values (%s,%s,%s)"
# val=("1","Single","1000")
# mycursor.execute(sql,val)
# mydb.commit()
# sql="insert into execute(sl_no,Package,cost_per_day) values (%s,%s,%s)"
# val=("2","double","1500")
# mycursor.execute(sql,val)
# mydb.commit()
# sql="insert into execute(sl_no,Package,cost_per_day) values (%s,%s,%s)"
# val=("3","Triple","2000")
# mycursor.execute(sql,val)
# mydb.commit()
# sql="insert into execute(sl_no,Package,cost_per_day) values (%s,%s,%s)"
# val=("4","Quad","3000")
# mycursor.execute(sql,val)
# mydb.commit()
# print("Executive data inserted succesfully")

def IntroPage():
    print("---------------------------------Welcome To BlueStar Hotel---------------------------------")
    print()        
    print("------------This is the Automation system for Booking ROOMs and ordering FOOds-------------")
    print()
    print("If you are new user,Enter NEW and Enter your details below")
    print("If you are already a registered user,Enter USER ")
    user_input=input("Your Response: ").upper().strip()
    if user_input=="NEW":
        name=input("Name: ").upper().strip()
        Age=int(input("Age: "))
        number=int(input("contact number:"))
        address=input("Address: ")
        sql="insert into user(Name,Age,number,address) values (%s,%s,%s,%s)"
        val=(name,Age,number,address)
        mycursor.execute(sql,val)
        mydb.commit()
        #sql
        print("Your information is collected succesfully")
        print("User id created")
        print()
    elif user_input=="USER":
        user_num=(input("Enter Your Registered Number: "))
        print()
        mycursor.execute(f"select * from user where number={user_num}")
        if True:
            result=mycursor.fetchall()
            for i in result:
                print(i)
        else:
            print("Please enter valid number.")
            IntroPage()
        print()
        user_input2=input("If you want update your registered phone number,Please Enter YES else NO: ").upper().strip()
        if user_input2=="YES": 
            user_input3=int(input("Please Enter your new number: "))
            sql=f"update user set number={user_input3} where number={user_num}"
            mycursor.execute(sql)
            mydb.commit()
            print("Number updated successfully")
            print()
        elif user_input2=="NO":pass
        else:
            print("Enter valid input")
            IntroPage()
        user_input4=input("If You want to delete user id,Enter Yes else NO: ").upper().strip()
        if user_input4=="YES":
            sql=f"delete from user where number={user_num}"
            mycursor.execute(sql)
            print("User id deleted successfully")
            IntroPage()
        elif user_input4=="NO":pass
        else:
            print("Please enter valid input")
            IntroPage()
    else:
        print("Please enter valid input")
        IntroPage()
    print("Please select and enter number of one of the either options listed below: ")
    print("1 for Booking Rooms\n2 for Ordering Foods")
IntroPage()


try:
    Input1=int(input("Your Response: "))
except:
    print("Please Enter only 1 or 2")
    Input1=int(input("Your Response: "))

class RoomsBooking(Summary):
    def Redirection(self):
        print("-----------------------------You are now redirected to ROOMS BOOKING automation page-------------------------------------------")
        print()
        print("Here are the categories of Rooms:")
        print()
        print("\'category\',\'description\'")
        mycursor.execute("select * from category")
        result=mycursor.fetchall()
        for i in result:
            print(i)
        #sql
    def Star(self):
        print()
        print("You selected Star category.")
        print()
        print("Here are the Packages coming under this category listed below...")
        print()
        print('sl_no',' Package',' Cost Per Day')
        print()
        mycursor.execute("select * from star")
        result=mycursor.fetchall()
        for i in result:
            print(i)
        #sql
    def VIP(self):
        print()
        print("You selected VIP category.")
        print()
        print("Here are the Packages coming under this category listed below...")
        print()
        print('sl_no',' Package',' Cost Per Day')
        print()
        mycursor.execute("select * from vip")
        result=mycursor.fetchall()
        for i in result:
            print(i)
        #sql
    def Executive(self):
        print()
        print("You selected Executive category.")
        print()
        print("Here are the Packages coming under this category listed below...")
        print()
        print('sl_no',' Package','Cost Per Day')
        print()
        mycursor.execute("select * from execute")
        result=mycursor.fetchall()
        for i in result:
            print(i)
        #sql
    def single(self):
        print()
        print("You selected single room package.")
        print()
        days=int(input("Please enter no. of days of stay: "))
        print()
        print("Your booking process is over.\nYour Payment process will be done separately.\n-------------------Thank you for Booking-------------------\n----------------------------------------------Enjoy the stay :)----------------------------------------")
    def double(self):
        print()
        print("You selected Double room package.")
        print()
        days=int(input("Please enter no. of days of stay: "))
        print()
        print("Your booking process is over.\nYour Payment process will be done separately.\n-------------------Thank you for Booking-------------------\n----------------------------------------------Enjoy the stay :)----------------------------------------")
    def triple(self):
        print()
        print("You selected triple room.")
        print()
        days=int(input("Please enter no. of days of stay: "))
        print()
        print("Your booking process is over.\nYour Payment process will be done separately.\n-------------------Thank you for Booking-------------------\n----------------------------------------------Enjoy the stay :)----------------------------------------")
    def quad(self):
        print()
        print("You selected quad room.")
        print()
        days=int(input("Please enter no. of days of stay: "))
        print()
        print("Your booking process is over.\nYour Payment process will be done separately.\n-------------------Thank you for Booking-------------------\n----------------------------------------------Enjoy the stay :)----------------------------------------")

if Input1==1:
    r=RoomsBooking()
    r.Redirection()
    print()
    Input2=input("Please select your desired category: ").strip().upper()
    if Input2=="STAR":
        r.Star()
    elif Input2=="VIP":
        r.VIP()       
    elif Input2=="EXECUTIVE":
        r.Executive()
    else:
        print("Please enter valid Category.")
        r.Redirection()
        Input2=input("Please select your desired category: ").strip().upper()
    Input3=int(input("Please enter the serial number of the Package: "))
    if Input3==1:
        r.single()
        if Input2=="STAR":
            print("Your Room number is:",random.randint(91,100),"Floor:9")
        elif Input2=="VIP":
            print("Your Room number is:",random.randint(81,90),"Floor:8")
        elif Input2=="EXECUTIVE":
            print("Your Room number is:",random.randint(71,80),"Floor:7")
    elif Input3==2:
        r.double()
        if Input2=="STAR":
            print("Your Room number is:",random.randint(61,70),"Floor:6")
        elif Input2=="VIP":
            print("Your Room number is:",random.randint(51,60),"Floor:5")
        elif Input2=="EXECUTIVE":
            print("Your Room number is:",random.randint(41,50),"Floor:4")    
    elif Input3==3:
        r.triple()
        if Input2=="STAR":
            print("Your Room number is:",random.randint(31,40),"Floor:3")
        elif Input2=="VIP":
            print("Your Room number is:",random.randint(21,30),"Floor:2")
        elif Input2=="EXECUTIVE":
            print("Your Room number is:",random.randint(11,20),"Floor:1")
    elif Input3==4:
        r.quad()
        if Input2=="STAR":
            print("Your Room number is:",random.randint(101,110),"Floor:10")
        elif Input2=="VIP":
            print("Your Room number is:",random.randint(111,20),"Floor:11")
        elif Input2=="EXECUTIVE":
            print("Your Room number is:",random.randint(121,130),"Floor:12")
    else:
        print("Please enter valid Package")
        Input3=int(input("Please enter the serial number of the Package: "))

#------------------------------------------FoodOrdering----------------------------------------------
# mycursor.execute("create table Foodcategory(sl_no int,Category varchar(200),Description varchar(255))")
# print("Table created")

# sql="insert into foodcategory(sl_no,Category,Description)values(%s,%s,%s)"
# val=("1","VEG","Veg items only.")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added Successfully")

# sql="insert into foodcategory(sl_no,Category,Description)values(%s,%s,%s)"
# val=("2","Non-VEG","Non-Veg items only")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added Successfully")

# sql="insert into foodcategory(sl_no,Category,Description)values(%s,%s,%s)"
# val=("3","North-indian","North-indian items only")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added Successfully")

# sql="insert into foodcategory(sl_no,Category,Description)values(%s,%s,%s)"
# val=("4","Chinese","Chinese items only")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added Successfully")

class FoodOrdering(Summary):
    def Redirection2(self):
        print("You are now redirected to Food Ordering Automation system.")
        print()
        print("Due to some reasons,we can offer only few food items.\nSorry for the trouble.")
        print()
        print("Here are the categories of Food available:")
        print()
        mycursor.execute("select * from foodcategory")
        result=mycursor.fetchall()
        for i in result:
            print(i)
        #sql=
    def veg(self):
        print("You selected Veg category.\nHere is your list of items:")
        print()
        print(veg)
        #sql
    def Non_veg(self):
        print("You selected Non-Veg category.\nHere are your list of items:")
        print()
        print(Non_veg)
        #sql
    def North_indian(self):
        print("You selected North Indian varities category.\nHere are your list of items:")
        print()
        print(north_indian)
        #sql
    def chinese(self):
        print("You selected chinese varities category.\nHere are your list of items:")
        print()
        print(chinese)
        #sql
f=FoodOrdering()

veg={"VEG.FRIED RICE":"@165","CHILLY GARLIC RICE":"@165","VEG HAKKA NOODLES":"@145"}
Non_veg={"CHICKEN BRIYANI":"@150","MUTTON BRIYANI":"@180","CHICKEN NOODLES":"@120","CHICKEN RICE":"@120"}
north_indian={"PANEER BUTTER MASALA":"@80","RAJASTHANI CHICKEN":"@190","HYDERABADI GRAVY":"@250"}
chinese={"SZECHWAN CHILLI CHICKEN":"@120","CHILLI CHINESE TOAST":"@115","GARLIC BREAD WITH CHEESE":"@119"}
Total_items={"VEG.FRIED RICE":165,"CHILLY GARLIC RICE":165,"VEG HAKKA NOODLES":145,"CHICKEN BRIYANI":150,"MUTTON BRIYANI":180,"CHICKEN NOODLES":120,"CHICKEN RICE":120,"PANEER BUTTER MASALA":80,"RAJASTHANI CHICKEN":190,"HYDERABADI GRAVY":250,"SZECHWAN CHILLI CHICKEN":120,"CHILLI CHINESE TOAST":115,"GARLIC BREAD WITH CHEESE":119}

if Input1==2:
    f.Redirection2()
    Input4=int(input("Please enter the serial number of category of food: "))
    if Input4==1:
        f.veg()
    elif Input4==2:
        f.Non_veg()
    elif Input4==3:
        f.North_indian()
    elif Input4==4:
        f.chinese()
    else:
        print("please enter valid digit.")
        r.Redirection2()
    def Items():
        Input5=input("Enter the name of item with exact spell and space as in list: ").upper().strip()
        Input6=int(input("Enter count of item: "))
        if Input5 in Total_items:
            Bill=Input6*Total_items[Input5]
            Input7=input("If you want to continue to more items selection,Enter YES else NO: ").upper().strip()
            if Input7=="NO":
                print("Your order costs:",Bill)
            elif Input7=="YES":
                Items()
                Bill+=Bill
                print("Your order costs:",Bill)
            else:
                print("Please enter only YES or NO: ")
                Items()
        else:
            print("Your selected item is not available.")
            Items()
    Items()
    print("Your order is placed.\nThank You for Ordering.\nHave a Good Day\nEnjoy our Foods :)")

#=======================================================================================================================================
elif Input1!=1 and Input1!=2:
    print("Please enter valid input of 1 or 2")
    Input1=int(input("Your Response: "))


        

