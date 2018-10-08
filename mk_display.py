from tkinter import *
from tkinter import ttk
import csv

def mk_display(stock_no_file):


    def show_selection():
        global kisyu,select_list,kikan,MySQLparam
        kisyu=[]
        select_list=[]
        if Val1.get() == True:
            kisyu.append("m")
        if Val2.get() == True:
            kisyu.append("w")
        if Val3.get() == True:
            kisyu.append("d")

        for i in lb.curselection():
            select_list.append(lb.get(i))

        kikan=[str(EditBox1.get()),str(EditBox2.get())]
        MySQLparam=[EditBox3.get(),EditBox4.get(),EditBox5.get(),EditBox6.get()]

        if len(select_list)!=0:
            print("選択銘柄 : \n" , select_list)
        root.destroy()

    root = Tk()
    root.title('Scrollbar')
    root.geometry("1000x700")

    # Frame1
    frame1 = ttk.Frame(root, padding=1)
    frame1.grid(column=0, row=0, sticky=(N, S, E, W))
    
    #Label1
    label = Label(frame1,text="【期間】",font=("",10),height=2).grid(column=0, row=0, sticky="w")

    #CheckBox
    Val1 = BooleanVar()
    Val2 = BooleanVar()
    Val3 = BooleanVar()

    Val1.set(True)
    Val2.set(False)
    Val3.set(False)

    CheckBox1 = ttk.Checkbutton(frame1,text="月次",variable=Val1).grid(column=0, row=1)

    CheckBox2 = ttk.Checkbutton(frame1,text="週次",variable=Val2).grid(column=1, row=1)

    CheckBox3 = ttk.Checkbutton(frame1,text="日次",variable=Val3).grid(column=2, row=1)

    # Frame2
    frame2 = ttk.Frame(root, padding=1)
    frame2.grid(column=0, row=1, sticky=(N, S, E, W))

    #エントリー1
    Label1=Label(frame2,text="開始年").grid(column=0, row=0, sticky="w")
    EditBox1 = Entry(frame2)
    EditBox1.insert(END,"2000")
    EditBox1.grid(column=0, row=1)

    #エントリー2
    Label2=Label(frame2,text="終了年").grid(column=1, row=0, sticky="w")
    EditBox2 = Entry(frame2)
    EditBox2.insert(END,"2018")
    EditBox2.grid(column=1, row=1)

    # Frame3
    frame3 = ttk.Frame(root, padding=1)
    frame3.grid(column=0, row=2, sticky=(N, S, E, W))

    #Label1
    label = Label(frame3,text="【MySQL】",font=("",10),height=2).grid(column=0, row=0, sticky="w")

    #エントリー3
    Label3=Label(frame3,text="host").grid(column=0, row=1, sticky="w")
    EditBox3 = Entry(frame3)
    EditBox3.insert(END,"127.0.0.1")
    EditBox3.grid(column=0, row=2,sticky="w")

    #エントリー4
    Label4=Label(frame3,text="port").grid(column=0, row=3, sticky="w")
    EditBox4 = Entry(frame3)
    EditBox4.insert(END,"3306")
    EditBox4.grid(column=0, row=4,sticky="w")

    #エントリー5
    Label5=Label(frame3,text="user").grid(column=0, row=5, sticky="w")
    EditBox5 = Entry(frame3)
    EditBox5.insert(END,"root")
    EditBox5.grid(column=0, row=6,sticky="w")

    #エントリー6
    Label1=Label(frame3,text="passwd").grid(column=0, row=7, sticky="w")
    EditBox6 = Entry(frame3)
    EditBox6.grid(column=0, row=8,sticky="w")

    # Frame4
    frame4 = ttk.Frame(root, padding=10)
    frame4.grid(column=0, row=3, sticky=(N, S, E, W))

    # Listbox
    lb = Listbox(frame4,selectmode=MULTIPLE,height=20,width=170)
    lb.grid(row=0, column=0)

    with open(stock_no_file,"r",encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row_list in reader:
            lb.insert(END,row_list[1] + "：" + row_list[0])

    # Scrollbar
    scrollbar = ttk.Scrollbar(frame4,orient=VERTICAL,command=lb.yview)
    lb['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=0,column=1,sticky=(N,S))

    #Button
    button1 = ttk.Button(frame4, text='OK', command=show_selection)
    button1.grid(row=1, column=0, columnspan=2)

    root.mainloop()

    param_list=[i.split("：")[1] for i in select_list]

    return MySQLparam,kisyu,kikan,param_list
