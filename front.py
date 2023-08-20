class employee:
    def viewproject():
        pid = st.text_input("Enter project Id : ")
        bt1=st.button("submit")
        if bt1:
            if(employee.check_project(pid) == False):
                st.write("project does not exists\nTry Again\n")
            else:
                sql = 'select * from project where pid=%s'
                data = (pid,)
                c = con.cursor()
                c.execute(sql, data)
                r=c.fetchall()
                for i in r:
                    st.write("Project Id :",i[0])
                    st.write("Project Name :",i[1])
                    st.write("Due Date :",i[2])
                    st.write("Status :",i[3])
                    st.write("Team Members :",i[4])
            
    
    def viewEmploy(Id):
        sql = 'select * from employee where employeeid=%s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            st.write("employee id :",i[0])
            st.write("employee name :",i[1])
            st.write("employee dob :",i[2])
            st.write("employee gender :",i[3])
            st.write("employee email :",i[4])
            st.write("employee positon :",i[5])
            st.write("employee phoneno :",i[6])
                   
        
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
        
              
    def updateEmploy(Id):
        phone=st.text_input("Enter new your phonenumber")
        bt1=st.button("submit")
        if bt1:
            sql = 'update employee set phonenumber=%s where employeeid=%s'
            d = (phone,Id)
            c=con.cursor()
            c.execute(sql, d)
            con.commit()
            st.write("updated successfully")
            
    def askleave(eid):
        ename=st.text_input("Enter name ")
        date=st.text_input("Enter start date  ")
        edate=st.text_input("Enter end date")
        tday=st.text_input("Enter total day")
        reason=st.text_input("Enter reason")
        status="Not Updated"
        bt1=st.button("submit")
        if bt1:
            d = (eid,ename,date,edate,tday,reason,status)
            sql = 'insert into empleave values(%s,%s,%s,%s,%s,%s,%s)'
            c = con.cursor()
            c.execute(sql, d)
            con.commit()
            st.write("Leave Added Successfully ")
        
    def addattend(empid):
        empname=st.text_input("Enter name ")
        Intime=st.text_input("Enter in time")
        Outtime=st.text_input("Enter out time")
        projectname=st.text_input("Enter ur project")
        daliyactivity=st.text_input("Enter today activity ")
        bt1=st.button("Add")
        if bt1:
            data = (empid,empname,Intime,projectname,daliyactivity,Outtime)
            sql = 'insert into attendance values(%s,%s,%s,%s,%s,%s)'
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            st.write("Attendance Added Successfully ")
        

    def viewdepart():
        sql = 'select * from department'
        c = con.cursor()
        c.execute(sql)
        r=c.fetchall()
        for i in r:
            st.write("Department id :",i[0])
            st.write("Department name :",i[1])
            st.write("No of Employees :",i[2])
            st.write("Members\n:",i[3])
            st.write("------------------------------------------------------")
        
        
    def viewleave(Id):
        sql = 'select * from empleave where empid=%s'
        data = (Id,)
        c = con.cursor(buffered=True)
        c.execute(sql, data)
        co = c.rowcount
        if co>=1:
            r=c.fetchall()
            for i in r:
                st.write("Employee id :",i[0])
                st.write("Employee Name :",i[1])
                st.write("Leave start date :",i[2])
                st.write("Leave End date :",i[3])
                st.write("Total days :",i[4])
                st.write("Reason : ",i[5])
                st.write("Status :",i[6])
                st.write("--------------------------------------------------")
        else:
            st.write("No leave in your profile")
                
        
          
    def updateproject():
        pid = st.text_input("Enter project Id : ")
        status=st.selectbox(("status"),("Completed","Progress","Not started"))
        bt1=st.button("submit")
        if bt1:
            if(employee.check_project(pid)== False):
                st.write("project not exist\nTry Again\n")
            else:
                sql = 'update project set status=%s where pid=%s'
                d = (status,pid)
                c=con.cursor()
                c.execute(sql, d)
                con.commit()
                st.write("updated successfully")
            
    def viewsalary(Id):
        sql = 'select * from salary where empid=%s'
        data = (Id,)
        c = con.cursor(buffered=True)
        c.execute(sql, data)
        co=c.rowcount
        if co!=0:
            r = c.fetchall()
            for i in r:
                st.write("Employee id :",i[0])
                st.write("Employee name :",i[1])
                st.write("Base salary :",str(i[2]))
                st.write("Bonus :",str(i[3]))
                st.write("Total salary :",str(i[4]))
        else:
            st.write("Salary not added")
      
            

    def check_employee(email,password,Id):
        sql = 'select * from elogin where email=%s and password=%s and eid=%s'
        c = con.cursor(buffered=True)
        data = (email,password,Id)
        c.execute(sql, data)
        r = c.rowcount
        if r == 1:
            return True
        else:
            return False  

    def updatepassword():
        email=st.text_input("Enter your email id ")
        Id=st.text_input("Enter your id")
        passw=st.text_input("Enter your old password")
        passw1=st.text_input("Enter your New password")
        bt=st.button("submit")
        if bt:
            if(employee.check_employee(email,passw,Id)==False):
                st.write("Enter correct details")
            else:
                sql = 'update elogin set password=%s where email=%s'
                d = (passw1,email)
                c=con.cursor()
                c.execute(sql, d)
                con.commit()
                st.write("updated successfully")

    def delleave(eid):
        sql='delete from empleave where empid=%s'
        d=(eid,)
        c=con.cursor()
        c.execute(sql,d)
        con.commit()
        st.write("Deleted your leaves successfully")

            
            
    def welcome():
        st.write("Welcome Here You Manage Your Account Lets see Menu")
        ch1=st.sidebar.selectbox(("Menu"),("Home","Account","Profile","Salary","Leave","Add Attendance","Project","Department"))
        if 'login' not in st.session_state:
            st.session_state.login=False
        if 'Id' not in st.session_state:
            st.session_state.Id="None"
        if(ch1=="Home"):
            st.image("home.jpeg")
        elif(ch1=="Profile" and st.session_state.login==True):
            ch2=st.selectbox(("Profile"),("Profile","View profile","Edit profile"))
            if(ch2=="Profile"):
                st.image("profile1.jpeg")

            elif(ch2=="View profile"):
                employee.viewEmploy(st.session_state.Id)
            elif(ch2=="Edit profile"):
                employee.updateEmploy(st.session_state.Id)
        elif(ch1=="Account"):
            ch3=st.selectbox(("Account"),("Account","login","logout","Update password"))
            if(ch3=="Account"):
                st.image("account3.jpeg")
            elif(ch3=="login"):
                eid=st.text_input("Enter Employee Email id")
                epw=st.text_input("Enter password")
                st.session_state.Id=st.text_input("Enter id")
                btn=st.button("Login")
                if btn:
                    if(employee.check_employee(eid,epw,st.session_state.Id)):
                        st.session_state.login=True
                        st.write("Login Successfully")
                    else:
                        st.write("Login Failed")
            elif(ch3=="logout"):
                st.session_state.login=False
                st.write("Logout successfull")
            elif(ch3=="Update password"):
                employee.updatepassword()
            
        elif(ch1=="Salary" and st.session_state.login==True):
            c11=st.selectbox(("Salary"),("Salary","View salary"))
            if(c11=="Salary"):
                st.image("salary3.jpeg")
            elif(c11=="View salary"):
                employee.viewsalary(st.session_state.Id)
        elif(ch1=="Leave" and st.session_state.login==True):
            ch4=st.selectbox(("Leave"),("Leave","Ask Leave","View leave","Cancel leave"))
            if(ch4=="Leave"):
                st.image("leave1.jpeg")
            elif(ch4=="Ask Leave"):
                employee.askleave(st.session_state.Id)
            elif(ch4=="View leave"):
                employee.viewleave(st.session_state.Id)
            elif(ch4=="Cancel leave"):
                employee.delleave(st.session_state.Id)
        elif(ch1=="Add Attendance" and st.session_state.login==True):
            employee.addattend(st.session_state.Id)
        elif(ch1=="Project" and st.session_state.login==True ):
            ch5=st.selectbox(("Project"),("Project","View project","Update project"))
            if(ch5=="Project"):
                st.image("project1.jpeg",width=700)
            elif(ch5=="View project"):
                employee.viewproject()
            elif(ch5=="Update project"):
                employee.updateproject()
        elif(ch1=="Department" and st.session_state.login==True):
            ch6=st.selectbox(("Department"),("Department","View Department",))
            if(ch6=="Department"):
                st.image("depart1.jpeg",width=700)

            elif(ch6=="View Department"):
                employee.viewdepart()
        else:
            st.write("Please Login and continue")
            st.image("loading.jpeg")        
    
class Admin:
    
    def createadmin():
        email= st.text_input("Enter email address : ")
        password = st.text_input("Enter password : ")
        bt1=st.button("Add")
        if bt1:
            data = (email,password)
            sql = 'insert into adminlogin values(%s,%s)'
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            st.write("Admin Added Successfully ")
        
        
    def elogin():
        email= st.text_input("Enter email address : ")
        password = st.text_input("Enter password : ")
        id=st.text_input("enter Id")
        bt1=st.button("Add")
        if bt1:
            data = (email,password,id)
            sql = 'insert into elogin values(%s,%s,%s)'
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            st.write("Employee Credentials Added Successfully ")
           
        
    def Addproject():
        pid= st.text_input("Enter project id ")
        pname= st.text_input("Enter project name and details  ")
        duedate=st.text_input("Enter Duedate ")
        status="Not started"
        team=st.text_input("Enter Team members ")
        bt1=st.button("Add")
        if bt1:
            data = (pid,pname,duedate,status,team)
            sql = 'insert into project values(%s,%s,%s,%s,%s)'
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            st.write("Assign project Successfully ")
        

    def Addemployee():
        eid= st.text_input("Enter employee id ")
        pname= st.text_input("Enter employee name  ")
        dob=st.text_input("Enter dateofbirth ")
        gender=st.selectbox(("gender"),("Male","Female"))
        position=st.text_input("Enter position")
        phone=st.text_input("Enter phone number ")
        email=st.text_input("Enter email id")
        bt1=st.button("Add")
        if bt1:
            data = (eid,pname,dob,gender,email,position,phone)
            sql = 'insert into employee values(%s,%s,%s,%s,%s,%s,%s)'
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            st.write("Employee added Successfully ")
      

    def Addsalary():
        eid= st.text_input("Enter employee id ")
        ename= st.text_input("Enter employee  name  ")
        salary=st.text_input("Enter salary")
        base=st.text_input("Enter bonus")
        total=st.text_input("Enter Total salary")
        bt1=st.button("Add")
        if bt1:
            data = (eid,ename,salary,base,total)
            sql = 'insert into salary values(%s,%s,%s,%s,%s)'
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            st.write("Salary added Successfully ")
     
    def Remove_Employ():
        employeeid = st.text_input("Enter Employee Id : ")
        bt1=st.button("submit")
        if bt1:
            if(Admin.check_employee(employeeid) == False):
                st.write("Employee does not exists\nTry Again\n")
            else:
                sql ='delete from employee where employeeid=%s'
                data = (employeeid,)
                c = con.cursor()
                c.execute(sql, data)
                con.commit()
                st.write("Employee Removed")
            
            
    def viewproject():
        sql = 'select * from project '
        c = con.cursor()
        c.execute(sql)
        r=c.fetchall()
        for i in r:
            st.write("Project id :",i[0])
            st.write("Project name :",i[1])
            st.write("Project Duedate :",i[2])
            st.write("Project status: ",i[3])
            st.write("Team Members\n :",i[4])
            st.write("-----------------------------------------------------------------------------")
      
            
   
        
    def removeproject():
        pid=st.text_input("Enter Project id")
        bt=st.button("Delete")
        if bt:
            sql = 'delete from project where pid=%s'
            data = (pid,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            st.markdown("Project was deleted")
      
        
        
    def Display_Employees():
        sql = 'select * from employee'
        c = con.cursor()
        c.execute(sql)
        r = c.fetchall()
        for i in r:
            st.write("Employee id :",i[0])
            st.write("Employee name :",i[1])
            st.write("Employee dob :",i[2])
            st.write("Employee gender :",i[3])
            st.write("Employee email :",i[4])
            st.write("Employee positon :",i[5])
            st.write("Employee phoneno :",i[6])
            st.write("------------------------------------------------")
            
              
    def viewAttend():
        sql = 'select * from Attendance'
        c = con.cursor()
        c.execute(sql)
        r=c.fetchall()
        for i in r:
            st.write("Employee id :",i[0])
            st.write("Employee name :",i[1])
            st.write("In time :",i[2])
            st.write("Project name :",i[3])
            st.write("Today Activities :",i[4])
            st.write("Out time :",i[5])
            st.write("--------------------------------------")

    def attbyid():
        eid=st.text_input("Enter Employee id")
        bt1=st.button("Submit")
        if bt1:
            sql = 'select * from Attendance where empid=%s'
            data=(eid,)
            c = con.cursor()
            c.execute(sql,data)
            r=c.fetchall()
            for i in r:
                st.write("Employee id :",i[0])
                st.write("Employee name :",i[1])
                st.write("In time :",i[2])
                st.write("Project name :",i[3])
                st.write("Today Activities :",i[4])
                st.write("Out time :",i[5])
                st.write("--------------------------------------")
              
              
    def viewleave():
        sql = 'select * from empleave'
        c = con.cursor()
        c.execute(sql)
        r=c.fetchall()
        for i in r:
           st.write("Employee id :",i[0])
           st.write("Employee name :",i[1])
           st.write("Leave start date :",i[2])
           st.write("Leave end date :",i[3])
           st.write("Total days :",i[4])
           st.write("Reason :",i[5])
           st.write("Status :",i[6])
           st.write("--------------------------------------------------------------")
              
              
    def viewEmploy():
        Id = st.text_input("Enter Employee Id : ")
        bt1=st.button("submit")
        if bt1:
            if(Admin.check_employee(Id) == False):
                st.write("Employee does not exists\nTry Again\n")
            else:
                sql = 'select * from employee where employeeid=%s'
                data = (Id,)
                c = con.cursor()
                c.execute(sql, data)
                r = c.fetchall()
                for i in r:
                    st.write("Employee id :",i[0])
                    st.write("Employee name :",i[1])
                    st.write("Employee dob :",i[2])
                    st.write("Employee gender :",i[3])
                    st.write("Employee email: ",i[4])
                    st.write("Employee positon :",i[5])
                    st.write("Employee phoneno :",i[6])
                
    
    def leave():
        Id=st.text_input("Employee id ")
        status=st.selectbox(("status"),("approved","disapproved"))
        bt1=st.button("submit")
        if bt1:
            sql = 'update empleave set status=%s where empid=%s'
            d = (status, Id)
            c=con.cursor()
            c.execute(sql, d)
            con.commit()
            st.write("Status updated")
      
              
              
    def Adddepartment():
        did= st.text_input("Enter department id ")
        dname= st.text_input("Enter department name and details  ")
        nom=st.text_input("Enter no of employees")
        mem=st.text_input("Enter  members ")
        bt1=st.button("Add")
        if bt1:
            data = (did,dname,nom,mem)
            sql = 'insert into department values(%s,%s,%s,%s)'
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            st.write("Department added Successfully ")
       
        
              
    def updatedepart():
        did=st.text_input("department id ")
        nom=st.text_input("Enter no of members")
        mem=st.text_input("Enter members ")
        bt1=st.button("submit")
        if bt1:
            sql = 'update department set noofemployees=%s,Members=%s where did=%s'
            d = (nom,mem,did)
            c=con.cursor()
            c.execute(sql, d)
            con.commit()
            st.write("updated successfully")
       
              
    def updatesalary():
        eid=st.text_input("Employee id ")
        salary=st.text_input("Enter new salary")
        bonus=st.text_input("Enter Bonus")
        total=st.text_input("Enter  Total salary")
        bt1=st.button("submit")
        if bt1:
            sql = 'update salary set Basesalary=%s,Bonus=%s,Totalsalary=%s where empid=%s'
            d = (salary,bonus,total,eid)
            c=con.cursor()
            c.execute(sql, d)
            con.commit()
            at.write("salary updated successfully")
        
          
   
          
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

    def Remove_elogin():
        email = st.text_input("Enter Employee email id : ")
        bt1=st.button("submit")
        if bt1:
            sql ='delete from elogin where email=%s'
            data = (email,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            st.write("Employee Login Removed")

    def Remove_adminlogin():
        email = st.text_input("Enter Admin email id : ")
        bt1=st.button("submit")
        if bt1:
            sql ='delete from adminlogin where email=%s'
            data = (email,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            st.write("Admin Login Removed")

    def updatepassword():
        email=st.text_input("Enter your email id ")
        passw=st.text_input("Enter your old password")
        passw1=st.text_input("Enter your New password")
        bt=st.button("submit")
        if bt:
            if(Admin.check_admin(email,passw)==False):
                st.write("Enter correct details")
            else:
                sql = 'update adminlogin set password=%s where email=%s'
                d = (passw1,email)
                c=con.cursor()
                c.execute(sql, d)
                con.commit()
                st.write("updated successfully")

    def viewdepart():
        sql = 'select * from department'
        c = con.cursor()
        c.execute(sql)
        r=c.fetchall()
        for i in r:
            st.write("Department id :",i[0])
            st.write("Department name : ",i[1])
            st.write("No of Employees :",i[2])
            st.write("Members in department :\n",i[3])
            st.write("------------------------------------------------")
              
          

    def Remove_depart():
        did= st.text_input("Enter Department id : ")
        bt1=st.button("submit")
        if bt1:
            sql ='delete from department where did=%s'
            data = (did,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            st.write("Department Removed")

    def Remove_salary():
        employeeid = st.text_input("Enter Employee Id : ")
        bt1=st.button("submit")
        if bt1:
            sql ='delete from employee where employeeid=%s'
            data = (employeeid,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            st.write("Employee salary Removed")
    
    
    def viewsalary():
        sql = 'select * from salary'
        c = con.cursor()
        c.execute(sql)
        r=c.fetchall()
        for i in r:
            st.write("Employee id :",i[0])
            st.write("Employee name : ",i[1])
            st.write("Base salary :",str(i[2]))
            st.write("Bonus :\n",str(i[3]))
            st.write("Total salay:",str(i[4]))
            st.write("------------------------------------------------")
       
            

    def welcome():
        st.write("Welcome,Here You Manage Your Details,Lets see Menu")
        ch1=st.sidebar.selectbox(("Menu"),("Home","Account","Add/Delete Account","Employee","Salary","Leave","Attendance","Project","Department"))
        if 'login1' not in st.session_state:
            st.session_state.login1=False
        if(ch1=="Home"):
            st.image("home.jpeg")
        elif(ch1=="Account"):
            ch2=st.selectbox(("Account"),("Account","login","logout","Update password"))
            if(ch2=="Account"):
                st.image("account4.jpeg")
            elif(ch2=="login"):
                eid=st.text_input("Enter Admin Email id")
                epw=st.text_input("Enter password")
                btn=st.button("Login")
                if btn:
                    if(Admin.check_admin(eid,epw)):
                        st.session_state.login1=True
                        st.write("Login Successfully")
                    else:
                        st.write("Login Failed")
            elif(ch2=="logout"):
                st.session_state.login1=False
                st.write("Your Account to be logged out")
            elif(ch2=="Update password"):
                Admin.updatepassword()
        elif(ch1=="Employee" and  st.session_state.login1==True):
            ch3=st.selectbox(("Employee"),("Employee","Add new employee","Delete Employee","View Employees","view employee by id"))
            if(ch3=="Employee"):
                st.image("login.jpeg")
            elif(ch3=="Add new employee"):
                Admin.Addemployee()
            elif(ch3=="Delete Employee"):
                Admin.Remove_Employ()
            elif(ch3=='View Employees'):
                Admin.Display_Employees()
            elif(ch3=="view employee by id"):
                Admin.viewEmploy()
        elif(ch1=="Salary"  and  st.session_state.login1==True):
            ch4=st.selectbox(("Salary"),("Salary","Add salary","Update salary","Delete salary","View salary"))
            if(ch4=="Salary"):
                st.image("salay5.jpeg")
            elif(ch4=="Add salary"):
                Admin.Addsalary()
            elif(ch4=="Update salary"):
                Admin.updatesalary()
            elif(ch4=="Delete salary"):
                Admin.Remove_salary()
            elif(ch4=="View salary"):
                Admin.viewsalary()
        elif(ch1=="Leave"  and  st.session_state.login1==True):
            ch5=st.selectbox(("Leave"),("Leave","Update leave","view leave"))
            if(ch5=="Leave"):
                st.image("leave4.jpeg")
            elif(ch5=="view leave"):
                Admin.viewleave()
            elif(ch5=="Update leave"):
                Admin.leave()
        elif(ch1=="Add/Delete Account"  and  st.session_state.login1==True):
            ch6=st.selectbox(("Account"),("Account","Create employee login","Delete employee login","Create new admin","Delete admin"))
            if(ch6=="Account"):
                st.image("login1.jpeg")
            elif(ch6=="Create employee login"):
                Admin.elogin()
            elif(ch6=="Delete employee login"):
                Admin.Remove_elogin()
            elif(ch6=="Create new admin"):
                Admin.createadmin()
            elif(ch6=="Delete admin"):
                Admin.Remove_adminlogin()
        elif(ch1=="Project"  and  st.session_state.login1==True):
            ch7=st.selectbox(("Project"),("Project","Assign project","View project","Delete project"))
            if(ch7=="Project"):
                st.image("project4.jpeg")
            elif(ch7=="Assign project"):
                Admin.Addproject()
            elif(ch7=="View project"):
                Admin.viewproject()
            elif(ch7=="Delete project"):
                Admin.removeproject()
        elif(ch1=="Department"  and  st.session_state.login1==True):
            ch8=st.selectbox(("Department"),("Department","Add department","View department","Update department","Delete department"))
            if(ch8=="Department"):
                st.image("depart2.jpeg",width=700)
            elif(ch8=="Add department"):
                Admin.Adddepartment()
            elif(ch8=="View department"):
                Admin.viewdepart()
            elif(ch8=="Update department"):
                Admin.updatedepart()
            elif(ch8=="Delete department"):
                Admin.Remove_depart()
        elif(ch1=="Attendance"  and  st.session_state.login1==True):
            ch9=st.selectbox(("Attendance"),("Attendance","View attendance","View attendance by id"))
            if(ch9=="Attendance"):
                st.image("attend2.jpeg")
            elif(ch9=="Attenadance"):
                st.image("attend.jpeg")
            elif(ch9=="View attendance"):
                Admin.viewAttend()
            elif(ch9=="View attendance by id"):
                Admin.attbyid()
        else:
            st.write("Please Login and continue")
            st.image("loading.jpeg")
       
     
import streamlit as st
import mysql.connector
import time



# making Connection
con = mysql.connector.connect(
	host="localhost", user="root", password="Nagercoil@9488", database="ems")


ch=st.sidebar.selectbox(("Role"),("Role","Employee","Admin",))
if(ch=="Role"):
    #st.markdown("<center> <h1>Welcome<h1> </center>",unsafe_allow_html=True)
    st.title("EMPLOYEE MANAGEMENT SYSTEM")
    st.image("role1.jpeg")
elif(ch=="Employee"):
    employee.welcome()
elif(ch=="Admin"):
    Admin.welcome()


