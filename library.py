from tkinter import*
from tkinter import ttk
import mysql.connector
import tkinter
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        # =================================variable==================================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finalprice=StringVar()
        
        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)  
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
        
        # =====================================DataFrameLeft============================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=860,height=350)
        
        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)
        
        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN NO:",font=("arial",12,"bold"),padx=2)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)
        
        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID NO:",font=("arial",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txlFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txlFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txlLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txlLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txlAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txlAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txlAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txlAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post Code",font=("arial",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txlPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txlPostCode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile No.",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txlMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txlMobile.grid(row=8,column=1)
        
        lblBookId=Label(DataFrameLeft,bg="powder blue",text="Book Id:",font=("arial",12,"bold"),padx=2)
        lblBookId.grid(row=0,column=2,sticky=W)
        txlBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
        txlBookId.grid(row=0,column=3)
        
        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txlBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        txlBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txlAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.author_var,width=29)
        txlAuthor.grid(row=2,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txlDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txlDateBorrowed.grid(row=3,column=3)
        
        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="Date Due:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txlDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        txlDateDue.grid(row=4,column=3)
        
        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days on Book:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txlDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook,width=29)
        txlDaysOnBook.grid(row=5,column=3)
        
        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("arial",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txlLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.latereturnfine_var,width=29)
        txlLateReturnFine.grid(row=6,column=3)
        
        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txlDateOverDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue,width=29)
        txlDateOverDue.grid(row=7,column=3)
        
        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",font=("arial",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txlActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finalprice,width=29)
        txlActualPrice.grid(row=8,column=3)
        
        # =====================================DataFrameRight========================================================
        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=870,y=5,width=580,height=350)
        
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Data Structure & Algorithm','OOPS with C++','DBMS','Web Designing','Machine Learning','Aritificial Intelligence',
                            'Beginner Python','Advance Python','OOPS with Python','My Sql','C Programming','Software Engineering',
                            'Hacking','Think Python','Core Python','Fluent Python','System Design','Tree and Graph','Mathematics' ]
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="Data Structure & Algorithm"):
                self.bookid_var.set("BKID2093")
                self.booktitle_var.set("Logic Building")
                self.author_var.set("Paul Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("499")
                
            elif(x=="OOPS with C++"):
                self.bookid_var.set("BKID5463")
                self.booktitle_var.set("Object Oriented")
                self.author_var.set("Bjarne Stroustrup")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("399")
                
            elif(x=="DBMS"):
                self.bookid_var.set("BKID1234")
                self.booktitle_var.set("Database Management")
                self.author_var.set("Johannes Gehrke")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("299")
                
            elif(x=="Web Designing"):
                self.bookid_var.set("BKID9766")
                self.booktitle_var.set("Website Design")
                self.author_var.set("Bella Andre")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("499")
                
            elif(x=="Machine Learning"):
                self.bookid_var.set("BKID5738")
                self.booktitle_var.set("Machine Python")
                self.author_var.set("Andriy Burkov")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("699")
                
            elif(x=="Aritificial Intelligence"):
                self.bookid_var.set("BKID9765")
                self.booktitle_var.set("AI Python")
                self.author_var.set("Peter Norvig")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("899")
            elif(x=="Beginner Python"):
                self.bookid_var.set("BKID9348")
                self.booktitle_var.set("PYthon Programming")
                self.author_var.set("Guido van Rossum")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("599")
            elif(x=="Advance Python"):
                self.bookid_var.set("BKID3203")
                self.booktitle_var.set("Logical Python")
                self.author_var.set("Guido van Rossum")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("799")
            elif(x=="OOPS with Python"):
                self.bookid_var.set("BKID3839")
                self.booktitle_var.set("OOPS with Python")
                self.author_var.set("Irv Kalb")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("1199")
                
            elif(x=="My Sql"):
                self.bookid_var.set("BKID0784")
                self.booktitle_var.set("My Sql")
                self.author_var.set("Alan Beaulieu")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("599")
                
            elif(x=="C Programming"):
                self.bookid_var.set("BKID9478")
                self.booktitle_var.set("C Programming")
                self.author_var.set("Dennis Ritchie")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("699")
                
            elif(x=="Software Engineering"):
                self.bookid_var.set("BKID0353")
                self.booktitle_var.set("Software Engineering")
                self.author_var.set("Sushil Goyal")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("299")
                
            elif(x=="Hacking"):
                self.bookid_var.set("BKID3824")
                self.booktitle_var.set("Hacking")
                self.author_var.set("Ankit Fadia")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("2099")
                
            elif(x=="Think Python"):
                self.bookid_var.set("BKID6564")
                self.booktitle_var.set("Think Python")
                self.author_var.set("Suman Wadhwa")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("599")
                
            elif(x=="Core Python"):
                self.bookid_var.set("BKID2943")
                self.booktitle_var.set("Core Python")
                self.author_var.set("Sushil Goyal")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("899")
                
            elif(x=="Fluent Python"):
                self.bookid_var.set("BKID0967")
                self.booktitle_var.set("Fluent Python")
                self.author_var.set("Luciano Ramalho")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("2599")
                
            elif(x=="System Design"):
                self.bookid_var.set("BKID6346")
                self.booktitle_var.set("System Design")
                self.author_var.set("Suman Wadhwa")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("599")
                
            elif(x=="Tree and Graph"):
                self.bookid_var.set("BKID6743")
                self.booktitle_var.set("Tree and Graph")
                self.author_var.set("Seymour Lipstouz")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("599")
                
            elif(x=="Mathematics"):
                self.bookid_var.set("BKID2938")
                self.booktitle_var.set("Mathematics")
                self.author_var.set("RD Sharma")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue.set("NO")
                self.finalprice.set("699")

        
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)
        
        # =======================================buttons frame=======================================================

        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=0,y=530,width=1530,height=60)
        
        btnAddData=Button(framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        btnAddData=Button(framebutton,command=self.show_data,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)
        btnAddData=Button(framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)
        btnAddData=Button(framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)
        btnAddData=Button(framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)
        btnAddData=Button(framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        
        # =======================================Information frame=======================================================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="Powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1",
                                                "address2","postid","mobile","bookid","booktitle","author","dateborrowed",
                                                "datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="382002",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdue.get(),
                                                                                                                self.finalprice.get()                                                                  
                                                                                                                 ))
        conn.commit()
        self.fatch_data()
        conn.close()
        
        messagebox.showinfo("Success","Member has been inserted successfully")
        
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="382002",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,BookId=%s,Mobile=%s,BookTitle=%s,Author=%s,Dateborrowed=%s,Datedue=%s,DaysonBook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where PRN_NO=%s",(
                                                                                                                self.member_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdue.get(),
                                                                                                                self.finalprice.get(),
                                                                                                                self.prn_var.get()
                                                                                                ))                                                                                        
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        
        messagebox.showinfo("Success","Member has been updated")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="382002",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
    
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()    
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finalprice.set(row[17]),
    
    def show_data(self):
        self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN NO:\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID NO:\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"First Name\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Last Name\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code\t\t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No.\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t\t"+self.author_var.get()+"\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"DateDue:\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+self.daysonbook.get()+"\n")
        self.txtBox.insert(END,"LateReturnFine:\t\t"+self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+self.dateoverdue.get()+"\n")
        self.txtBox.insert(END,"ActualPrice:\t\t"+self.finalprice.get()+"\n")
        
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue.set(""),
        self.finalprice.set("") 
        self.txtBox.delete("1.0",END)
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="382002",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success","Member has been Deleted")   
        
        
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
    
        

                
        
        
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()