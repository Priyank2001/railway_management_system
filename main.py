from tkinter import *
from classes import *
from tkinter import messagebox
import csv
master = Tk()
usersList = []
curr_userID = -1
#z = user("raj","raj@gmail.com","raj","raj",1)

#usersList.append(z)
#z = user("Vaibhav","baboi@gmail.com","baboi","baboi",2)
#
#usersList.append(z)
trains = []
##test_train = train(1,"Delhi" , "Guwahati" , 300)
##
##trains.append(test_train)
##test_train = train(2,"Jaipur" , "Patna" , 1500)
##
##trains.append(test_train)
############################################################################################################

## Intialising trains

with open('trains.csv',mode ='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        trains.append(train(int(row[0]),row[1],row[2],int(row[3])))
        s = row[4]
        s = s.removeprefix("{")
        s = s.removesuffix("}")
        arr = s.split(":")
        #for elem in arr:
        #    trains[len(trains)-1].addPassenger(int(elem))

############################################################################################################

##intialsing users
with open('users.csv',mode = 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        usersList.append(user(row[1],row[2],row[3],row[4],int(row[0])))
        s = row[5]
        s = s.removeprefix("{")
        s = s.removesuffix("}")
        arr = s.split(":")
        for elem in arr:
            if elem != '':
                usersList[len(usersList)-1].addTicket(int(elem))


############################################################################################################

'''
widgets are added here
'''

def newUserMenu(parent , a):
    global curr_userID , usersList
    b = []
    for x in range(0,5):
            b.append('')
    for x in range(1,5):
        b[x] = a[x].get()
        if b[x] == '':
            messagebox.showwarning("showwarning", 'Any field is left empty')
            return
    newWindow = Toplevel(parent,pady=100,padx=100)
    usersList.append(user(b[1],b[2],b[3],b[4],len(usersList) + 101))
    curr_userID = usersList[len(usersList)-1].ID
    #print(len(usersList))
    Label(newWindow , text=usersList[curr_userID-101].name).pack()


##############################################################################################################
def clear_frame(parent):
   for widgets in parent.winfo_children():
      widgets.destroy()
##############################################################################################################

def bookNowButton(parent,id):
    global curr_userID
    #print(id)
    trains[id-1-100].addPassenger(curr_userID)
    usersList[curr_userID-101].addTicket(id)

def cancelNowButton(id):
    global curr_userID
    trains[id-101].passengersID.remove(curr_userID)
    usersList[curr_userID-101].tickets.remove(id)

def bookTicket(parent):
    clear_frame(parent)
    parent.title("Book  tickets")
    Label(parent, text="ID").grid(row = 1 , column=1 , padx=10,pady=5)
    Label(parent, text="Starting Point").grid(row =1, column=2, padx=10,pady=5)
    Label(parent, text="Destination").grid(row = 1, column=3, padx=10,pady=5)
    Label(parent, text="Price").grid(row =1 , column=4, padx=10,pady=5)
    for idx,item in enumerate(trains):
        Label(parent, text=item.ID).grid(row = idx+2, column=1 , padx=10,pady=5)
        Label(parent, text=item.source).grid(row = idx+2, column=2, padx=10,pady=5)
        Label(parent, text=item.dest).grid(row = idx+2, column=3, padx=10,pady=5)
        Label(parent, text=item.price).grid(row = idx+2, column=4, padx=10,pady=5)
        Button(parent,text="Book now", command=lambda i=parent ,j = item.ID : bookNowButton(i,j)).grid(row = idx+2 ,column = 6 , padx=10,pady=5)

def cancelTicket(parent):
    clear_frame(parent)
    parent.title("Cancel tickets")
    Label(parent, text="ID").grid(row = 1 , column=1 , padx=10,pady=5)
    Label(parent, text="Starting Point").grid(row =1, column=2, padx=10,pady=5)
    Label(parent, text="Destination").grid(row = 1, column=3, padx=10,pady=5)
    Label(parent, text="Price").grid(row =1 , column=4, padx=10,pady=5)
    for idx,item in enumerate(usersList[curr_userID-101].tickets,start = 2):
        Label(parent, text=trains[item-101].ID).grid(row = idx+2, column=1 , padx=10,pady=5)
        Label(parent, text=trains[item-101].source).grid(row = idx+2, column=2, padx=10,pady=5)
        Label(parent, text=trains[item-101].dest).grid(row = idx+2, column=3, padx=10,pady=5)
        Label(parent, text=trains[item-101].price).grid(row = idx+2, column=4, padx=10,pady=5)
        Button(parent,text="Cancel", command=lambda i=parent ,j = item : cancelNowButton(j)).grid(row = idx+2 ,column = 6 , padx=10,pady=5)



###########################################################################################################
def updateProfile():
    a = 10

def enquiry(parent):
    clear_frame(parent)
    Label(parent , text="Name: " ).grid(row = 1 , column=1,padx =10 , pady = 5)
    Label(parent , text=usersList[curr_userID-101].name ).grid(row = 1 , column=2,padx =10 , pady = 5)
    Label(parent , text="E-mail: " ).grid(row = 2 , column=1,padx =10 , pady = 5)
    Label(parent , text=usersList[curr_userID-101].email ).grid(row = 2 , column=2,padx =10 , pady = 5)
    Label(parent , text="Tickets Booked").grid(row=3 , column=0, columnspan=4)
    for idx,item in enumerate(usersList[curr_userID-101].tickets,start = 2):
        Label(parent, text=trains[item-101].ID).grid(row = idx+2, column=1 , padx=10,pady=5)
        Label(parent, text=trains[item-101].source).grid(row = idx+2, column=2, padx=10,pady=5)
        Label(parent, text=trains[item-101].dest).grid(row = idx+2, column=3, padx=10,pady=5)
        Label(parent, text=trains[item-101].price).grid(row = idx+2, column=4, padx=10,pady=5)
        #print(trains[item-101].source , trains[item-101].dest)
   
##############################################################################################################
##############################################################################################################

def existingUserMenu(parent , a):
    global curr_userID , usersList
    b = []
    for x in range(0,3):
            b.append('')
    for x in range(1,3):
        b[x] = a[x].get()
        if b[x] == '':
            messagebox.showwarning("Field left empty", 'Any field is left empty')
            return
    found = False
    for idx,curr in enumerate (usersList,start=0):
        if b[1] == curr.username and b[2] == curr.password:
            curr_userID = curr.ID
            found = True
            break
    if found == False :
        messagebox.showwarning("Not Found", 'Check your username/password')
        return
    newWindow= Toplevel(parent,pady=100,padx=50)
    newWindow.title("Existing User")
    newWindow.geometry("500x500")
    Label(newWindow , text="User Login Successful").grid(row=0, column=0,columnspan=2)
    options = ['Book Tickets','Update Profile','Enquiry']
    buttons = []
    
    #for idx,item in enumerate(options,start = 1):
    Button(newWindow , text = "1. Book Tickets", fg = "black",command=lambda: bookTicket(newWindow) ).grid(row=1, column=0,columnspan=2)
    Button(newWindow , text = "2. Update Profile", fg = "black",command=updateProfile ).grid(row=2, column=0,columnspan=2)
    Button(newWindow , text = "3. Enquiry", fg = "black",command=lambda i = newWindow : enquiry(i) ).grid(row=3, column=0,columnspan=2)
    Button(newWindow , text = "4. Cancel Tickets", fg = "black",command=lambda i = newWindow : cancelTicket(i) ).grid(row=4, column=0,columnspan=2)


##############################################################################################################

##############################################################################################################


def choice_introPage():
    val = v.get()
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master,pady=100,padx=100)
 
    # sets the title of the
    # Toplevel widget
    
    newWindow.title(val)
 
    # sets the geometry of toplevel
    newWindow.geometry("500x500")
    if val == 1:
        Label(newWindow,
          text ="Create an Account").grid(row = 0 , column= 0,columnspan=2)
        Label(newWindow,text = "Name" ).grid(row = 1,column=0)
        Label(newWindow,text = "Email" ).grid(row = 2,column=0)
        Label(newWindow,text = "Username" ).grid(row = 3,column=0)
        Label(newWindow,text = "Password" ).grid(row = 4,column=0)
        
        a = []
        for x in range(0,5):
            a.append(StringVar())
        for x in range(1,5):
            Entry(newWindow,textvariable = a[x]).grid(row = x,column=1)
        Button(newWindow , text ="Submit" , fg = "black" ,command=lambda: newUserMenu(newWindow , a) ).grid(row = 5 , column= 0,columnspan=2)
    elif val == 2:
        Label(newWindow,
          text ="Login").grid(row = 0 , column= 0,columnspan=2)
        Label(newWindow,text = "Username" ).grid(row = 2,column=0)
        Label(newWindow,text = "Password" ).grid(row = 3,column=0)
        a = []
        for x in range(0,3):
            a.append(StringVar())
        for x in range(1,3):
            Entry(newWindow,textvariable = a[x]).grid(row = x+1,column=1)
        Button(newWindow , text ="Submit" , fg = "black" ,command=lambda: existingUserMenu(newWindow , a) ).grid(row = 5 , column= 0,columnspan=2)
##############################################################################################################

##############################################################################################################

##############################################################################################################

v = IntVar()

def userMode():
    master1 = Toplevel(master)
    introPage = Canvas(master1, width=700, height=700)
    introPage.pack()
    Label(introPage,text="Welcome to Railway Management System").grid(row = 0,column=0,columnspan=2)

    Radiobutton(master1, text="New User ",variable=v,value = 1).pack(pady=10)
    Radiobutton(master1,text="Existing User",variable=v,value=2).pack(pady=10)
    Button(master1 , text ="Submit" , fg = "black" , command=choice_introPage).pack(pady=10)


def showPassengerDetails(parent):
    clear_frame(parent)
    Label(parent , pady=5,padx = 10 , text="ID").grid(row=0,column=0)
    Label(parent , pady=5,padx = 10 , text="Name").grid(row=0,column=1)
    Label(parent , pady=5,padx = 10 , text="E-mail").grid(row=0,column=2)
    for idx, item in enumerate(usersList , start = 2):
        Label(parent , pady=5,padx = 10 , text=item.ID).grid(row=idx,column=0)
        Label(parent , pady=5,padx = 10 , text=item.name).grid(row=idx,column=1)
        Label(parent , pady=5,padx = 10 , text=item.email).grid(row=idx,column=2)
    




def adminMenu(parent , j):
    master1 = Toplevel(parent,padx=120,pady=120)
    password = j.get()
    if password != 'admin':
        messagebox.showwarning("showwarning", 'Wrong Password')
        return
    Label(master1 , text="Admin menu").grid(row=0,column=0,columnspan=2,pady=10)
    Button(master1,text="Show Passenger Details",command= lambda i = master1: showPassengerDetails(i)).grid(row=2,column=0,columnspan=2,pady=10)
    Button(master1,text="Show Train Details").grid(row=3,column=0,columnspan=2,pady=10)
    Button(master1,text="Add Train Details").grid(row=4,column=0,columnspan=2,pady=10)

def adminMode():
    master1 = Toplevel(master,padx=120,pady=120)
    Label(master1,text="Welcome to Railway Management System").grid(row = 0,column=0,columnspan=2)
    Label(master1 , text="Enter Password" ).grid(row = 2,column=0)
    cr = StringVar()
    Entry(master1,textvariable=cr).grid(row=2,column=1)
    Button(master1 ,text="Submit" ,command= lambda i = master1 , j = cr :adminMenu(i,j) ).grid(row=4,column=0,columnspan=2)

cz = IntVar()
Label(master , text="Welcome to Railway Management System").pack()
Button(master , text="Admin Mode",padx=10,pady=10,command=adminMode ).pack()
Button(master , text="User Mode",padx=10,pady=10,command=userMode).pack()
master.mainloop()

with open("users.csv",mode = 'w') as csv_file:
    writer = csv.writer(csv_file)
    for us in usersList:
        arr = []
        arr.append(str(us.ID))
        arr.append(str(us.name))
        arr.append(str(us.email))
        arr.append(str(us.username))
        arr.append(str(us.password))
        s = ':'.join(str(x) for x in us.tickets)
        s = "{" + s + "}"
        arr.append(s)
        z = ",".join(arr)
        writer.writerow(arr)
