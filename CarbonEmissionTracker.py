#Project Class12
#CARBON EMISSION TRACKER
#Joel Bonnie XIIA-09


#IMPORTING MODULES
import csv
from unittest.mock import mock_open
import mysql.connector as mysql
import tkinter
from tkinter import messagebox,ttk
import matplotlib.pyplot as plot

#Declaring global connection and cursor object
global mycon
global mycur



#DEFINING FUNCTIONS

#Function for choice

def getoption():
    #checking condition to show country list
    k=var.get()
    i=checkvar.get()
          
    #checking which option
    try:
        if k==1:
            frame1.forget()
            #option1
            if i==1:
                c_list()
            return compare()
        elif k==2:
            frame1.forget()
            if i==1:
                c_list()
            #option2
            return compare_world()
        elif k==3:
            frame1.forget()
            if i==1:                    
                c_list()
            #option3
            return sources()
    except:
        pass

    else:
        #Error
        messagebox.showerror('Error','Please select an option.')
    

#Function to exit program
def close():
    window.destroy()
    try:
        window2.destroy()
    except:
        pass
    try:
        plot.close('all')
    except:
        pass
    
    

#Function to restart Program
def restart():
    close()
    interface()
    
 
#Function to create Comparison Bar Graph 1
def create_graph1():
    c1=var1.get()
    c2=var2.get()
    #Error Messages
    if c1=="" or c2=="":
        messagebox.showerror("Error","Please enter both countries.")
        return False
    if c1==c2:
        messagebox.showerror("Error","Please enter two different countries.")
        return False
        
    

    
    l=[]
    mycur.execute("select Total from carbonemission where entity=%s",(c1,))
    values=mycur.fetchall()
    if not values:
        #Error
        messagebox.showerror("Error","Country 1 is not Included.")
        return False
    for i in values :
        l+=i
    mycur.execute("select Total from carbonemission where entity=%s",(c2,))
    values=mycur.fetchall()
    if not values:
        #Error
        messagebox.showerror("Error","Country 2 is not Included.")
        return False
    for i in values :
        l+=i
    
    plot.style.use("dark_background")
    x=[c1,c2]
    y=l
    plot.bar(x,y,width=.25,color="#C39977")
    plot.ticklabel_format(axis="y",style='plain')
    plot.xlabel('Country')
    plot.ylabel('Emission in tonnes')
    plot.title('Carbon Emission Comparison')
    plot.tight_layout()
    plot.show()
    
        
    
#Function to create Comparison Bar Graph 2
def create_graph2(c1,c2="World"):
    if c1=="":
        messagebox.showerror("Error","Please enter the country.")
        return False
    if c1=="World":
        #Error
        messagebox.showerror("Error","Please enter another country.")
        return False
        
    
    
    l=[]
    mycur.execute("select Total from carbonemission where entity=%s",(c1,))
    values=mycur.fetchall()
    if not values:
        #Error
        messagebox.showerror("Error","Country is not Included.")
        return False
    for i in values :
        l+=i
    mycur.execute("select Total from carbonemission where entity=%s",(c2,))
    values=mycur.fetchall()
    
    for i in values :
        l+=i

    plot.style.use("dark_background")
    x=[c1,c2]
    y=l
    plot.bar(x,y,width=0.25,color="#C39977")
    plot.ticklabel_format(axis="y",style='plain')
    plot.xlabel('Country')
    plot.ylabel('Emission in tonnes')
    plot.title('Carbon Emission Comparison')
    plot.tight_layout()
    plot.show()

#Function to create Comparison Bar Graph 3
def create_graph3(c1):
    if c1=="":
        #Error
        messagebox.showerror("Error","Please enter the country.")
        return False
   
    
    
    
    mycur.execute("select * from carbonemission where entity=%s",(c1,))
    values=mycur.fetchall()
    if not values:
        #Error
        messagebox.showerror("Error","Country is not Included.")
        return False
    
    l=[]
    for i in values:
        l+=i
    plot.style.use("dark_background")
    y=l[3:]
    x=['Buildings','Industry','Other\nfuel\ncombustion\n','Transport ','Manufact.\n&Constr.  ','Electricity\n&Heat  ','Total']
    plot.bar(x,y,width=.5,color="#C39977")
    plot.ticklabel_format(axis="y",style='plain')
    plot.xlabel('Sources')
    plot.ylabel('Emission in tonnes')
    plot.title('Carbon Emission Sources for '+c1)
    plot.tight_layout()
    
    plot.show()
        

    
#Highlight and relief
def high(event,a):
    if a==0:
        but0['relief']="sunken"
        but0['background']="#C38855"     
        but0['foreground']="white"
        
        
    elif a==1:
        but_create['relief']="sunken"
        but_create['background']="#C38855"
        but_create['foreground']="white"
    elif a==2:
        but1['relief']="sunken"
        but1['background']="#C38855"
        but1['foreground']="white"
    elif a==3:
        but2['relief']="sunken"
        but2['background']="#C38855"
        but2['foreground']="white"
def unhigh(event,a):
    if a==0:
        but0['relief']="raised"
        but0['background']="black"
        but0['foreground']="white"
        
    elif a==1:
        but_create['relief']="raised"
        but_create['background']="black"
        but_create['foreground']="white"
    elif a==2:
        but1['relief']="raised"
        but1['background']="black"
        but1['foreground']="white"
    elif a==3:
        but2['relief']="raised"
        but2['background']="black"
        but2['foreground']="white"     
                  
                 
#Function to create a list of the countries
def c_list():
    global window2
    #creating a new window for country list
    window2=tkinter.Tk()
    window2.title("Country List")
    window2.geometry("250x400")
    window2.resizable(0,0)
    
    label= tkinter.Label(window2,text="COUNTRY LIST",bg="black",fg="white", font=('Quicksand Light',15))
    label.pack(fill="x")
    
    
    mycur.execute("select Entity from carbonemission")
    k=mycur.fetchall()
    s=""
    for i in k:
        s=s+i[0]+"\n"
    text=tkinter.Text(window2,bg="black",fg="white",font=('Arial',10))
    text.pack()
    text.insert(tkinter.END,s)
    

#Get Countries
def c_extract():
    
    mycur.execute('select Entity from carbonemission')
    k=mycur.fetchall()
    t=()
    for i in k:
        t+=i
    return t
    
    
    
#OPTION1
def compare():
    
    frame2=tkinter.Frame(window,bg="black")
    frame2.pack()
    
    label= tkinter.Label(frame2,text="YOU HAVE SELECTED OPTION 1",bg="black",fg="white",font=('Quicksand Light',25))
    label.pack()
    label_1= tkinter.Label(frame2,text="Comparing total emissions for different countries graphically\n",bg="black",fg="white",font=('Arial',13))
    label_1.pack(fill="x")

    
    #Accepting Inputs
    global var1
    global var2

    var1=tkinter.StringVar()
    var2=tkinter.StringVar()
    cvalues=c_extract()
        
    label1=tkinter.Label(frame2,text="Enter the first country",bg="black",fg="#C39977",font=('Arial',10))
    label1.pack(anchor= tkinter.W,fill="x")
    Entry1=ttk.Combobox(frame2,textvariable=var1)
    
    Entry1['values']=cvalues
    Entry1.pack(anchor= tkinter.W,fill="x")
    Entry1.current()
    
    label2=tkinter.Label(frame2,text="Enter the second country",bg="black",fg="#C39977",font=('Arial',10))
    label2.pack(anchor= tkinter.W,fill="x")
    Entry2=ttk.Combobox(frame2,textvariable=var2)
    
    Entry2['values']=cvalues
    Entry2.pack(anchor= tkinter.W,fill="x")
    Entry2.current()
    label=tkinter.Label(frame2,text="\n",bg="black")
    label.pack()
    label= tkinter.Label(frame2,text="Create the Graph",bg="black",fg="white",font=('Arial',10))
    label.pack()
    global but_create
    global but1
    global but2
    but_create=tkinter.Button(frame2,text="Create",bg="black",fg="white",font=('Arial',13),activebackground="#C38855",activeforeground="white",width="16",height="3",command=create_graph1)
    but_create.pack()
    
    #highlighting buttons on hovering    
    but_create.bind("<Enter>",lambda event:high(event,a=1))
    but_create.bind("<Leave>",lambda event:unhigh(event,a=1))
    
    label=tkinter.Label(frame2,text="\n\n",bg="black")
    label.pack()

    #Quit Restart Options
    but1 = tkinter.Button(frame2,text="Restart",width="14",height="2",activebackground="#C38855",activeforeground="white",command=restart,bg="black",fg="white")
    but1.pack()
    but2= tkinter.Button(frame2,text="Quit",width="14",height="2",activebackground="#C38855",activeforeground="white",command=close,bg="black",fg="white")
    but2.pack()
    #highlighting buttons on hovering
    but1.bind("<Enter>",lambda event:high(event,a=2))
    but1.bind("<Leave>",lambda event:unhigh(event,a=2))
    but2.bind("<Enter>",lambda event:high(event,a=3))
    but2.bind("<Leave>",lambda event:unhigh(event,a=3))


#OPTION2
def compare_world():
    frame2=tkinter.Frame(window,bg="black")
    frame2.pack()
    label= tkinter.Label(frame2,text="YOU HAVE SELECTED OPTION 2",bg="black",fg="white",font=('Quicksand Light',25))
    label.pack()
    label_1= tkinter.Label(frame2,text="Comparing total emissions of a country with world average\n",bg="black",fg="white",font=('Arial',13))
    label_1.pack(fill="x")

    #Accepting Inputs
    var1=tkinter.StringVar()
    cvalues=c_extract()
    
    label1=tkinter.Label(frame2,text="Enter the country",bg="black",fg="#C39977",font=('Arial',10))
    label1.pack(anchor= tkinter.W,fill="x")
    Entry1=ttk.Combobox(frame2,textvariable=var1)
    
    Entry1['values']=cvalues
    Entry1.pack(anchor= tkinter.W,fill="x")
    Entry1.current()
    label=tkinter.Label(frame2,text="\n",bg="black")
    label.pack()
    label2= tkinter.Label(frame2,text="Create the Graph",bg="black",fg="white",font=('Arial',10))
    label2.pack()
    
    global but_create
    global but1
    global but2
    but_create=tkinter.Button(frame2,text="Create",bg="black",fg="white",font=('Arial',13),activebackground="#C38855",activeforeground="white",width="16",height="3",command=lambda:create_graph2(var1.get()))
    but_create.pack()
    
    #highlighting buttons on hovering
    but_create.bind("<Enter>",lambda event:high(event,a=1))
    but_create.bind("<Leave>",lambda event:unhigh(event,a=1))

    label=tkinter.Label(frame2,text="\n\n",bg="black")
    label.pack()

    #Quit Restart Options
    but1 = tkinter.Button(frame2,text="Restart",activebackground="#C38855",activeforeground="white",width="14",height="2",command=restart,bg="black",fg="white")
    but1.pack()
    but2= tkinter.Button(frame2,text="Quit",activebackground="#C38855",activeforeground="white",width="14",height="2",command=close,bg="black",fg="white")
    but2.pack()
    #highlighting buttons on hovering
    but1.bind("<Enter>",lambda event:high(event,a=2))
    but1.bind("<Leave>",lambda event:unhigh(event,a=2))
    but2.bind("<Enter>",lambda event:high(event,a=3))
    but2.bind("<Leave>",lambda event:unhigh(event,a=3))



#OPTION3
def sources():
    frame2=tkinter.Frame(window,bg="black")
    frame2.pack()
    label= tkinter.Label(frame2,text="YOU HAVE SELECTED OPTION 3",bg="black",fg="white",font=('Quicksand Light',25))
    label.pack()
    label_1= tkinter.Label(frame2,text="See the various sources for Carbon Emissions for a specified Country\n",bg="black",fg="white",font=('Arial',13))
    label_1.pack(fill="x")

    #Accepting Inputs
    var1=tkinter.StringVar()
    cvalues=c_extract()
    
    label1=tkinter.Label(frame2,text="Enter the country",bg="black",fg="#C39977",font=('Arial',10))
    label1.pack(anchor= tkinter.W,fill="x")
    Entry1=ttk.Combobox(frame2,textvariable=var1)
    
    Entry1['values']=cvalues
    Entry1.pack(anchor= tkinter.W,fill="x")
    Entry1.current()
    label=tkinter.Label(frame2,text="\n",bg="black")
    label.pack()
    label2= tkinter.Label(frame2,text="Create the Graph",bg="black",fg="white",font=('Arial',10))
    label2.pack()
    global but_create
    global but1
    global but2
    but_create=tkinter.Button(frame2,text="Create",bg="black",fg="white",font=('Arial',13),activebackground="#C38855",activeforeground="white",width="16",height="3",command=lambda:create_graph3(var1.get()))
    but_create.pack()
    
    #highlighting buttons on hovering
    but_create.bind("<Enter>",lambda event:high(event,a=1))
    but_create.bind("<Leave>",lambda event:unhigh(event,a=1))
    label=tkinter.Label(frame2,text="\n\n",bg="black")
    label.pack()

    #Quit Restart Options
    but1 = tkinter.Button(frame2,text="Restart",activebackground="#C38855",activeforeground="white",width="14",height="2",command=restart,bg="black",fg="white")
    but1.pack()
    but2= tkinter.Button(frame2,text="Quit",activebackground="#C38855",activeforeground="white",width="14",height="2",command=close,bg="black",fg="white")
    but2.pack()
    #highlighting buttons on hovering
    but1.bind("<Enter>",lambda event:high(event,a=2))
    but1.bind("<Leave>",lambda event:unhigh(event,a=2))
    but2.bind("<Enter>",lambda event:high(event,a=3))
    but2.bind("<Leave>",lambda event:unhigh(event,a=3))

#Function for GRAPHICAL USER INTERFACE

def interface():
    #creating the window
    global window
    window = tkinter.Tk()
    window.title("Carbon Emission Tracker")
    window.geometry("960x540")
    window.resizable(0,0)
    window.configure(bg="black")
    
    #creating the background
    
    bgd=tkinter.PhotoImage(file='C:/CET/BackGround.png')
    label=tkinter.Label(window,image=bgd)
    label.place(x=0,y=0,relwidth=1,relheight=1)
    

    global frame1
    
    
    #Creating The Header   
    frame1=tkinter.Frame(window,bg="black")
    
    frame1.pack()
    labe0= tkinter.Label(frame1,text="CARBON",bg="black",fg="white",font=('Yu Gothic UI',65))
    labe0.pack(fill="x")
    label= tkinter.Label(frame1,text="EMISSION TRACKER",bg="black",fg="white",font=('Quicksand Light',35))
    label.pack(fill="x")
    label2= tkinter.Label(frame1,text="Created by Joel Bonnie\n",bg="black",fg="white",font=('Quicksand Light',13))
    label2.pack(fill="x")
    label3= tkinter.Label(frame1,text="Please select your choice:\n",bg="black",fg="white",font=('Arial',15))
    label3.pack(fill="x")

    #Creating the option selector
    global var
    var=tkinter.IntVar()
    R1=tkinter.Radiobutton(frame1,text=" Compare total emissions for different countries graphically\t\t\t",variable=var,value=1,bg="black",fg="#C39977",font=('Arial',9))
    R1.pack(anchor= tkinter.W)
    R2=tkinter.Radiobutton(frame1,text="Compare total emissions of a country with world average\t\t\t",variable=var,value=2,bg="black",fg="#C39977",font=('Arial',9))
    R2.pack(anchor= tkinter.W)
    R3=tkinter.Radiobutton(frame1,text="  See the various sources for Carbon Emissions for a specified Country\t\t",variable=var,value=3,bg="black",fg="#C39977",font=('Arial',9))
    R3.pack(anchor= tkinter.W)

    global checkvar
    checkvar= tkinter.IntVar()
    checkbox=tkinter.Checkbutton(frame1,text="Show Country List",variable=checkvar,onvalue=1,offvalue=0,bg="black",fg="grey",activebackground="#C38855",font=('Arial',9))
    checkbox.pack()
    
    global but0    
    but0 = tkinter.Button(frame1,text="Next",width="14",height="3",command=getoption,bg="black",fg="white",activebackground="#C38855",activeforeground="white",font=('Arial',10))
    but0.pack()
    #highlighting buttons on hovering    
    but0.bind("<Enter>",lambda event:high(event,a=0))
    but0.bind("<Leave>",lambda event:unhigh(event,a=0))
    


    window.mainloop()


#CREATING THE DATABASE, TABLE AND IMPORTING VALUES FROM CSV FILE 

def create_database():
    #creating database
    mycon=mysql.connect(host="localhost",user="root",passwd="root")
    mycur=mycon.cursor()
    mycur.execute("create database CarbonEmission")
    
    #Connecting mySQL and Python
    mycon=mysql.connect(host="localhost",user="root",passwd="root",database="CarbonEmission")
    mycur=mycon.cursor()

    #creating table
    query='''create table CarbonEmission(Entity char(30),Code char(10),Year bigint ,
            Buildings bigint,Industry bigint,Other_fuel_combustion bigint
            ,Transport bigint,Manufacturing_and_Construction bigint, Electricity_and_Heat
            bigint,Total bigint)'''
    mycur.execute(query)


def import_values():
    
    #Importing Values From CSV File
    obj=open("CarbonEmission.csv","r")
    read=csv.reader(obj)
    records=[]
    k=next(read)
    for i in read:
        records.append([i[0],i[1],int(i[2]),int(i[3]),int(i[4]),int(i[5]),int(i[6]),int(i[7]),int(i[8]),int(i[9])])
    #Connecting mySQL and Python
    mycon=mysql.connect(host="localhost",user="root",passwd="root",database="CarbonEmission")
    mycur=mycon.cursor()
    #inserting into table
    for i in records:
        k=tuple(i)
        query="insert into CarbonEmission values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycur.execute(query,k)

    mycon.commit()

#PROGRAM MAIN
print("Welcome to Carbon Emission Tracker")
print("Initialising....")
try:
    #Initialising Database and Table
    
    create_database()
    
    print("Creating Database....")
    
    import_values()
    print("Importing values and creating table...")
    print("Starting Carbon Emission Tracker...")
    
    interface()
except:
    #Data is already Initialised
    print("Starting Carbon Emission Tracker...")
    mycon=mysql.connect(host="localhost",user="root",passwd="root",database="CarbonEmission")
    mycur=mycon.cursor()
    interface()

    
     

#PROGRAM ENDS
    


