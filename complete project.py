import tkinter
from tkinter import *
import tkinter.messagebox
import re
import pymysql

class createaccount:
   
    #mycon = pymysql.connect(host="localhost", user="root", password="lavisingh", database="project")
    def __init__(self,root):

        frame=Frame(root,bg="grey")
        frame.pack()




        
        # labels
        
        self.lblregistrationform = Label(frame, text="REGISTRATION FORM",bg="pink",font=20)
        self.lblregistrationform.grid(row=1,column=10)

        
        
        self.lblloginform = Label(frame, text="LOGIN FORM",bg="olive",font=20)
        self.lblloginform.grid(row=5,column=10)

              
        
        self.lblforgotpassword = Label(frame, text="FORGOT PASSWORD",bg="yellow",font=20)
        self.lblforgotpassword.grid(row=8,column=10)

                
        self.lblupdatedetails=Label(frame, text="UPDATE DETAILS",bg="orange",font=20)
        self.lblupdatedetails.grid(row=12, column=10)

        self.lbldelete=Label(frame, text="DELETE DETAILS",bg="red",font=20)
        self.lbldelete.grid(row=15, column=10)
        
        # create account
        
        self.lblfirstname = Label(frame, text="FIRST NAME")
        self.lblfirstname.grid(row=0,column=0)
        self.varfirstname = StringVar()
        self.txtfirstname = Entry(frame, textvariable=self.varfirstname, bd=3,width=35)
        self.txtfirstname.grid(row=0, column=1)

        self.lbllastname = Label(frame, text="LAST NAME")
        self.lbllastname.grid(row=1, column=0)
        self.varlastname = StringVar()
        self.txtlastname = Entry(frame, textvariable=self.varlastname, bd=3, width=35)
        self.txtlastname.grid(row=1, column=1)

        self.lblemailid = Label(frame, text="EMAIL ID")
        self.lblemailid.grid(row=2, column=0)
        self.varemailid = StringVar()
        self.txtemailid = Entry(frame, textvariable=self.varemailid, bd=3, width=35)
        self.txtemailid.grid(row=2, column=1)

        self.lblpassword = Label(frame, text="PASSWORD")
        self.lblpassword.grid(row=3, column=0)
        self.varpassword = StringVar()
        self.txtpassword = Entry(frame, textvariable=self.varpassword, bd=3, width=35,show="*")
        self.txtpassword.grid(row=3, column=1)

        self.btncreateaccount=Button(frame, text="CREATE ACCOUNT",bd=5)
        self.btncreateaccount.grid(row=4, column=3)
        self.btncreateaccount.bind("<Button-1>",self.btncreateaccount_button_1)

        #login

        self.lblemailid1 = Label(frame, text="EMAIL ID")
        self.lblemailid1.grid(row=5, column=0)
        self.varemailid1 = StringVar()
        self.txtemailid1 = Entry(frame, textvariable=self.varemailid1, bd=3, width=35)
        self.txtemailid1.grid(row=5, column=1)

              
        self.lblpassword1 = Label(frame, text="PASSWORD")
        self.lblpassword1.grid(row=6, column=0)
        self.varpassword1 = StringVar()
        self.txtpassword1 = Entry(frame, textvariable=self.varpassword1, bd=3, width=35,show="*")
        self.txtpassword1.grid(row=6, column=1)

     
        self.btnloginform=Button(frame, text="LOGIN",bd=5)
        self.btnloginform.grid(row=7, column=3)
        self.btnloginform.bind("<Button-1>",self.btnloginform_button_1)        

        #forgot password
        
        self.lblenteremailid = Label(frame, text="ENTER EMAIL ID AND CLICK ON GET PASSWORD")
        self.lblenteremailid.grid(row=8, column=0)
        self.varenteremailid = StringVar()
        self.txtenteremailid = Entry(frame, textvariable=self.varenteremailid, bd=3, width=35)
        self.txtenteremailid.grid(row=8, column=1)
        
        self.lblyourpassword = Label(frame, text="YOUR PASSWORD WILL APPEAR HERE AFTER CLICK")
        self.lblyourpassword.grid(row=9, column=0)
        self.varyourpassword = StringVar()
        self.txtyourpassword = Entry(frame, textvariable=self.varyourpassword, bd=3, width=35)
        self.txtyourpassword.grid(row=9, column=1)
             
        self.btnforgotpassword=Button(frame, text="GET PASSWORD",bd=5)
        self.btnforgotpassword.grid(row=10, column=3)
        self.btnforgotpassword.bind("<Button-1>",self.btnforgotpassword_button_1)        

        #update
        
        self.lblenteremailidchange = Label(frame, text="ENTER EMAIL ID")
        self.lblenteremailidchange.grid(row=11, column=0)
        self.varenteremailidchange = StringVar()
        self.txtenteremailidchange = Entry(frame, textvariable=self.varenteremailidchange, bd=3, width=35)
        self.txtenteremailidchange.grid(row=11, column=1)
        
        self.lblenternewemailid = Label(frame, text="ENTER NEW EMAIL ID")
        self.lblenternewemailid.grid(row=12, column=0)
        self.varenternewemailid = StringVar()
        self.txtenternewemailid = Entry(frame, textvariable=self.varenternewemailid, bd=3, width=35)
        self.txtenternewemailid.grid(row=12, column=1)

        self.lblenternewpassword = Label(frame, text="ENTER NEW PASSWORD")
        self.lblenternewpassword.grid(row=13, column=0)
        self.varenternewpassword = StringVar()
        self.txtenternewpassword = Entry(frame, textvariable=self.varenternewpassword, bd=3, width=35,show="*")
        self.txtenternewpassword.grid(row=13, column=1)

               
        self.btnupdatedetails=Button(frame, text="UPDATE DETAILS",bd=5)
        self.btnupdatedetails.grid(row=14, column=3)
        self.btnupdatedetails.bind("<Button-1>",self.btnupdatedetails_button_1)        

        #delete
        self.lblemailiddelete = Label(frame, text="EMAIL ID")
        self.lblemailiddelete.grid(row=15, column=0)
        self.varemailiddelete = StringVar()
        self.txtemailiddelete = Entry(frame, textvariable=self.varemailiddelete, bd=3, width=35)
        self.txtemailiddelete.grid(row=15, column=1)

              
        self.btndelete=Button(frame, text="DELETE DETAILS",bd=5)
        self.btndelete.grid(row=16, column=3)
        self.btndelete.bind("<Button-1>",self.btndelete_button_1)
        


    def btncreateaccount_button_1(self,event):   # button for create account
        firstname=self.varfirstname.get()
        lastname=self.varlastname.get()
        emailid=self.varemailid.get()
        password=self.varpassword.get()
        e=re.compile(r"\w+\.?\w*@\w+\.[a-z]{2,3}")
        emailidmatch=e.match(emailid)
        p=re.compile(r"[A-Z]+\w*\W{1}\w*")
        passwordmatch=p.match(password)
       
        if(  firstname!='' and lastname!='' and emailid!='' and password!=''):
            
            if( emailidmatch and passwordmatch and emailidmatch.group()==emailid and passwordmatch.group()==password and len(password)>8 ):               
                                          
                mycursor = createaccount.mycon.cursor()
                strquery="insert into customer values(%s,%s,%s,%s)"
                mycursor.execute(strquery, (firstname,lastname,emailid,password))
                createaccount.mycon.commit()           
                self.varfirstname.set('')
                self.varlastname.set('')
                self.varemailid.set('')
                self.varpassword.set('')                                          
                                                 
                                                                        
            else:         
                      
           
                tkinter.messagebox.showinfo(" create account"," emailid  shoud be  of the form  [a-z,A-Z,_, . ,0-9]@[a-z,A-Z,_,0-9].[a-z,A-Z,_,0-9](3 charcters compulsory) and password should be greater than 8 character and password should have one uppercase at starting(compulsory),one special character( e.g.=@,!) at any position(compulsory) and lowercase(not compulsory)")
           
     
        else:            
            
            tkinter.messagebox.showinfo("create account","complete your entry")
            
  
            

            
     
        
    def btnloginform_button_1(self,event):      # button for login        
                                        
        emailid1=self.varemailid1.get()
        password1=self.varpassword1.get()
        mycursor = createaccount.mycon.cursor()
        strquery="select * from customer"
        mycursor.execute(strquery)
        createaccount.mycon.commit()
        
        if(emailid1!='' and password1!=''):
            
            for row in mycursor.fetchall():        
                   
                                                       
             
                if(emailid1==row[2] and password1==row[3] ):              
                
                
                
                    tkinter.messagebox.showinfo("login","successfully login")
                 
                    self.varemailid1.set('')
                    self.varpassword1.set('')
                    break
        
            if( self.varemailid1.get() and self.varpassword1.get()):
            
            
            
                tkinter.messagebox.showinfo("login","incorrect emailid or password")
                 
        else:
            
            
            tkinter.messagebox.showinfo("login","complete your entry")
            
               
                 
               
                
                
             
  
            
    def btnforgotpassword_button_1(self,event):                   # button for forgot password
        
         enteremailid=self.varenteremailid.get()
         mycursor = createaccount.mycon.cursor()
         strquery="select * from customer"
         mycursor.execute(strquery)
         createaccount.mycon.commit()
         if(enteremailid!=''):
             
             for row in mycursor.fetchall():         
                      
                                                      
                                    
                 if( enteremailid==row[2]  ):
                     
                     msgresult=tkinter.messagebox.askyesno("delete","get password")
                     if(msgresult==True):
                         
                         mycursor = createaccount.mycon.cursor()
                         strquery="select * from customer where emailid=%s"
                         mycursor.execute(strquery,enteremailid)
                         createaccount.mycon.commit()
                         self.varenteremailid.set('')
                         self.varyourpassword.set(mycursor.fetchone()[3])
                         break               
                                                               
                        
                     else:
                         
                         tkinter.messagebox.showinfo("forgot password","passwword dump")
                         self.varenteremailid.set('')
                         break
        
             if(self.varenteremailid.get()  ):            
            
                                                     
                 tkinter.messagebox.showinfo("forgot password","incorrect emailid ")
           
     
         else:             
                        
             tkinter.messagebox.showinfo("forgot password","complete your entry")





             
            
             
    def btnupdatedetails_button_1(self,event):                     # button for update details
                      
        enteremailidchange=self.varenteremailidchange.get()
        enternewemailid=self.varenternewemailid.get()
        enternewpassword=self.varenternewpassword.get()
        mycursor = createaccount.mycon.cursor()
        strquery="select * from customer"
        mycursor.execute(strquery)
        createaccount.mycon.commit()
        
        e=re.compile(r"\w+\.?\w*@\w+\.[a-z]{2,3}")
        emailidmatch=e.match(enternewemailid)
        p=re.compile(r"[A-Z]+\w*\W{1}\w*")
        passwordmatch=p.match(enternewpassword)       
                        
            
        if( enternewemailid!='' and enternewpassword!='' and enteremailidchange!=''):            
            
            for row in mycursor.fetchall():               
                                            
                if(  enteremailidchange==row[2] and emailidmatch and passwordmatch and emailidmatch.group()==enternewemailid and passwordmatch.group()==enternewpassword and len(enternewpassword)>8  ):
               
                               
                    msgresult=tkinter.messagebox.askyesno("update","are you sure you want to update information ")
                    if(msgresult==True):
                    
                        mycursor = createaccount.mycon.cursor()
                        strquery="update customer set emailid=%s ,password=%s where emailid=%s"
                        mycursor.execute(strquery,(enternewemailid,enternewpassword,enteremailidchange))
                        createaccount.mycon.commit()
                        self.varenteremailidchange.set('')
                        self.varenternewemailid.set('')               
                        self.varenternewpassword.set('')                                             
                        break                                                                                     
                    else:                    
                                         
                        tkinter.messagebox.showinfo("update","not updated")
                        self.varenteremailidchange.set('')
                        self.varenternewemailid.set('')               
                        self.varenternewpassword.set('') 
                        break      
               
                  
            if(self.varenternewemailid.get()):            
                                                        
           
                 tkinter.messagebox.showinfo("update","incorrect emailid or incorrect newemailid or incorrect new password")                     
                   
        else:            
            
            tkinter.messagebox.showinfo("update","complete your entry")            
                                                                               
                                                                            
                                                                                        
                                                                              
                                                 
                                         
                                                                                                            
                                                                             
                                              
                
    def btndelete_button_1(self,event):                              # button for delete
       
        deleteemailid=self.varemailiddelete.get()
        mycursor = createaccount.mycon.cursor()
        strquery="select * from customer"
        mycursor.execute(strquery)
        createaccount.mycon.commit()                
        if(deleteemailid!=''):
            
            for row in mycursor.fetchall():                                            
                               
                                     
                if(deleteemailid==row[2]  ):
                
                    msgresult=tkinter.messagebox.askyesno("delete","are you sure you want to delete information ")
                    if(msgresult==True):
                    
                        mycursor = createaccount.mycon.cursor()
                        strquery="delete from customer where emailid=%s "
                        mycursor.execute(strquery,deleteemailid)
                        createaccount.mycon.commit()
                        self.varemailiddelete.set('')             
                        break   
                       
                    else:                    
                     
                        tkinter.messagebox.showinfo("delete","not deleted")
                        self.varemailiddelete.set('')
                        break 
            
        
            if(self.varemailiddelete.get()  ):        
                                             
           
                tkinter.messagebox.showinfo("delete","incorrect emailid ")
           
        else:            
            
            tkinter.messagebox.showinfo("delete","complete your entry")          
           
          
                                            
                                                                        
                
               
                                                                       
              
root=Tk()
root.state("z")
createaccount(root)

root.mainloop()
