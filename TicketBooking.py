from unittest import result
from xml.dom.pulldom import START_ELEMENT
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="dani",
    database="onlinebooking"
    )
mycursor=mydb.cursor()

#Database:
# mycursor.execute("create database OnlineBooking")
# print("db created successfully")

#Tables:
# mycursor.execute("create table salem (sl_no int,movies varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Chennai (sl_no int,movies varchar(255))")
# print("table created successfully")

# mycursor.execute("create table namakkal (sl_no int,movies varchar(255))")
# print("table created successfully")

# mycursor.execute("create table coimbatore (sl_no int,movies varchar(255))")
# print("table created successfully")

# mycursor.execute("create table madurai (sl_no int,movies varchar(255))")
# print("table created successfully")

# mycursor.execute("create table trichy (sl_no int,movies varchar(255))")
# print("table created successfully")



#values:

# sql="insert into salem(sl_no,movies) values (%s,%s)"
# val=("1","movie1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into salem(sl_no,movies) values (%s,%s)"
# val=("2","movie2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into salem(sl_no,movies) values (%s,%s)"
# val=("3","movie3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into chennai(sl_no,movies) values (%s,%s)"
# val=("1","movie1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into chennai(sl_no,movies) values (%s,%s)"
# val=("2","movie2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into chennai(sl_no,movies) values (%s,%s)"
# val=("3","movie3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into coimbatore(sl_no,movies) values (%s,%s)"
# val=("1","movie1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into coimbatore(sl_no,movies) values (%s,%s)"
# val=("2","movie2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into coimbatore(sl_no,movies) values (%s,%s)"
# val=("3","movie3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into namakkal(sl_no,movies) values (%s,%s)"
# val=("1","movie1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into namakkal(sl_no,movies) values (%s,%s)"
# val=("2","movie2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into namakkal(sl_no,movies) values (%s,%s)"
# val=("3","movie3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into madurai(sl_no,movies) values (%s,%s)"
# val=("1","movie1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into madurai(sl_no,movies) values (%s,%s)"
# val=("2","movie2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into madurai(sl_no,movies) values (%s,%s)"
# val=("3","movie3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into trichy(sl_no,movies) values (%s,%s)"
# val=("1","movie1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into trichy(sl_no,movies) values (%s,%s)"
# val=("2","movie2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into trichy(sl_no,movies) values (%s,%s)"
# val=("3","movie3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")



#tables
# mycursor.execute("create table Movie11 (sl_no int,theatres varchar(255))")
# print("table created successfully") 

# mycursor.execute("create table Movie21 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie31 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie12 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie22 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie32 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie13 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie23 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie33 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie14 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie24 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie34 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie15 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie25 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie35 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie16 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie26 (sl_no int,theatres varchar(255))")
# print("table created successfully")

# mycursor.execute("create table Movie36 (sl_no int,theatres varchar(255))")
# print("table created successfully")


#values:
#11
# sql="insert into movie11(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie11(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie11(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #21
# sql="insert into movie21(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie21(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie21(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #31
# sql="insert into movie31(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie31(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie31(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #12
# sql="insert into movie12(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie12(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie12(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #22
# sql="insert into movie22(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie22(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie22(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #32
# sql="insert into movie32(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie32(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie32(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #13
# sql="insert into movie13(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie13(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie13(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #23
# sql="insert into movie23(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie23(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie23(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #33
# sql="insert into movie33(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie33(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie33(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #14
# sql="insert into movie14(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie14(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie14(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #24
# sql="insert into movie24(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie24(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie24(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #34
# sql="insert into movie34(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie34(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie34(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #15
# sql="insert into movie15(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie15(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie15(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #25
# sql="insert into movie25(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie25(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie25(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #35
# sql="insert into movie35(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie35(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie35(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #16
# sql="insert into movie16(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie16(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie16(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #26
# sql="insert into movie26(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie26(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie26(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# #36
# sql="insert into movie36(sl_no,theatres) values (%s,%s)"
# val=("1","theatre1")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie36(sl_no,theatres) values (%s,%s)"
# val=("2","theatre2")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")

# sql="insert into movie36(sl_no,theatres) values (%s,%s)"
# val=("3","theatre3")
# mycursor.execute(sql,val)
# mydb.commit()
# print("value added successfully")


print("------------------------------WELCOME TO TICKETforSHOW-------------------------------------")
print("TOP CITIES:")
locations=["chennai","salem","coimbatore","madurai","namakkal","trichy"]
print(locations)

input1=input("Enter your location: ").lower().strip()

def chennai():
        mycursor.execute("select * from chennai")
        result=mycursor.fetchall()
        print("sl_no","Movies")
        for i in result:
            print(i)
        input2=int(input("Enter the sl_no of movie: "))
        chennai={1:movie11,2:movie21,3:movie31}
        result=chennai[input2]
        if input2 in chennai:
            result()
            input3=int(input("Enter serial number of Theatre: "))
            if input3==1 or input3==2 or input3==3:
                print("FIRST CLASS WILL BE 150 RUPEES\n""SECOND CLASS WILL BE 120 RUPEES")
                Class=input("ENTER CLASS(FIRST OR SECOND):").upper().strip()
                if Class=="FIRST":
                     first_class()
                elif Class=="SECOND":
                     second_class() 
                else:
                    print("Invalid class")
                    input_func1()
            else:
                print("Enter valid theatre sl_no: ")
                input_func1()

        else:
            print("Enter valid movie sl_no: ")
            input_func1()
def salem():
        mycursor.execute("select * from salem")
        result=mycursor.fetchall()
        print("sl_no","Movies")
        for i in result:
            print(i)
        input2=int(input("Enter the sl_no of movie: "))
        salem={1:movie12,2:movie22,3:movie32}
        result=salem[input2]
        if input2 in salem:
            result()
            input3=int(input("Enter serial number of Theatre: "))
            if input3==1 or input3==2 or input3==3:
                print("FIRST CLASS WILL BE 150 RUPEES\n""SECOND CLASS WILL BE 120 RUPEES")
                Class=input("ENTER CLASS(FIRST OR SECOND):").upper().strip()
                if Class=="FIRST":
                    first_class()
                elif Class=="SECOND":
                    second_class() 
                else:
                    print("Invalid class")
                    input_func1()
            else:
                print("Enter valid theatre sl_no: ")
                input_func1()

        else:
            print("Enter valid movie sl_no: ")
            input_func1()
def coimbatore():
        mycursor.execute("select * from coimbatore")
        result=mycursor.fetchall()
        print("sl_no","Movies")
        for i in result:
            print(i)
        input2=int(input("Enter the sl_no of movie: "))
        coimbatore={1:movie13,2:movie23,3:movie33}
        result=coimbatore[input2]
        if input2 in coimbatore:
            result()
            input3=int(input("Enter serial number of Theatre: "))
            if input3==1 or input3==2 or input3==3:
                print("FIRST CLASS WILL BE 150 RUPEES\n""SECOND CLASS WILL BE 120 RUPEES")
                Class=input("ENTER CLASS(FIRST OR SECOND):").upper().strip()
                if Class=="FIRST":
                    first_class()
                elif Class=="SECOND":
                    second_class() 
                else:
                    print("Invalid class")
                    input_func1()
            else:
                print("Enter valid theatre sl_no: ")
                input_func1()

        else:
            print("Enter valid movie sl_no: ")
            input_func1()
def madurai():
        mycursor.execute("select * from madurai")
        result=mycursor.fetchall()
        print("sl_no","Movies")
        for i in result:
            print(i)
        input2=int(input("Enter the sl_no of movie: "))
        madurai={1:movie14,2:movie24,3:movie34}
        result=madurai[input2]
        if input2 in madurai:
            result()
            input3=int(input("Enter serial number of Theatre: "))
            if input3==1 or input3==2 or input3==3:
                print("FIRST CLASS WILL BE 150 RUPEES\n""SECOND CLASS WILL BE 120 RUPEES")
                Class=input("ENTER CLASS(FIRST OR SECOND):").upper().strip()
                if Class=="FIRST":
                    first_class()
                elif Class=="SECOND":
                    second_class() 
                else:
                    print("Invalid class")
                    input_func1()
            else:
                print("Enter valid theatre sl_no: ")
                input_func1()

        else:
            print("Enter valid movie sl_no: ")
            input_func1()
def namakkal():
        mycursor.execute("select * from namakkal")
        result=mycursor.fetchall()
        print("sl_no","Movies")
        for i in result:
            print(i)
        input2=int(input("Enter the sl_no of movie: "))
        namakkal={1:movie15,2:movie25,3:movie35}
        result=namakkal[input2]
        if input2 in namakkal:
            result()
            input3=int(input("Enter serial number of Theatre: "))
            if input3==1 or input3==2 or input3==3:
                print("FIRST CLASS WILL BE 150 RUPEES\n""SECOND CLASS WILL BE 120 RUPEES")
                Class=input("ENTER CLASS(FIRST OR SECOND):").upper().strip()
                if Class=="FIRST":
                    first_class()
                elif Class=="SECOND":
                    second_class() 
                else:
                    print("Invalid class")
                    input_func1()
            else:
                print("Enter valid theatre sl_no: ")
                input_func1()

        else:
            print("Enter valid movie sl_no: ")
            input_func1()
                
def trichy():
        mycursor.execute("select * from trichy")
        result=mycursor.fetchall()
        print("sl_no","Movies")
        for i in result:
            print(i)
        input2=int(input("Enter the sl_no of movie: "))
        trichy={1:movie16,2:movie26,3:movie36}
        result=trichy[input2]
        if input2 in trichy:
            result()
            input3=int(input("Enter serial number of Theatre: "))
            if input3==1 or input3==2 or input3==3:
                print("FIRST CLASS WILL BE 150 RUPEES\n""SECOND CLASS WILL BE 120 RUPEES")
                Class=input("ENTER CLASS(FIRST OR SECOND):").upper().strip()
                if Class=="FIRST":
                    first_class()
                elif Class=="SECOND":
                    second_class() 
                else:
                    print("Invalid class")
                    input_func1()
            else:
                print("Enter valid theatre sl_no: ")
                input_func1()

        else:
            print("Enter valid movie sl_no: ")
            input_func1()

def movie11():
        mycursor.execute("select * from movie11")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie21():
        mycursor.execute("select * from movie21")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie31():
        mycursor.execute("select * from movie31")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie12():
        mycursor.execute("select * from movie12")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie22():
        mycursor.execute("select * from movie22")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie32():
        mycursor.execute("select * from movie32")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie13():
        mycursor.execute("select * from movie13")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie23():
        mycursor.execute("select * from movie23")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie33():
        mycursor.execute("select * from movie33")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie14():
        mycursor.execute("select * from movie14")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie24():
        mycursor.execute("select * from movie24")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie34():
        mycursor.execute("select * from movie34")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie15():
        mycursor.execute("select * from movie15")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie25():
        mycursor.execute("select * from movie25")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie35():
        mycursor.execute("select * from movie35")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie16():
        mycursor.execute("select * from movie16")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie26():
        mycursor.execute("select * from movie26")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def movie36():
        mycursor.execute("select * from movie36")
        result=mycursor.fetchall()
        print("sl_no","Theatres")
        for i in result:
            print(i)
def first_class():
    seats=int(input("ENTER NUMBER OF SEATS:"))
    pay=seats*150
    print(f"You have to pay {pay} rupees")
def second_class():
    seatss=int(input("ENTER NUMBER OF SEATS:"))
    pay2=seatss*120
    print(f"You have to pay {pay2} rupees")

dict_of_locations={'chennai':chennai,'salem':salem,'madurai':madurai,'coimbatore':coimbatore,'trichy':trichy,'namakkal':namakkal}
input_func1=dict_of_locations[input1]
if input1 in locations:
    input_func1()
    print("--------------------------------------Thank you for Booking-------------------------------------\n---------------------------------------------Enjoy the Show--------------------------------------------------------")
else:
    print("invalid location.")
    print(locations)
    input1=input("Enter your location: ").lower().strip()
    
    
