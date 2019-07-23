import tkinter


from tkinter import *
import tkinter.messagebox
import tkinter.scrolledtext 
import tkinter.filedialog
from tkinter.font import Font
import re
class notepad:
    
          
    def __init__(self,master):
      
        self.master=master
        
        
        
        self.horizontalscroll=Scrollbar(self.master,orient=HORIZONTAL)
        self.horizontalscroll.pack(side=BOTTOM,fill=X)
        self.verticalscroll=Scrollbar(self.master)
        
        self.verticalscroll.pack(side="right",fill=Y)
        self.textarea= Text (self.master,wrap=NONE,width=200,height=100,xscrollcommand=self.horizontalscroll.set,yscrollcommand=self.verticalscroll.set)
        self.textarea.pack()
        self.horizontalscroll.config(command=self.textarea.xview)
   
     
        
        self.verticalscroll.config(command=self.textarea.yview)
        
        self.mainmenu=Menu(self.master)
        self.master.config(menu=self.mainmenu)
        
        self.filemenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="File",menu=self.filemenu)
                                                                                                                                                                                                                    
        self.filemenu.add_command(label="New",command=self.new)
        self.filemenu.add_command(label="Open",command=self.open)
        
        self.filemenu.add_command(label="Saveas",command=self.saveas)
        self.filemenu.add_command(label="delete",command=self.delete)
        self.filemenu.add_command(label="exit",command=self.exit)
   
        self.editmenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="Edit",menu=self.editmenu)
        self.editmenu.add_command(label="Undo", command=self.undo)
        self.editmenu.add_command(label="Redo",command=self.redo)
        self.editmenu.add_command(label="Cut",command=self.cut)
        self.editmenu.add_command(label="Paste",command=self.paste)
        self.editmenu.add_command(label="copy",command=self.copy)
        self.editmenu.add_command(label="replace",command=self.replace)
        self.editmenu.add_command(label="selectall",command=self.selectall)
        self.editmenu.add_command(label="deselectall",command=self.deselectall)
        self.editmenu.add_command(label="highlight line",command=self.highlightline)
        self.editmenu.add_command(label="find....",command=self.find)
        
        self.formatmenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="format",menu=self.formatmenu)
        self.formatmenu.add_command(label="font",command=self.font)
          
        self.mainmenu.add_cascade(label="About",command=self.about)
         
    def  open(self):
        
        
        file=tkinter.filedialog.askopenfile(filetypes = (("All files", "*.*"),("text file","*.txt") ))
                                                   
        self.textarea.delete('1.0', END)                                              
        if(file!=None ):
          
            filename=file
           
            contents=file.read()                           
                
            self.textarea.insert('1.0',contents)
            file.close()
        
        
    def saveas(self):
        file=tkinter.filedialog.asksaveasfile(filetypes=(("All files", "*.*"),("text file","*.txt")))
                       
                                                     

                                                     
        if(file!=None):
            
            
            contents=self.textarea.get('1.0',END)
            file.write(contents)
            file.close()
            
    def delete(self):
        
        self.textarea.delete("sel.first", "sel.last")
       
            
    def undo(self):
        self.textarea.edit_undo()
        
    def redo(self):
        
        
        self.textarea.edit_redo()
            
    def paste(self):
        
        self.textarea.event_generate('<<Paste>>')     
                                                
        
                
    def cut(self):
        
        
        self.textarea.event_generate('<<Cut>>')
       
        
        
        
    def copy(self):
        
        self.textarea.event_generate('<<Copy>>')
        
        
                       
                
        
    def about(self):
        tkinter.messagebox.showinfo("about","it is a notepad made with tkinter(python module)")
        
            
    def exit(self):
        
        self.master.destroy()
        

    def new(self):        
        
        self.textarea.delete('1.0', END)
        
    def replace(self):
        
        self.top=Toplevel(self.master)
        self.top.title("replace dialog")
        self.lblreplacewhat = Label(self.top, text="REPLACE WHAT ")
        self.lblreplacewhat.grid(row=0,column=0)
        self.varreplacewhat = StringVar()
        self.txtreplacewhat = Entry(self.top, textvariable=self.varreplacewhat, bd=3,width=35)
        self.txtreplacewhat.grid(row=0, column=1)

        self.lblreplacewith = Label(self.top, text="REPLACE WITH")
        self.lblreplacewith.grid(row=1, column=0)
        self.varreplacewith = StringVar()
        self.txtreplacewith = Entry(self.top, textvariable=self.varreplacewith, bd=3, width=35)
        self.txtreplacewith.grid(row=1, column=1)
        
        
        self.btnreplaceall=Button(self.top, text="REPLACE ALL",bd=5)
        self.btnreplaceall.grid(row=4, column=3)
        self.btnreplaceall.bind("<Button-1>",self.btnreplaceall_button_1)

        
        self.btncancel=Button(self.top, text="CANCEL",bd=5)
        self.btncancel.grid(row=4, column=4)
        self.btncancel.bind("<Button-1>",self.btncancel_button_1)
        
    def  btncancel_button_1(self,event):
        
        self.top.destroy()
        
        

    def btnreplaceall_button_1(self,event):
        
        if(self.varreplacewhat.get() and self.varreplacewith.get()):
            
            
            replacecompile=re.compile(self.varreplacewhat.get())
        
            str1=self.textarea.get('1.0',END)
            replacefindall =replacecompile.findall(str1)
           
            if(replacefindall!=[]):
                
                replacesub =replacecompile.sub(self.varreplacewith.get(),str1)
      
                
                
                self.textarea.delete('1.0', END) 
                self.textarea.insert('1.0',replacesub)
                self.top.destroy()
            else:
                
                               
                tkinter.messagebox.showinfo("replace","content not found or nothing is written on notepad vs")
                self.top.destroy()
          

                
            
    
    
                
        
        else:
            
            tkinter.messagebox.showinfo("replace","complete your entry or nothing is written on notepad vs")
            self.top.destroy()
        
    def find(self):
        
        self.top=Toplevel(self.master)
        self.top.title("find dialog")
        self.lblfindwhat = Label(self.top, text="FIND WHAT ")
        self.lblfindwhat.grid(row=0,column=0)
        self.varfindwhat = StringVar()
        self.txtfindwhat = Entry(self.top, textvariable=self.varfindwhat, bd=3,width=35)
        self.txtfindwhat.grid(row=0, column=1)


        
        
        self.btnfindall=Button(self.top, text="FIND ALL",bd=5)
        self.btnfindall.grid(row=4, column=3)
        self.btnfindall.bind("<Button-1>",self.btnfindall_button_1)

        
        
        
        self.btncancel=Button(self.top, text="CANCEL",bd=5)
        self.btncancel.grid(row=4, column=4)
        self.btncancel.bind("<Button-1>",self.btncancel_button_1)

    def btnfindall_button_1(self,event):
        print(self.textarea.index(INSERT))
        self.textarea.tag_add("sel","2.7","2.9")
        self.textarea.tag_config("sel",background="green")
        if(self.varfindwhat.get()):
            
            
            findcompile=re.compile(self.varfindwhat.get())
        
            str1=self.textarea.get('1.0',END)
            findfindall =findcompile.findall(str1)
            m=findfindall.span()
            
            
            
            x1=len(self.textarea.get('1.0','1.10000000000'))
            x2=len(self.textarea.get('1.0','2.10000000000'))
            x3=len(self.textarea.get('1.0','3.10000000000'))
            x4=len(self.textarea.get('1.0','4.10000000000'))
            v=str(m[0])            
            b=str(m[1])
            v1=str(m[0]-(x1+1))           
            b1=str(m[1]-(x1+1))
            print(v1)
            print(b1)
            v2=str(m[0]-(x2+1))            
            b2=str(m[1]-(x2+1))             
            v3=str(m[0]-(x3+1))            
            b3=str(m[1]-(x3+1))
            v4=str(m[0]-(x4+1))            
            b4=str(m[1]-(x4+1))
            self.textarea.tag_add("sel","1."+v,"1."+b)
            self.textarea.tag_config("sel",background="green")
            self.textarea.tag_add("sel","2."+v1,"2."+b1)
            self.textarea.tag_config("sel",background="green")
            self.textarea.tag_add("sel","3."+v2,"3."+b2)
            self.textarea.tag_config("sel",background="green")
            self.textarea.tag_add("sel","4."+v3,"4."+b3)
            self.textarea.tag_config("sel",background="green")
            self.textarea.tag_add("sel","5."+v4,"5."+b4)
            self.textarea.tag_config("sel",background="green")
            
            
        
            
          
      
                
             
                               
         
                     
                              
               
            self.top.destroy()
        
        else:
            
            tkinter.messagebox.showinfo("replace","complete your entry ")
    
            
                
    def selectall(self):
        self.textarea.tag_add("sel","1.0",END)
        self.textarea.tag_config("sel",background="green")

    def deselectall(self):
        
        self.textarea.tag_remove("sel","1.0",END)
        
        
    def highlightline(self):
        
        
        self.top=Toplevel(self.master)
        self.top.title("highlight dialog")
        self.lblhighlightline = Label(self.top, text="HIGHLIGHT THE LINE NO. ")
        self.lblhighlightline.grid(row=0,column=0)
        self.varhighlightline= StringVar()
        self.txthighlightline = Entry(self.top, textvariable=self.varhighlightline, bd=3,width=35)
        self.txthighlightline.grid(row=0, column=1)

 
        
        
        self.btnhighlight=Button(self.top, text="OK",bd=5)
        self.btnhighlight.grid(row=4, column=3)
        self.btnhighlight.bind("<Button-1>",self.btnhighlightline_button_1)

                
        
        self.btncancel=Button(self.top, text="CANCEL",bd=5)
        self.btncancel.grid(row=4, column=5)
        self.btncancel.bind("<Button-1>",self.btncancel_button_1)

    def btnhighlightline_button_1(self,event):
        
        if(self.varhighlightline.get()  ):
            
            
            highlightline=self.varhighlightline.get()
            highlightlineend=str(int(highlightline)+1)
            
            self.textarea.tag_add("sel",highlightline+".0",highlightline+".100000 ")
            self.textarea.tag_config("sel",background="green")
        
            self.top.destroy()
            
        else:
            
            tkinter.messagebox.showinfo("highlight","complete your entry or blank line will not highlight ")
            self.top.destroy()
        
    
    def font(self):
        
        self.top=Toplevel(self.master)
        self.top.title("font dialog")
        
        self.lblcolor = Label(self.top, text="TEXT COLOR: ")
        self.lblcolor.grid(row=1,column=0)
        self.varcolor= StringVar()
        self.txtcolor = Entry(self.top, textvariable=self.varcolor, bd=3,width=20)
        self.txtcolor.grid(row=2, column=0)
       
        self.listboxcolor = Listbox(self.top)
            
        self.listboxcolor.insert(1,"red")
        self.listboxcolor.insert(2,"orange")
        self.listboxcolor.insert(3,"blue")
        self.listboxcolor.insert(4,"pink")
        self.listboxcolor.insert(5,"yellow")
        self.listboxcolor.insert(6,"green")
        self.listboxcolor.insert(7,"black")
        self.listboxcolor.insert(8,"brown")
        self.listboxcolor.insert(9,"olive")
        self.listboxcolor.insert(10,"purple")     
        self.listboxcolor.insert(11,"grey")
        self.listboxcolor.insert(12,"white")
        
        
        self.listboxcolor.grid(row=3,column=0,padx=20,pady=20)
        
        
        self.listboxcolor.bind("<<ListboxSelect>>",self.btnfontlistboxcolor_button_1)


        self.listboxfontsize = Listbox(self.top)
        self.lblfontsize = Label(self.top, text="TEXT SIZE: ")
        self.lblfontsize.grid(row=1,column=1)
        self.varfontsize= StringVar()
        self.txtfontsize = Entry(self.top, textvariable=self.varfontsize, bd=3,width=20)
        self.txtfontsize.grid(row=2, column=1)
        
        self.listboxfontsize.insert(1,"10")
        self.listboxfontsize.insert(2,"15")
        self.listboxfontsize.insert(3,"20")
        self.listboxfontsize.insert(4,"25")
        self.listboxfontsize.insert(5,"30")
        self.listboxfontsize.insert(6,"35")
        self.listboxfontsize.insert(7,"40")
        self.listboxfontsize.insert(8,"45")
        self.listboxfontsize.insert(9,"50")
        self.listboxfontsize.insert(10,"55")     
        self.listboxfontsize.insert(11,"60")
        self.listboxfontsize.insert(12,"65")
        self.listboxfontsize.insert(12,"70")
        
        self.listboxfontsize.grid(row=3,column=1,padx=20,pady=20)
        self.listboxfontsize.bind("<<ListboxSelect>>",self.btnfontlistboxfontsize_button_1)
        
        self.listboxbackground = Listbox(self.top)
        self.lblbackground = Label(self.top, text="BACKGROUND COLOR: ")
        self.lblbackground.grid(row=1,column=2)
        self.varbackground= StringVar()
        self.txtbackground = Entry(self.top, textvariable=self.varbackground, bd=3,width=20)
        self.txtbackground.grid(row=2, column=2)
        
        self.listboxbackground.insert(1,"red")
        self.listboxbackground.insert(2,"orange")
        self.listboxbackground.insert(3,"blue")
        self.listboxbackground.insert(4,"pink")
        self.listboxbackground.insert(5,"yellow")
        self.listboxbackground.insert(6,"green")
        self.listboxbackground.insert(7,"black")
        self.listboxbackground.insert(8,"brown")
        self.listboxbackground.insert(9,"olive")
        self.listboxbackground.insert(10,"purple")     
        self.listboxbackground.insert(11,"grey")
        self.listboxbackground.insert(12,"white")
        
        self.listboxbackground.grid(row=3,column=2,padx=20,pady=20)
        self.listboxbackground.bind("<<ListboxSelect>>",self.btnfontlistboxbackground_button_1)

        self.listboxfontweight = Listbox(self.top)
        self.lblfontweight = Label(self.top, text=" FONT WEIGHT: ")
        self.lblfontweight.grid(row=1,column=3)
        self.varfontweight= StringVar()
        self.txtfontweight = Entry(self.top, textvariable=self.varfontweight, bd=3,width=20)
        self.txtfontweight.grid(row=2, column=3)
        
        self.listboxfontweight.insert(1,"bold")
        self.listboxfontweight.insert(2,"normal")
        
        
        self.listboxfontweight.grid(row=3,column=3,padx=20,pady=20)
        self.listboxfontweight.bind("<<ListboxSelect>>",self.btnfontlistboxfontsize_button_1)


          

  


    def btnfontlistboxcolor_button_1(self,event):
        
        for element in self.listboxcolor.curselection():
            
            
            listboxcolorelement=self.listboxcolor.get(element)
                
            self.varcolor.set(listboxcolorelement)
            self.textarea.configure(foreground=listboxcolorelement)
           

    def btnfontlistboxfontsize_button_1(self,event):
        
        
        for element in self.listboxfontsize.curselection():
            
            
            
            listboxfontsizeelement=self.listboxfontsize.get(element)
            self.fontsizeelement=listboxfontsizeelement 
            self.varfontsize.set(self.fontsizeelement)
            if(self.fontsizeelement):
                
                fontsize=Font(size=self.fontsizeelement)
                self.textarea.configure(font=fontsize)
                
            if(self.fontweightelement and self.fontsizeelement):
                
                    
                fontsize=Font(size=self.fontsizeelement,weight=self.fontweightelement)
                self.textarea.configure(font=fontsize) 
                   
            
                
                
                
            


        for element in self.listboxfontweight.curselection():
            
            
            
            
            listboxfontweightelement=self.listboxfontweight.get(element)
            self.fontweightelement=listboxfontweightelement 
            self.varfontweight.set(self.fontweightelement)
            if(self.fontweightelement):
                
                fontweight=Font(weight=self.fontweightelement)
                self.textarea.configure(font=fontweight) 
               


            if(self.fontweightelement and self.fontsizeelement):
                
                fontweight=Font(weight=self.fontweightelement,size=self.fontsizeelement)
                self.textarea.configure(font=fontweight) 
                
                    
                   
           
    def btnfontlistboxbackground_button_1(self,event):
        
        
        
        for element in self.listboxbackground.curselection():
            
            
            
            
            listboxbackgroundelement=self.listboxbackground.get(element)
             
            self.varbackground.set(listboxbackgroundelement)
            
            self.textarea.configure(background=listboxbackgroundelement)
            

  
         
       



               
root=Tk()
root.state('z')
root.title("NOTEPAD  VS")
notepad(root)

root.mainloop()        
