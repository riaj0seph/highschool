def flightbooking():
    fld=open("flightlist.csv",'r')
    w=csv.reader(fld)
    for i in w:
        if len(i)>3:
         print("Destination:",i[0],"Destination Code:",i[1],"Date:",i[2],"Rate",i[3], sep='  ')
    fld.close()
      
def cancel_date():
    print("PLEASE NOTE: An appropriate fee will be charged as a result of date changes")
    inpt=input("Cancel flight(c) or Change date(d)?")
    if type(L[3])==str:
        print("You have no currently scheduled flights")
    elif inpt=='c':
        print("Flight to",L[3][0],'has been successfully cancelled')
        L[3]='destination not set'
    elif inpt=='d':
        import math
        select=1
        while select==1:
         day,mnth=int(input("Please enter the day(number) to which you wish to change your flight to:")),int(input("Please enter the month(number) to which you wish to change your flight to:"))
         day1=L[3][2][0]
         mnth1=L[3][2][1]
         additional=500+abs(mnth1-mnth)*750
         final=L[3][3][0]+additional
         print("FInal amount is:",final)
         sel=input("Accept(a) or Go back(b)?:")
         if sel=='a':
             L[3][2][0],L[3][2][1]=day,mnth
             L[3][3][0]=final
             select=2        
         if sel=='b':
             continue

        
def services():
    s=open("services.txt","r")
    dsc=s.readlines()
    decide=input("Search for a service(s) or display all available services(d)?")
    if decide=='s':
        search=input("Enter the service you are looking for")
        f=0
        for i in dsc:
            if search.lower() in i.lower():
                print("Service available:",i)
                f=1
        if f==0:
                print("We're sorry, we do not have this service at the moment")
    else:
        for i in dsc:
            print(i)
    s.close()

def jobapply():
    if L[1]<21:
        print("You must be above 21 to apply for a job")
    else:
        job=input("Enter your required field you would like to work in:")
        gender=input("Enter your gender(F/M):")
        ed=input("Enter your qualifications")
        exp=input("Do you have any previous work experience (Y/N)?")
        cont=int(input("Enter your contact number"))
        n,ag=L[0],L[1]
        global cv
        cv=[n,ag,job,gender,ed,exp,cont]
        j=open("applications.csv",'a',newline='')
        y=csv.writer(j)
        y.writerow(cv)
        j.close()
        print(cv)
        print("Your application has been submitted")

def applicationaccept():
    j=open("applications.csv",'r')
    c=0
    h=csv.reader(j)
    for cv in h:
        c=c+1
    if c==0:
        print("There are no current applications")
    else:
        print(">>>>>>Current applications")
        j.seek(0)
        for cv in h:
            print(cv)
        number=int(input("Enter the number of applicants to be rejected"))
        rej=[]
        for i in range(number):
            n=input("Enter name to be deleted/rejected")
            rej.append(n)
        accepted=[]
        j.seek(0)
        for i in h:
            if i[0] not in rej:
                accepted.append(i)
        j.close()
        k=open("emp.dat","wb+")
        pickle.dump(accepted,k)
        k.seek(0)
        y=pickle.load(k)
        print("Accepted applicants")
        print(y)
        k.close()
        print("Applications accepted successfully")

def flightchange():
    r=open("flightlist.csv",'r+',newline='')
    print("Currently available flights")
    k=csv.reader(r)
    for rec in k:
        print(rec)
    print("Update flight list")
    r.seek(0)
    d=[]
    D=[]
    loc=input("Enter the destination to be modified:")
    k=csv.reader(r)
    for rec in k:
            if loc==rec[0]:
                code=input("Enter the new International Airport Code:")
                day=int(input("Enter the day"))
                month=int(input("Enter the month"))
                year=int(input("Enter the year"))
                d.append(day)
                d.append(month)
                d.append(year)
                rate=int(input("Enter the rate"))
                D.append([loc,code,d,rate])
            else:
                D.append(rec)
    r.close()
    r=open("flightlist.csv",'w',newline='')
    e=csv.writer(r)
    e.writerows(D)
    r.close()

    
        
print('='*80)
print("\t\t\t Welcome to Cochin Airport")
g=0
import csv
import pickle
fld=open("flightlist.csv",'w',newline='')
w=csv.writer(fld)
d=[["Bengaluru",'BLR',[15,8,2023],[4000]],['Singapore','SIN',[3,7,2023],[15000]],['Paris','CDG',[6,8,2023],[60000]],['Addis Ababa','ADD',[28,7,2023],[45000]]]
w.writerows(d)
fld.close()
s=open("services.txt",'w')
serv=["Lounges\n","ATM\n","Money Exchange\n","Veg Restaurants\n","Non Veg Restaurants\n","Prayer Room\n","Feeding Room\n"]
s.writelines(serv)
s.close()

def account_create():
    global g
    g=0
    print("Create an account")
    global L
    name=input("Enter your full name")
    age=int(input("Enter your legal age"))
    acctype=input("Registering as admin(a) or user(u)?")
    L=[name,age,acctype,'destination not selected']

account_create()
if L[2]=='u':
 while  True:
    print('='*80)
    print("\t\t\t\t MENU")
    print('='*80)
    print("How may we assist you?")
    print("1. Flight Booking")
    print("2. Flight Cancellation or Flight Date Change")
    print("3. Airport Services and Facilities")
    print("4. Job Application")
    print("5.Quit Menu")
    ch=int(input("Enter your selection: "))
    if ch==1:
        print(">>>Flight Booking<<<")
        flightbooking()
        destination=input("Enter your desired destination's code")
        for i in d:
         if i[1]==destination:
            L[3]=i
            print("Flight successfully booked")
    elif ch==2:
        print(">>>Cancellations and Date Changes<<<")
        cancel_date()
    elif ch==3:
        print(">>>Services and Facilities<<<")
        services()
    elif ch==4:
        print(">>>Applications<<<")
        jobapply()
    elif ch==5:
        print("Thank you for visiting, come again!")
        break
    else:
        print("Invalid selection; please enter the correct corresponding number")

elif L[2]=='a':
    while True:
        print("\t\t\t\t Admin account")
        print('='*80)
        print("1. Edit the Available Flights")
        print("2. Review Job Applications")
        print("Enter any other key to exit admin menu")
        ch=input("Enter your selection: ")
        if ch=='1':
            flightchange()
        elif ch=='2':
            applicationaccept()
        else:
            print("Exiting...")
            break
            
               


   
      
            
    
    
    
        
        
        
            
        
