from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label, PhotoImage
from tkinter import Tk, Label, Button, PhotoImage
from PIL import Image, ImageTk
from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from PIL import ImageTk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter as tk
import sqlite3
from tkcalendar import *
import tkinter as tk
conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="loop"
        )

        # Create a cursor object
cursor = conn.cursor()

        # Create the college database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS college")

        # Switch to the college database
cursor.execute("USE college")

        # Create the student_pro table
cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_pro (
                std_id INT(30),
                std_name VARCHAR(50),
                class VARCHAR(50),
                division VARCHAR(20),
                dob DATE,
                roll_no VARCHAR(20),
                gender VARCHAR(20)
            )
        """)
        # Create the fee_detail table
cursor.execute("""
            CREATE TABLE IF NOT EXISTS fee_detail (
                std_id INT(30),
                std_name VARCHAR(50),
                gender VARCHAR(40),
                class VARCHAR(50),
                total_fee INT(60),
                fee_paid INT(30),
                pending_fee INT(30)
            )
        """)
cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_transactions (
                student_id INT(11) NOT NULL PRIMARY KEY,
                student_name VARCHAR(225),
                transaction_id INT(11),
                transaction_date DATE,
                amount DECIMAL(10, 2),
                payment_mode VARCHAR(50),
                phone_number VARCHAR(15)
            )
        """)


        # Commit changes
conn.commit()

        # Close connection
conn.close()



def open_payment():
    new_window = tk.Toplevel(window)
    new_window.title("payment window")
    #g = Label(new_window
    g = Label(new_window,text="QR Code",fg="black",bg="light green",font=('Georgia',18,'bold'),width=100)
    g.pack()
    image_0=Image.open(r"C:\Users\rohit\OneDrive\Pictures\og QR code.png")
    bck_end=ImageTk.PhotoImage(image_0)
    lbl=Label(new_window,image=bck_end)
    lbl.place(x=500,y=150)
    new_window.mainloop()
def student_profile ():
    new_window1 = tk.Toplevel(window)
    new_window1.title("student profile")
    def execute_query(query, data=None):
        mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
        mycursor = mydb.cursor()
        try:
            if data:
                mycursor.execute(query, data)
            else:
                mycursor.execute(query)
            mydb.commit()
        except Exception as e:
            print(f"Error: {e}")
            mydb.rollback()
        finally:
            mydb.close()
    #new_window1.mainloop()
    def on_insert_click():
        global a1, b1, c1, d1, e1, f1, g1
        a = a1.get()
        b = b1.get()
        c = c1.get()
        d = d1.get()
        e = e1.get()
        f = f1.get()
        g = g1.get()

        if a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "":
            messagebox.showinfo("Insert status", "All Fields are required",parent = new_window1)
        else:
            query = "INSERT INTO student_pro VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (a, b, c, d, e, f, g)
            execute_query(query, data)

            # Clear entry fields
            for entry in [a1, b1, c1, d1, e1, f1, g1]:
                entry.delete(0, 'end')

            messagebox.showinfo("Insert status", "Inserted Successfully",parent = new_window1)

    def on_delete_click():
        global a1, b1, c1, d1, e1, f1, g1
        if a1.get() == "":
            messagebox.showinfo("Delete status", "Id is compulsory for delete",parent = new_window1)
        else:
            query = "DELETE FROM student_pro WHERE std_id = %s"
            data = (a1.get(),)
            execute_query(query, data)

            # Clear entry fields
            for entry in [a1, b1, c1, d1, e1, f1, g1]:
                entry.delete(0, 'end')

            messagebox.showinfo("Delete status", "Deleted Successfully",parent = new_window1)


    def search_stdid():
        if(a1.get() == "" ):
            messagebox.showinfo("search status","student Id is compulsory for search",parent = new_window1)
        else:
            mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
            mycursor = mydb.cursor()
            a = a1.get()
            mycursor.execute("SELECT * FROM student_pro WHERE std_id = %s", (a,))
            rows = mycursor.fetchall()
            if len(rows) != 0:
                    # Display the first row's data in the respective Entry widgets
                    data = rows[0]
                    b1.delete(0, 'end')
                    b1.insert(0, data[1])  # Assuming std_name is in the second column
                    c1.delete(0, 'end')
                    c1.insert(0, data[2])  # Assuming class is in the third column
                    d1.delete(0, 'end')
                    d1.insert(0, data[3])  # Assuming div is in the fourth column
                    e1.delete(0, 'end')
                    e1.insert(0, data[4])  # Assuming dob is in the fifth column
                    f1.delete(0, 'end')
                    f1.insert(0, data[5])  # Assuming roll_no is in the sixth column
                    g1.delete(0, 'end')
                    g1.insert(0, data[6])  # Assuming gender is in the seventh column

                    messagebox.showinfo("Search status", "Search successful",parent = new_window1)
            else:
                    messagebox.showinfo("Search status", "No data found for the given student ID",parent = new_window1)

                    mydb.commit()
    def pick_date_mfg(event=None):
        global cal_mfg, date_window_mfg
        date_window_mfg = Toplevel()
        date_window_mfg.grab_set()
        date_window_mfg.title('choose manufacturing date')
        date_window_mfg.geometry('250x220+590+370')
        cal_mfg = Calendar(date_window_mfg, selectmode="day" , date_pattern="y/mm/dd")
        cal_mfg.place(x=0, y=0)
        submit_btn=Button(date_window_mfg, text="submit", command=grab_date_mfg)
        submit_btn.place(x=80, y=190)

    def grab_date_mfg():
        global cal_mfg, date_window_mfg
        e1.delete(0, END)
        e1.insert(0, cal_mfg.get_date())
    
        date_window_mfg.destroy()
    text_label=tk.Label(new_window1,text="Student Profile",fg="black",bg="light green",font=('Georgia',24,'bold'),width=60)
    text_label.place(x=0,y=0)
    global a1, b1, c1, d1, e1, f1, g1
    
    a = Label(new_window1,text="Student roll no:",font=('Georgia',18,'bold'))
    a.place(x=500,y=120)
    b = Label(new_window1,text ="Name Of Student:",font=('Georgia',18,'bold'))
    b.place(x=500,y=160)
    c = Label(new_window1,text="Class:",font=('Georgia',18,'bold'))
    c.place(x=500,y=210)
    d = Label(new_window1 ,text = "Division :",font=('Georgia',18,'bold'))
    d.place(x=500,y=260)
    e = Label(new_window1 ,text = "Date Of Birth:",font=('Georgia',18,'bold'))
    e.place(x=500,y=310)
    f = Label(new_window1,text = "phone no: ",font=('Georgia',18,'bold'))
    f.place(x=500,y=360)
    g = Label(new_window1 ,text = "Gender:",font=('Georgia',18,'bold'))
    g.place(x=500,y=410)
    a1 = Entry(new_window1)
    a1.place(x=800,y=120)
    b1 = Entry(new_window1)
    b1.place(x=800,y=160)
    c1 = Entry(new_window1)
    c1.place(x=800,y=210)
    options = ['1', '2','3','4','5','6','7','8','9','10']
    c1 = ttk.Combobox(new_window1, values=options, font=('Georgia',8))
    c1.place(x=800,y=210)
    c1.set(options[0])
    d1 = Entry(new_window1)
    d1.place(x=800,y=260)
    options = ['A', 'B','C','D']
    d1 = ttk.Combobox(new_window1, values=options, font=('Georgia',8))
    d1.place(x=800,y=260)
    d1.set(options[0])
    e1 = Entry(new_window1)
    e1.place(x=800,y=310)
    e1.insert(0,'yyyy/mm/dd')
    e1.bind("<FocusIn>", pick_date_mfg)
    date_button_mfg = Button(new_window1, text="Pick Date", command=pick_date_mfg)
    date_button_mfg.place(x=1000, y=310)
    f1 = Entry(new_window1 )
    f1.place(x=800,y=360)
    g1 = Entry(new_window1 )
    g1.place(x=800,y=410)
    options = ['male', 'female']
    g1 = ttk.Combobox(new_window1, values=options, font=('Georgia',8))
    g1.place(x=800,y=410)
    g1.set(options[0])

    insert = Button(new_window1 , text="Insert", font=('Georgia',18,'bold'),bg='light green',command=on_insert_click)
    insert.place(x=500,y=500)

    delete = Button(new_window1 , text="Delete",font=('Georgia',18,'bold'),bg='light green', command=on_delete_click)
    delete.place(x=700,y=500)

    search = Button(new_window1, text="Search", font=('Georgia',18,'bold'),bg='light green',command=search_stdid)
    search.place(x=900,y=500)
    new_window1.mainloop()
def open_fee_details():
    new_window2 = tk.Toplevel(window)
    new_window2.title("student profile")
    def execute_query(query, data=None):
        mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
        mycursor = mydb.cursor()
        try:
            if data:
                mycursor.execute(query, data)
            else:
                mycursor.execute(query)
            mydb.commit()
        except Exception as e:
            print(f"Error: {e}")
            mydb.rollback()
        finally:
            mydb.close()
    def on_insert_fee_details():
        #global h1, i1, j1, k1, l1, m1, n1
        h = h1.get()
        i = i1.get()
        j = j1.get()
        k = k1.get()
        l = l1.get()
        m = m1.get()
        n = n1.get()

        if h == "" or i == "" or j == "" or k == "" or l == "" or m == "" or n == "":
            messagebox.showinfo("Insert status", "All Fields are required",parent = new_window2)
        else:
            query = "INSERT INTO fee_detail VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (h, i, j, k, l, m, n)
            execute_query(query, data)

            # Clear entry fields
            for entry in [h1, i1, j1, k1, l1, m1, n1]:
                entry.delete(0, 'end')

            messagebox.showinfo("Insert status", "Inserted Successfully",parent = new_window2)
    
    def update_on_click():
     h = h1.get();
     i = i1.get();
     j = j1.get();
     k = k1.get();
     l = l1.get();
     m = m1.get();
     n = n1.get();
    
     if(h=="" or i=="" or j=="" or k=="" or l=="" or m=="" or n==""):
        messagebox.showinfo("update status","All Fields are required",parent = new_window2)
     else:
        mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
        mycursor = mydb.cursor()
        mycursor.execute("update fee_detail set std_name='"+ i +"', gender='"+ j +"', class='"+ k +"', total_Fee='"+ l +"', fee_Paid='"+ m +"', pending_Fee='"+ n +"' where std_id='"+ h +"'")
        mycursor.execute("commit");
        
        h1.delete(0, 'end')
        i1.delete(0, 'end')
        j1.delete(0, 'end')
        k1.delete(0, 'end')
        l1.delete(0, 'end')
        m1.delete(0, 'end')
        n1.delete(0, 'end')
        messagebox.showinfo("update status","update Succesfully",parent = new_window2);
        mydb.close();
    
    
        
    text_label=tk.Label(new_window2,text="Fee Details",fg="black",bg="light green",font=('Georgia',24,'bold'),width=60)
    text_label.place(x=0,y=0)
    h = Label(new_window2,text="Student roll no:",font=('Georgia',18,'bold'))
    h.place(x=500,y=120)
    i = Label(new_window2,text = "Student Name:",font=('Georgia',18,'bold'))
    i.place(x=500,y=160)
    j = Label(new_window2,text="Gender:",font=('Georgia',18,'bold'))
    j.place(x=500,y=210)
    k = Label(new_window2 ,text = "Class:",font=('Georgia',18,'bold'))
    k.place(x=500,y=260)
    l = Label(new_window2 ,text = "Total Fees:",font=('Georgia',18,'bold'))
    l.place(x=500,y=310)
    m = Label(new_window2 ,text = "Fees Paid:",font=('Georgia',18,'bold'))
    m.place(x=500,y=360)
    n = Label(new_window2 ,text = "Pending Fees:",font=('Georgia',18,'bold'))
    n.place(x=500,y=410)
    h1 = Entry(new_window2)
    h1.place(x=800,y=120)
    i1 = Entry(new_window2 )
    i1.place(x=800,y=160)
    j1 = Entry(new_window2)
    j1.place(x=800,y=210)
    options = ['male', 'female']
    j1 = ttk.Combobox(new_window2, values=options, font=('Georgia',8))
    j1.place(x=800,y=210)
    j1.set(options[0])
    k1 = Entry(new_window2 )
    k1.place(x=800,y=260)
    options = ['1', '2','3','4','5','6','7','8','9','10']
    k1 = ttk.Combobox(new_window2, values=options, font=('Georgia',8))
    k1.place(x=800,y=260)
    k1.set(options[0])
    l1 = Entry(new_window2)
    l1.place(x=800,y=310)
    m1 = Entry(new_window2 )
    m1.place(x=800,y=360)
    n1 = Entry(new_window2 )
    n1.place(x=800,y=410)

    insert = Button(new_window2 , text="Insert", font=('Georgia',18,'bold'),fg="black",bg="light green",command=on_insert_fee_details)
    insert.place(x=500,y=500)

    #delete = Button(new_window2 , text="Delete",font=('Georgia',18,'bold'),fg="black",bg="light green")#, command=on_delete_click)
    #delete.place(x=700,y=500)
    
    update = Button(new_window2 , text="Update", font=('Georgia',18,'bold'),fg="black",bg="light green", command=update_on_click)
    update.place(x=700,y=500)
def open_transaction():
    new_window3 = tk.Toplevel(window)
    new_window3.title("Transaction details")
    def execute_query(query, data=None):
        mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
        mycursor = mydb.cursor()
        try:
            if data:
                mycursor.execute(query, data)
            else:
                mycursor.execute(query)
            mydb.commit()
        except Exception as e:
            print(f"Error: {e}")
            mydb.rollback()
        finally:
            mydb.close()
    def on_insert_transac():
        
        #global h1, i1, j1, k1, l1, m1, n1
        o = o1.get()
        p = p1.get()
        q = q1.get()
        r = r1.get()
        s = s1.get()
        t = t1.get()
        u = u1.get()

        if o == "" or p == "" or q == "" or r == "" or s == "" or t == "" or u == "":
            messagebox.showinfo("Insert status", "All Fields are required",parent = new_window3)
        else:
            query = "INSERT INTO student_transactions VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (o, p, q, r, s, t, u)
            execute_query(query, data)

            # Clear entry fields
            for entry in [o1, p1, q1, r1, s1, t1, u1]:
                entry.delete(0, 'end')
            messagebox.showinfo("Insert status", "Inserted Successfully",parent = new_window3)
    def search_transac():
        if(o1.get() == "" ):
            messagebox.showinfo("search status","student Id is compulsory for search",parent = new_window3)
        else:
            mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
            mycursor = mydb.cursor()
            o = o1.get()
            mycursor.execute("SELECT * FROM student_transactions WHERE student_id = %s", (o,))
            rows = mycursor.fetchall()
            if len(rows) != 0:
                # Display the first row's data in the respective Entry widgets
                    data = rows[0]
                    p1.delete(0, 'end')
                    p1.insert(0, data[1])  # Assuming std_name is in the second column
                    q1.delete(0, 'end')
                    q1.insert(0, data[2])  # Assuming class is in the third column
                    r1.delete(0, 'end')
                    r1.insert(0, data[3])  # Assuming div is in the fourth column
                    s1.delete(0, 'end')
                    s1.insert(0, data[4])  # Assuming dob is in the fifth column
                    t1.delete(0, 'end')
                    t1.insert(0, data[5])  # Assuming roll_no is in the sixth column
                    u1.delete(0, 'end')
                    u1.insert(0, data[6])  # Assuming gender is in the seventh column

                    messagebox.showinfo("Search status", "Search successful",parent = new_window3)
            else:
                    messagebox.showinfo("Search status", "No data found for the given student ID",parent = new_window3)

                    mydb.commit()
    def pick_date_mfg(event=None):
        global cal_mfg, date_window_mfg
        date_window_mfg = Toplevel()
        date_window_mfg.grab_set()
        date_window_mfg.title('choose manufacturing date')
        date_window_mfg.geometry('250x220+590+370')
        cal_mfg = Calendar(date_window_mfg, selectmode="day" , date_pattern="y/mm/dd")
        cal_mfg.place(x=0, y=0)
        submit_btn=Button(date_window_mfg, text="submit", command=grab_date_mfg)
        submit_btn.place(x=80, y=190)

    def grab_date_mfg():
        global cal_mfg, date_window_mfg
        r1.delete(0, END)
        r1.insert(0, cal_mfg.get_date())
    
        date_window_mfg.destroy()
    text_label=tk.Label(new_window3,text="Transaction Details",fg="black",bg="light green",font=('Georgia',24,'bold'),width=65)
    text_label.place(x=0,y=0)
    o = Label(new_window3,text="Student Roll no:",font=('Georgia',18,'bold'))
    o.place(x=500,y=120)
    p = Label(new_window3,text = "Student Name:",font=('Georgia',18,'bold'))
    p.place(x=500,y=160)
    q = Label(new_window3,text="Transaction id:",font=('Georgia',18,'bold'))
    q.place(x=500,y=210)
    r = Label(new_window3 ,text = "Date:",font=('Georgia',18,'bold'))
    r.place(x=500,y=260)
    s= Label(new_window3 ,text = "Amount:",font=('Georgia',18,'bold'))
    s.place(x=500,y=310)
    t = Label(new_window3 ,text = "Payment Mode:",font=('Georgia',18,'bold'))
    t.place(x=500,y=360)
    u = Label(new_window3,text = "Phone No:",font=('Georgia',18,'bold'))
    u.place(x=500,y=410)
    o1 = Entry(new_window3 )
    o1.place(x=800,y=120)
    p1 = Entry(new_window3)
    p1.place(x=800,y=160)
    q1 = Entry(new_window3)
    q1.place(x=800,y=210)
    r1 = Entry(new_window3 )
    r1.place(x=800,y=260)
    r1.insert(0,'yyyy/mm/dd')
    r1.bind("<FocusIn>", pick_date_mfg)
    date_button_mfg = Button(new_window3, text="Pick Date", command=pick_date_mfg)
    date_button_mfg.place(x=1000, y=260)
    s1 = Entry(new_window3)
    s1.place(x=800,y=310)
    t1 = Entry(new_window3 )
    t1.place(x=800,y=360)
    options = ['Gpay', 'Phonepay','cash']
    t1 = ttk.Combobox(new_window3, values=options, font=('Georgia',8))
    t1.place(x=800,y=360)
    t1.set(options[0])
    u1 = Entry(new_window3 )
    u1.place(x=800,y=410)
    insert = Button(new_window3 , text="Insert", font=('Georgia',18,'bold'),bg='light green',command=on_insert_transac)
    insert.place(x=500,y=500)

    #delete = Button(new_window3 , text="Delete",font=('Georgia',18,'bold'),bg='light green')#, command=on_delete_tran)
    #delete.place(x=900,y=500)

    search = Button(new_window3 , text="Search", font=('Georgia',18,'bold'),bg='light green',command=search_transac)
    search.place(x=700,y=500)
def search_here():
    new_window4 = tk.Toplevel(window)
    new_window4.title("search here")
    def search_rollno():
        if(i1.get() == "" ):
            messagebox.showinfo("search status","Roll Number is compulsory for search",parent = new_window4)
        else:
            mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
            mycursor = mydb.cursor()
            i = i1.get()
            mycursor.execute("SELECT * FROM fee_detail WHERE std_id = %s", (i,))
            #mycursor.execute("SELECT * FROM pharmaco WHERE company = ?")
            rows = mycursor.fetchall()
            if len(rows) != 0:
                    # Clear existing data in the table
                    for item in rollname_table.get_children():
                        rollname_table.delete(item)
                    
                    for i in rows:
                        # Insert retrieved data into the treeview
                        rollname_table.insert("", END, values=i)
                        
                    messagebox.showinfo("Search status", "Search successful",parent = new_window4)
            else:
                    messagebox.showinfo("Search status", "No data found for the given Roll Number",parent = new_window4)
            
        mydb.commit()
        mydb.close()
    def search_class():
        if(s1.get() == "" ):
            messagebox.showinfo("search status","Roll Number is compulsory for search",parent = new_window4)
        else:
            mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
            mycursor = mydb.cursor()
            s = s1.get()
            mycursor.execute("SELECT * FROM fee_detail WHERE class = %s", (s,))
            #mycursor.execute("SELECT * FROM pharmaco WHERE company = ?")
            rows = mycursor.fetchall()
            if len(rows) != 0:
                    # Clear existing data in the table
                    for item in rollname1_table.get_children():
                        rollname1_table.delete(item)
                    
                    for i in rows:
                        # Insert retrieved data into the treeview
                        rollname1_table.insert("", END, values=i)
                        
                    messagebox.showinfo("Search status", "Search successful",parent = new_window4)
            else:
                    messagebox.showinfo("Search status", "No data found for the given Roll Number",parent = new_window4)
            
        mydb.commit()
        mydb.close()
    text_label=tk.Label(new_window4,text="Search Here",fg="black",bg="light green",font=('Georgia',24,'bold'),width=100)
    text_label.pack()
    Framedeatils=Frame(new_window4,bd=15,relief=RIDGE)
    Framedeatils.place(x=2,y=100,width=1360,height=300)
    i = Label(new_window4 ,text = "Roll NO:",font=('Georgia',12))
    i.place(x=600,y=50)
    i1 = Entry(new_window4)
    i1.place(x=700,y=50)
    search = Button(new_window4, text="search by roll no", font=("Georgia", 12), bg="powder blue",command = search_rollno)
    search.place(x=900,y=50)
    sc_x=ttk.Scrollbar(Framedeatils,orient=HORIZONTAL)
    sc_x.pack(side=BOTTOM,fill=X)
    rollname_table=ttk.Treeview(Framedeatils,column=("student Roll no","student name","Gender","Class","Total Fees","Fees Paid","Pending Fees","uses"),xscrollcommand=sc_x.set)
    sc_x.config(command=rollname_table.xview)
    #medname table
    rollname_table.heading("student Roll no",text="student Roll no")
    rollname_table.heading("student name",text="student name")
    rollname_table.heading("Gender",text="Gender")
    rollname_table.heading("Class",text="class")
    rollname_table.heading("Total Fees",text="Total fees")
    rollname_table.heading("Fees Paid",text="Fees Paid")
    
    rollname_table.heading("Pending Fees",text="Pending fees")
    
    rollname_table["show"]="headings"
    rollname_table.pack(fill=BOTH,expand=1)
    rollname_table.column("student Roll no",width=170)
    rollname_table.column("student name",width=280)
    rollname_table.column("Gender",width=170)
    rollname_table.column("Class",width=170)
    rollname_table.column("Total Fees",width=170)
    rollname_table.column("Fees Paid",width=170)
    rollname_table.column("Pending Fees",width=170)
    
    s = Label(new_window4 ,text = "Class:",font=('Georgia',12))
    s.place(x=550,y=410)
    s1 = Entry(new_window4)
    s1.place(x=600,y=410)
    searchclass = Button(new_window4, text="search by class", font=("Georgia", 12), bg="powder blue", command = search_class )
    searchclass.place(x=750,y=410)
    Frame1=Frame(new_window4,bd=15,relief=RIDGE)
    Frame1.place(x=2,y=450,width=1360,height=250)
    sc_x=ttk.Scrollbar(Frame1,orient=HORIZONTAL)
    sc_x.pack(side=BOTTOM,fill=X)
    rollname1_table=ttk.Treeview(Frame1,column=("student Roll no","student name","Gender","Class","Total Fees","Fees Paid","Pending Fees","uses"),xscrollcommand=sc_x.set)
    sc_x.config(command=rollname1_table.xview)
    sc_y=ttk.Scrollbar(Frame1,orient=VERTICAL)
    sc_y.pack(side=RIGHT,fill=Y)
    rollname1_table.heading("student Roll no",text="student Roll no")
    rollname1_table.heading("student name",text="student name")
    rollname1_table.heading("Gender",text="Gender")
    rollname1_table.heading("Class",text="class")
    rollname1_table.heading("Total Fees",text="Total fees")
    rollname1_table.heading("Fees Paid",text="Fees Paid")
    
    rollname1_table.heading("Pending Fees",text="Pending fees")
    
    rollname1_table["show"]="headings"
    rollname1_table.pack(fill=BOTH,expand=1)
    rollname1_table.column("student Roll no",width=170)
    rollname1_table.column("student name",width=280)
    rollname1_table.column("Gender",width=170)
    rollname1_table.column("Class",width=170)
    rollname1_table.column("Total Fees",width=170)
    rollname1_table.column("Fees Paid",width=170)
    rollname1_table.column("Pending Fees",width=170)
    

window = Tk()
window.title("Fee Management")
window.geometry('600x600')
Frameone=Frame(window,bd=15,relief=RIDGE)
Frameone.place(x=500,y=50,width=860,height=650)
text_label=tk.Label(Frameone,text="WELCOME",fg="black",bg="light green",font=('Georgia',24,'bold'),width=40)
text_label.pack()
text_label=tk.Label(Frameone,text="fees structure",fg="black",font=('Georgia',24,'bold'),width=40)
text_label.pack()
#from PIL import Image, ImageTk, ImageFilter
#import tkinter as tk

# Assuming Frameone is already defined

# Open the image

# Assuming the rest of your tkinter setup follows
image_0=Image.open(r"C:\Users\rohit\OneDrive\Pictures\fee structure.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(Frameone,image=bck_end)
lbl.place(x=300,y=150)

text_label=tk.Label(window,text="fee management",fg="black",bg="light green",font=('Georgia',24,'bold'),width=100)
text_label.pack()
Framedeatils=Frame(window,bd=15,relief=RIDGE)
Framedeatils.place(x=2,y=50,width=500,height=650)
text_label=tk.Label(Framedeatils,text="MENU",fg="black",bg="light green",font=('Georgia',24,'bold'),width=100)
text_label.pack()
student_details = Button(Framedeatils, text="STUDENT PROFILE", height=2, width=30,bg= "powder blue",font=('Georgia',12,'bold'), command = student_profile)
student_details .place(x=40,y=90)

fee_details = Button(Framedeatils, text="FEE DETAILS", height=2, width=30,bg= "powder blue",font=('Georgia',12,'bold'), command = open_fee_details)
fee_details .place(x=40,y=180)

payment = Button(Framedeatils, text="PAY HERE", height=2, width=30,bg= "powder blue",font=('Georgia',12,'bold'), command = open_payment)
payment .place(x=40,y=270)

transac = Button(Framedeatils, text="TRANSACTION DETAILS", height=2, bg= "powder blue",width=30,font=('Georgia',12,'bold'), command = open_transaction)
transac .place(x=40,y=360)

reciept = Button(Framedeatils, text="SEARCH HERE", height=2, bg= "powder blue",width=30,font=('Georgia',12,'bold'), command = search_here)
reciept .place(x=40,y=470)


window.mainloop()
