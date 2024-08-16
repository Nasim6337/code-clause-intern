import requests as rt
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from bs4 import BeautifulSoup as bs
from tkinter.filedialog import asksaveasfile



win=Tk()

url_source=StringVar(win)
tag_var=StringVar(win)
class_var_tag=StringVar(win)
class_var_name=StringVar(win)
id_var_tag=StringVar(win)
id_var_name=StringVar(win)

class scrapper:
    tg=""
    sp=""
    main_link=""
    soup=""
    def url_copy(self):
        data=url_source.get()
        self.main_link=rt.get(data)
        print(self.main_link.status_code)
        self.soup=bs(self.main_link.content,"html.parser")
        self.sp=self.soup.prettify()
        text.insert(END,self.sp)
    
    def res(self):
        
    
        
        if (tag_var.get() and class_var_name.get()):
            result.delete('1.0',END)            
            result.insert(END,"Please Enter either tag name or class name at a time ")
            
        elif (tag_var.get() and id_var_name.get()):
            result.delete('1.0',END)
            result.insert(END,"Please Enter either tag name or class name at a time")
        
        elif (class_var_name.get() and id_var_name.get()):
            result.delete('1.0',END)
            result.insert(END,"Please Enter either class name or id at a time ")

        elif(tag_var.get() or class_var_tag.get() or id_var_tag.get()):
            if tag_var.get():
                result.delete('1.0',END)
                tag_res=self.soup.find_all(tag_var.get()) 
                result.insert(END,tag_res)
                
            elif class_var_name.get():
                result.delete('1.0',END)
                class_res=self.soup.find(class_var_tag.get(),class_var_name.get())
                result.insert(END,class_res)
                
                
                
                

            elif id_var_name.get():
                result.delete('1.0',END)
                id_res=self.soup.find(id_var_tag.get(),id_var_name.get())
                result.insert(END,id_res)
                    
            else:
                result.delete('1.0',END)
                result.insert(END,"Invalid Argument")
        else:
            result.delete('1.0',END)
            result.insert(END,"Please Enter tag name and other Attributes")


    def sv_file(self):
        var=asksaveasfile(title="save file",initialdir="\\",filetypes=(("textfile","*.txt"),("all files","*.*")),defaultextension="*.txt")
        data1=result.get("1.0",END)
        var.write(data1)
          
        

      




sr=scrapper()#object of the class
win.geometry("1360x700+2+2")
win.resizable(False,False)
win.config(bg="#ffffb3")
lb=Label(win,text="Please enter your URL and click ok",font=("",27),fg="black",bg="#ffffb3")
lb.place(x=370,y=10)
url=Label(win,text="enter your URL:",font=("",20),bg="#ffffb3")
url.place(x=350,y=80,width=250,height=30)
url_en=Entry(win,font=("",15),bg="#ffff99",textvariable=url_source)
url_en.place(x=600,y=80,width=250,height=30)
bt=Button(win,text="OK",bg="#ffffb3",font=("",20),command=sr.url_copy)
bt.place(x=880,y=80,width=50,height=30)

text=ScrolledText(win)
text.place(x=20,y=120,width=1310,height=200)

desc=Label(win,text="Scrap your Data by Tag name, Class name or \nID name. Enter your choice:",justify=LEFT,font=("",20),bg="#ffffb3")
desc.place(x=370,y=350)

#tag area start
url_tag=Label(win,text="Tag  name:",bg="#ffffb3",font=("",20))
url_tag.place(x=370,y=420)
tag_en=Entry(win,font=("",15),bg="#ffff99",textvariable=tag_var)
tag_en.place(x=550,y=420,width=300,height=30)
Or=Label(win,text="OR",font=("",20),bg="#ffffb3")
Or.place(x=870,y=420)
#tag area end

#class name area start
url_class=Label(win,text="Tag & class:",bg="#ffffb3",font=("",19))
url_class.place(x=370,y=460)
class_en=Entry(win,font=("",15),bg="#ffff99",textvariable=class_var_tag)
class_en.place(x=550,y=460,width=145,height=30)
class_en2=Entry(win,font=("",15),bg="#ffff99",textvariable=class_var_name)
class_en2.place(x=705,y=460,width=145,height=30)
Or=Label(win,text="OR",font=("",20),bg="#ffffb3")
Or.place(x=870,y=455)
#class name area end here


#id area start here
id_tag=Label(win,text="Tag & ID:",bg="#ffffb3",font=("",21))
id_tag.place(x=370,y=500)
id_en=Entry(win,font=("",15),bg="#ffff99",textvariable=id_var_tag)
id_en.place(x=550,y=500,width=145,height=30)
id_en2=Entry(win,font=("",15),bg="#ffff99",textvariable=id_var_name)
id_en2.place(x=705,y=500,width=145,height=30)
Or=Label(win,text="OR",font=("",20),bg="#ffffb3")
Or.place(x=870,y=495)
#id area end here

bt2=Button(win,text="OK",bg="#ffffb3",font=("",20),command=sr.res)
bt2.place(x=670,y=540,width=50,height=30)

result=ScrolledText(win)
result.place(x=10,y=580,width=1280,height=120)
save_file=Button(win,text="S\na\nv\ne",bg="#ffff66",font=("Times New Roman",15),command=sr.sv_file)
save_file.place(x=1300,y=580,width=40,height=120)
win.mainloop()