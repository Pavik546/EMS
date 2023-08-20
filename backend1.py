# importing mysql connector
import mysql.connector
import os
import sys
import time

# making Connection
con = mysql.connector.connect(
	host="localhost", user="root", password="Nagercoil@9488", database="ems")

class Admin:
    
    def createadmin():
        email= input("Enter email address : ")
        password = input("Enter password : ")
        data = (email,password)
        sql = 'insert into adminlogin values(%s,%s)'
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Admin Added Successfully ")
        Admin.welcome()
        
    def elogin():
        email= input("Enter email address : ")
        password = input("Enter password : ")
        data = (email,password)
        sql = 'insert into elogin values(%s,%s)'
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Employee Credentials Added Successfully ")
        Admin.welcome()
        
    def Addproject():
        pid= input("Enter project id ")
        pname= input("Enter project name and details  ")
        duedate=input("Enter Duedate ")
        status="Not started"
        team=input("Enter Team members ")
        data = (pid,pname,duedate,status,team)
        sql = 'insert into project values(%s,%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Assign project Successfully ")
        Admin.welcome()

    def Addemployee():
        eid= input("Enter employee id ")
        pname= input("Enter employee name  ")
        dob=input("Enter dateofbirth ")
        gender=input("Enter gender")
        position=input("Enter position")
        phone=input("Enter phone number ")
        email=input("Enter email id")
        data = (eid,pname,dob,gender,email,position,phone)
        sql = 'insert into employee values(%s,%s,%s,%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Employee added Successfully ")
        Admin.welcome()

    def Addsalary():
        eid= input("Enter employee id ")
        ename= input("Enter employee  name  ")
        salary=int(input("Enter salary"))
        base=(10/100)*salary
        total=salary+base
        data = (eid,ename,salary,base,total)
        sql = 'insert into salary values(%s,%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Salary added Successfully ")
        Admin.welcome()
    def Remove_Employ():
        employeeid = input("Enter Employee Id : ")
        if(Admin.check_employee(employeeid) == False):
            print("Employee does not exists\nTry Again\n")
            Admin.welcome()
        else:
            sql ='delete from employee where employeeid=%s'
            data = (employeeid,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            print("Employee Removed")
            Admin.welcome()
            
    def viewproject():
        Id = input("Enter project Id : ")
        sql = 'select * from project where pid=%s'
        data=(Id,)
        c = con.cursor()
        c.execute(sql, data)
        for r in c:
            print(r)
        Admin.welcome()
            
    def Remove_Employlogin():
        email = input("Enter Employee email ")
        sql = 'delete from elogin where email=%s'
        data = (email,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Employee Removed")
        Admin.welcome()
        
    def removeproject():
        pid= input("Enter project id ")
        sql = 'delete from project where pid=%s'
        data = (email,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Project Removed")
        Admin.welcome()
        
        
    def Display_Employees():
        sql = 'select * from employee'
        c = con.cursor()
        c.execute(sql)
        r = c.fetchall()
        for i in r:
            print("employee id",i[0])
            print("employee name",i[1])
            print("employee dob",i[2])
            print("employee gender",i[3])
            print("employee email",i[4])
            print("employee positon",i[5])
            print("employee phoneno",i[6])
            print("---------------------")
        Admin.welcome()
              
    def viewAttend():
        sql = 'select * from Attendance'
        c = con.cursor()
        c.execute(sql)
        for r in c:
            print(r)
        Admin.welcome()
              
    def viewleave():
        sql = 'select * from empleave'
        c = con.cursor()
        c.execute(sql)
        for i in c:
            print(i)
        print("---------------------")
        Admin.welcome()
              
              
    def viewEmploy():
        Id = input("Enter Employee Id : ")
        if(Admin.check_employee(Id) == False):
            print("Employee does not exists\nTry Again\n")
            Admin.welcome()
        else:
            sql = 'select * from employee where employeeid=%s'
            data = (Id,)
            c = con.cursor()
            c.execute(sql, data)
            r = c.fetchall()
            for i in r:
                print("employee id",i[0])
                print("employee name",i[1])
                print("employee dob",i[2])
                print("employee gender",i[3])
                print("employee email",i[4])
                print("employee positon",i[5])
                print("employee phoneno",i[6])
                print("---------------------")
            Admin.welcome()
    
    def leave():
        Id=input("Employee id ")
        status=input("Enter leave approved/disapproved")
        sql = 'update empleave set status=%s where empid=%s'
        d = (status, Id)
        c=con.cursor()
        c.execute(sql, d)
        con.commit()
        print("Status updated")
        Admin.welcome()
              
              
    def Adddepartment():
        did= input("Enter department id ")
        dname= input("Enter department name and details  ")
        nom=input("Enter no of employees")
        mem=input("Enter  members ")
        data = (did,dname,nom,mem)
        sql = 'insert into department values(%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Department added Successfully ")
        Admin.welcome()
        
              
    def updatedepart():
        did=input("department id ")
        nom=input("Enter no of members")
        mem=input("Enter members ")
        sql = 'update department set noofemployees=%s,Members=%s where did=%s'
        d = (nom,mem,did)
        c=con.cursor()
        c.execute(sql, d)
        con.commit()
        print("updated successfully")
        Admin.welcome()
              
    def updatesalary():
        eid=input("Employee id ")
        salary=int(input("Enter new salary"))
        bonus=(10/100)*salary
        total=salary+bonus
        sql = 'update salary set Basesalary=%s,Bonus=%s,Totalsalary=%s where empid=%s'
        d = (salary,bonus,total,eid)
        c=con.cursor()
        c.execute(sql, d)
        con.commit()
        print("salary updated successfully")
        Admin.welcome()
          
   
          
    def check_employee(Id):
        sql = 'select * from employee where employeeid=%s'
        c = con.cursor(buffered=True)
        data = (Id,)
        c.execute(sql, data)
        r = c.rowcount
        if r == 1:
            return True
        else:
            return False
              
    def check_project(Id):
        sql = 'select * from project where pid=%s'
        c = con.cursor(buffered=True)
        data = (Id)
        c.execute(sql, data)
        r = c.rowcount
        if r == 1:
            return True
        else:
            return False
     
          
    def menu():
        os.system('cls')
        print("1 to assign project details")
        print("2 to Remove Employee details ")
        print("3 to remove employee login")
        print("4 to Display Employees details")
        print("5 to Create employee login")
        print("6 to create admin login")
        print("7 to view Attendance and task details employee")
        print("8 to give permission leave" )
        print("9 to add department of company")
        print("10 to update details of department")
        print("11 to update salary of employee")
        print("12 to view project details")
        print("13 to view employee details by id")
        print("14 to view the leave details")
        print("15 to remove project detail")
        print("16 t0 add salary details")
        print("17 to add new employee")
        print()
        ch = input("Enter your Choice ")
        if ch == '1':
            Admin.Addproject()
        elif ch == '2': 
            Admin.Remove_Employ()
        elif ch == '3':
            Admin.Remove_Employlogin()
        elif ch == '4':
            Admin.Display_Employees()
        elif ch=='5':
            Admin.elogin()
        elif ch=='6':
            Admin.createadmin()
        elif ch=='7':
            Admin.viewAttend()
        elif ch=='8':
            Admin.leave()
        elif ch=='9':
            Admin.Adddepartment()
        elif ch=='10':
            Admin.updatedepart()
        elif ch=='11':
            Admin.updatesalary()
        elif ch=='12':
            Admin.viewproject()
        elif ch=='13':
            Admin.viewEmploy()
        elif ch=='14':
            Admin.viewleave()
        elif ch=='15':
            Admin.removeproject()
        elif ch=='16':
            Admin.Addsalary()
        elif ch=='17':
            Admin.Addemployee()
        else:
            print("Wrong choice")
        time.sleep(5)
        Admin.welcome()
      
    def welcome():
        print("Welcome to Employee Management Record")
        l=input("If u want continue type yes/no")
        if (l=='yes'):
            Admin.menu()
        else:
            sys.exit()

      
    
class employee:
    def viewproject():
        pid = input("Enter project Id : ")
        if(employee.check_project(pid) == False):
            print("project does not exists\nTry Again\n")
            employee.welcome()
        else:
            sql = 'select * from project where pid=%s'
            data = (pid,)
            c = con.cursor()
            c.execute(sql, data)
            for r in c:
                print(r)
            employee.welcome()
    
    def viewEmploy():
        Id = input("Enter Employee Id : ")
        if(employee.check_employee(Id) == False):
            print("Employee does not exists\nTry Again\n")
            employee.welcome()
        else:
            sql = 'select * from employee where employeeid=%s'
            data = (Id,)
            c = con.cursor()
            c.execute(sql, data)
            r = c.fetchall()
            for i in r:
                print("employee id",i[0])
                print("employee name",i[1])
                print("employee dob",i[2])
                print("employee gender",i[3])
                print("employee email",i[4])
                print("employee positon",i[5])
                print("employee phoneno",i[6])
                print("---------------------")
            employee.welcome()
    def check_employee(Id):
        sql = 'select * from employee where employeeid=%s'
        c = con.cursor(buffered=True)
        data = (Id,)
        c.execute(sql, data)
        r = c.rowcount
        if r == 1:
            return True
        else:
            return False
        
    def check_project(pid):
        sql = 'select * from project where pid=%s'
        c = con.cursor(buffered=True)
        data = (pid,)
        c.execute(sql, data)
        r = c.rowcount
        if r == 1:
            return True
        else:
            return False
        
              
    def updateEmploy():
        Id = input("Enter Employee Id : ")
        phone=input("Enter your phonenumber")
        sql = 'update employee set phonenumber=%s where employeeid=%s'
        d = (phone,Id)
        c=con.cursor()
        c.execute(sql, d)
        con.commit()
        print("updated successfully")
        employee.welcome()
            
    def askleave():
        eid=input("Enter employee id ")
        ename=input("Enter name ")
        date=input("Enter start date  ")
        edate=input("Enter end date")
        tday=input("Enter total day")
        reason=input("Enter reason")
        status="NULL"
        d = (eid,ename,date,edate,tday,reason,status)
        sql = 'insert into empleave values(%s,%s,%s,%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql, d)
        con.commit()
        print("Leave Added Successfully ")
        employee.welcome()
        
    def addattend():
        empid=input("Enter Employee id ")
        empname=input("Enter name ")
        Intime=input("Enter in time")
        Outtime=input("Enter out time")
        projectname=input("Enter ur project")
        daliyactivity=input("Enter today activity ")
        data = (empid,empname,Intime,projectname,daliyactivity,Outtime)
        sql = 'insert into attendance values(%s,%s,%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Attendance Added Successfully ")
        employee.welcome()

    def viewdepart():
        sql = 'select * from department'
        c = con.cursor()
        c.execute(sql)
        for r in c:
            print(r)
        employee.welcome()
        
    def viewleave():
        Id = input("Enter employee Id : ")
        sql = 'select * from empleave where empid=%s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        for r in c:
            print(r)
        employee.welcome()
        
              
    def updateproject():
        pid = input("Enter project Id : ")
        if(employee.check_project(pid)== False):
            print("project not exist\nTry Again\n")
            employee.welcome()
        else:
            status=input("Enter status of project")
            sql = 'update project set status=%s where pid=%s'
            d = (status,pid)
            c=con.cursor()
            c.execute(sql, d)
            con.commit()
            print("updated successfully")
            employee.welcome()
            
    def viewsalary():
        Id = input("Enter Employee Id : ")
        if(employee.check_employee(Id) == False):
            print("Employee does not exists\nTry Again\n")
            employee.welcome()
        else:
            sql = 'select * from salary where empid=%s'
            data = (Id,)
            c = con.cursor()
            c.execute(sql, data)
            r = c.fetchall()
            for i in r:
                print("employee id",i[0])
                print("employee name",i[1])
                print("employee basesalary",i[2])
                print("employee bonus",i[3])
                print("employee total salary",i[4])
                print("---------------------")
            employee.welcome()
    
            
    
            
    def menu():
        os.system('cls')
        print("1 to view project details")
        print("2 to view Employee detail")
        print("3 to Edit your details")
        print("4 to ask leave")
        print("5 to add Attendance")
        print("6 to view department")
        print("7 to view leave details")
        print("8 to Update project status" )
        print("9 to view your salary")
        print()
        ch = input("Enter your Choice ")
        if ch == '1':
            employee.viewproject()
        elif ch == '2':
            employee.viewEmploy()
        elif ch == '3':
            employee.updateEmploy()
        elif ch == '4':
            employee.askleave()
        elif ch=='5':
            employee.addattend()
        elif ch=='6':
            employee.viewdepart()
        elif ch=='7':
            employee.viewleave()
        elif ch=='8':
            employee.updateproject()
        elif ch=='9':
            employee.viewsalary()
        else:
            print("Wrong choice")
        time.sleep(10)
        employee.welcome()
            
    def welcome():
        print("Welcome to Employee Management Record")
        l=input("If u want continue type yes/no")
        if (l=='yes'):
            employee.menu()
        else:
            sys.exit()

      

    
def check_admin(email,password):
    sql = 'select * from adminlogin where email=%s and password=%s'
    c = con.cursor(buffered=True)
    data = (email,password)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False   
    
def check_employeee(email,password):
    sql = 'select * from elogin where email=%s and password=%s'
    c = con.cursor(buffered=True)
    data = (email,password)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False    


# Calling menu function
role=input("Enter your role (admin/employee)")
if(role=='admin'):
    email=input("Enter email ")
    password=input("Enter password ")
    if(check_admin(email,password) == True):
        admi=Admin.welcome()
    else:
        print("Login failed")
if(role=='employee'):
    email=input("Enter email ")
    password=input("Enter password ")
    if(check_employeee(email,password) == True):
        emp=employee.welcome()
    else:
        print("Login failed")
