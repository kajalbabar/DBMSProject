from tkinter import messagebox
from tkinter import *
import os
import mysql.connector
import random


root = Tk()
root.title("Bus Service")
root.configure()
N1=StringVar()
#entry store for dd
d=StringVar()
m=StringVar()
y=StringVar()
s=StringVar()

src1=StringVar()
src1.set(None)
des1=StringVar()
des1.set(None)



src_options=['Mumbai',"Pune","satara"]
dest_options=['Kolhapur','Sangli']


#root.geometry("900x600+250+10")
root.geometry("1366x768")
l1 =Label(root,text="Online Ticket Booking",font=("elephant",30,"bold"),fg="navy blue")
l1.grid(row=0,column=0,padx=450,pady=10 ,sticky=W)

#l1.pack(fill=BOTH,pady=2,padx=1)


name=Label(root,text="Enter Name : ",fg="black",font=("arrial",20,"bold"))
name.grid(row=3,column=0,padx=100,pady=30,sticky=W)

name_entry = Entry(root,textvariable = N1,width=40,bg="lavender")
name_entry.grid(row=3,padx=350,pady=20,column=0,sticky=W)

#var
source_name=Label(root,text="Source : ",fg="black",font=("arrial",20,"bold"))
source_name.grid(row=5,padx=200 , pady=20,column=0,sticky=W)
To = Label(root,text="To",fg="black",font=("arrial",20,"bold"))
To.grid(row=5,padx=575 , pady=20,column=0,sticky=W)
dest_name=Label(root,text="Destination : ",fg="black",font=("arrial",20,"bold"))
dest_name.grid(row=5,padx=700 , pady=20,column=0,sticky=W)

#entries
S1En = OptionMenu(root, src1,*src_options)
S1En.grid(row=5,padx=350 , pady=20,column=0,sticky=W)

D1En = OptionMenu(root, des1,*dest_options)
D1En.grid(row=5,padx=900 , pady=20,column=0,sticky=W)

date=Label(root,text="Enter the date : ",fg="black",font=("arrial",20,"bold"))
date.grid(row=7,padx=200 , pady=20,column=0,sticky=W)

dd=Label(root,text="dd",fg="black",font=("arrial",15,"bold"))
dd.grid(row=8,padx=300, pady=20,sticky=W)

mm=Label(root,text="mm",fg="black",font=("arrial",15,"bold"))
mm.grid(row=8,padx=500, pady=20,sticky=W)

yy=Label(root,text="yyyy",fg="black",font=("arrial",15,"bold"))
yy.grid(row=8,padx=700 , pady=20,column=0,sticky=W)

s1E=Label(root,text="Seat No(Enter Only you want to Cancel)",fg="black",font=("arrial",15,"bold"))
s1E.grid(row=9,padx=300 , pady=20,column=0,sticky=W)


#entries for date
ddEn=Entry(root,textvariable = d,width=15,bg="lavender")
ddEn.grid(row=8,padx=350 , pady=20,column=0,sticky=W)

mmEn=Entry(root,textvariable = m,width=15,bg="lavender")
mmEn.grid(row=8,padx=550 , pady=20,column=0,sticky=W)
yyEn=Entry(root,textvariable = y,width=15,bg="lavender")
yyEn.grid(row=8,padx=755, pady=20,column=0,sticky=W)

s1=Entry(root,textvariable = s,width=15,bg="lavender")
s1.grid(row=9,padx=800, pady=20,column=0,sticky=W)


#--------------------------------------------------------------------------------
#connect to the data
myData =mysql.connector.connect(host='localhost',user='root',password='1214',database='Online_Reservation');
#create cursor
myCursor = myData.cursor()
myCursor.execute("use Online_Reservation");






def confirm():
	
	
	empty=[]
	myCursor.execute('select seat from m_k where avail="y"');
	for x in myCursor:
		empty.append(x[0]);
	#print("Empty")
	#print(empty)
	
	if(len(empty) == 0):
		messagebox.showinfo("Information","No seats Available");
	else:
		seat = random.choice(empty)
		#print("Seat = "+str(seat))
		myCursor.execute ("update m_k set avail='n' where seat = "+str(seat))
		#print(myCursor)
		
		Name=N1.get()
		#print("Name="+Name)
		
		dateEntry = [y.get(),m.get(),d.get()]
		date = ("-").join(dateEntry)
		src=src1.get()
		dest=des1.get()
		
		try:
		      myCursor.execute("insert into Passenger values( NULL ,'"+Name + "', '"+str(date)+"', '"+src + "' , '"+dest+"')" )
		      myCursor.execute("select cost from Cost where Source = '"+src + "' and Destination = '"+dest+"'")
		      #print("select cost from Cost where Source = '"+src + "' and Destination = '"+dest+"'")
		      
		      cost = 0
		      for x in myCursor:
		          cost=x[0]
		      messagebox.showinfo("Information","Your Reservation is Confirmed\n Seat Number "+ str(seat)+"\nCost = "+str(cost))
		      myData.commit()
		except mysql.connector.errors.DataError:
			messagebox.showerror("Error ","Enter Valid date")
			#print("insert into Passenger values( NULL, '"+Name + "', '"+str(date)+"', '"+src + "' , '"+dest+"')" )
		

def cancel():
	seat= s1.get()
	myCursor.execute("update m_k set avail='y' where seat = "+str(seat))
	messagebox.showinfo("Information","Your Reservation is cancelled\n Seat Number "+ str(seat))
	myData.commit()	



'''
def getinfo():
    Name=N1.get()
    print("Name="+Name)
    d1,m1,y1=d.get(),m.get(),y.get()
    print("date")
    print(d1,m1,y1)
    src=src1.get()
    dest=des1.get()
    print("src")
    print(src)
    print(dest)
'''
book = Button(root,text="Confirm",fg='black',command=confirm,bg='cyan',font=("arrial",14,"bold"),width=20)
book.place(x=350,y=500)

delete = Button(root,text="Cancel",fg='black',command=cancel,bg='cyan',font=("arrial",14,"bold"),width=20)
delete.place(x=700,y=500)
root.mainloop()



