from tkinter import *
from tkinter import ttk
import connect

def fEditor():

    # ฟังก์ชันเพิ่มข้อมูล
    def addFactbtn():
        window = Tk()
        window.title('Knowledge')
        window.geometry('400x200')
        
        def insert():
            mycursor = connect.mydb.cursor()
            sql = "INSERT INTO Fact (fact) VALUES (%s)"
            val = (Afact.get())
            mycursor.execute(sql, val)
            connect.mydb.commit()

        Afact = Entry(window)
        Afact.pack()

        addF = Button(window, text='Add',command=insert)
        addF.pack()

        window.mainloop()

    # ฟังก์ชันลบข้อมูล
    def deleteFact():
        mycursor = connect.mydb.cursor()
        sql = "DELETE FROM fact WHERE fact = %s"
        val = (fact.get(ANCHOR))
        mycursor.execute(sql, val)
        connect.mydb.commit()

    # ฟังก์ชันเพิ่มกฎ
    def addRulebtn():
        window = Tk()
        window.title('Rule')
        window.geometry('400x220')

        # ฟังก์ชันสร้างกฎ
        def create():
            sql = "INSERT INTO Rule (if1,if2,if3,if4,if5,then1,then2,then3,then4,then5,rule) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val1 = (if1.get())
            val2 = (if2.get())
            val3 = (if3.get())
            val4 = (if4.get())
            val5 = (if5.get())
            val6 = (then1.get())
            val7 = (then2.get())
            val8 = (then3.get())
            val9 = (then4.get())
            val10 = (then5.get())
            if val1 != '':
                i='IF:'
            else:
                i=''
            if val2 != '':
                a='.AND:'
            else:
                a=''
            if val3 != '':
                b='.AND:'
            else:
                b=''
            if val4 != '':
                c='.AND:'
            else:
                c=''
            if val5 != '':
                d='.AND:'
            else:
                d=''
            if val7 != '':
                e='.AND:'
            else:
                e=''
            if val8 != '':
                f='.AND:'
            else:
                f=''
            if val9 != '':
                g='.AND:'
            else:
                g=''
            if val10 != '':
                h='.AND:'
            else:
                h=''
            if val6 != '':
                t='.THEN:'
            else:
                t=''
            Rule = i+val1+a+val2+b+val3+c+val4+d+val5+t+val6+e+val7+f+val8+g+val9+h+val10
            myfact.execute(sql, (val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,Rule))
            connect.mydb.commit()

        Frame0 = Frame(window)
        Frame0.pack()

        Frame1 = Frame(Frame0)
        Frame1.grid(row=0,column=0)

        Frame2 = Frame(Frame0)
        Frame2.grid(row=0,column=1)

        Label(Frame1, text='IF').pack()

        if1=ttk.Combobox(Frame1, values=myfactresult)
        if1.pack(padx=5,pady=5)

        if2=ttk.Combobox(Frame1, values=myfactresult)
        if2.pack(padx=5,pady=5)

        if3=ttk.Combobox(Frame1, values=myfactresult)
        if3.pack(padx=5,pady=5)

        if4=ttk.Combobox(Frame1, values=myfactresult)
        if4.pack(padx=5,pady=5)

        if5=ttk.Combobox(Frame1, values=myfactresult)
        if5.pack(padx=5,pady=5)

        Label(Frame2, text='THEN').pack()

        then1=ttk.Combobox(Frame2, values=myfactresult)
        then1.pack(padx=5,pady=5)

        then2=ttk.Combobox(Frame2, values=myfactresult)
        then2.pack(padx=5,pady=5)

        then3=ttk.Combobox(Frame2, values=myfactresult)
        then3.pack(padx=5,pady=5)

        then4=ttk.Combobox(Frame2, values=myfactresult)
        then4.pack(padx=5,pady=5)

        then5=ttk.Combobox(Frame2, values=myfactresult)
        then5.pack(padx=5,pady=5)

        CreRule = Button(window, text='Create Rule',command=create)
        CreRule.pack(padx=5,pady=5)

        window.mainloop()

# ฟังก์ชันลบกฎ
    def deleteRule():
        mycursor = connect.mydb.cursor()
        sql = "DELETE FROM rule WHERE rule = %s"
        val = (rule.get(ANCHOR))
        mycursor.execute(sql, val)
        rule.delete(ANCHOR)
        connect.mydb.commit()

    window = Tk()
    window.title('Knowledge Base Editor')
    window.geometry('450x300')

    Tframe = Frame(window)
    Tframe.pack(fill=BOTH, expand=True)

    Bframe = Frame(window)
    Bframe.pack(fill=BOTH, expand=True)

    frame1 = Frame(Tframe)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

    frame2 = Frame(Tframe)
    frame2.pack(expand=True)

    frame3 = Frame(Bframe)
    frame3.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

    frame4 = Frame(Bframe)
    frame4.pack(expand=True)



# DBselect
    myfact = connect.mydb.cursor()
    myfact.execute("SELECT `fact` FROM `Fact`")
    myfactresult = myfact.fetchall()

    myrule = connect.mydb.cursor()
    myrule.execute("SELECT `rule` FROM `rule`")
    myruleresult = myrule.fetchall()

# เป็นส่วนที่ดึง fact จากตารางข้อมูลมาเก็บไว้ในต้วแปล myfactresult
# เป็นส่วนที่ดึง Rule จากตารางข้อมูลมาเก็บไว้ในต้วแปล myruleresult

# ส่วนของfact
    Yfactscrollbar = Scrollbar(frame1)
    Yfactscrollbar.pack(side=RIGHT, fill=Y)

    Xfactscrollbar = Scrollbar(frame1,orient=HORIZONTAL)
    Xfactscrollbar.pack(side=BOTTOM,fill=X)

    fact = Listbox(frame1, font=16, height=5, yscrollcommand=Yfactscrollbar.set, xscrollcommand=Xfactscrollbar.set)
    for x in myfactresult:
        fact.insert(END,x)
    fact.pack(side=LEFT, fill=BOTH, expand=True)
    Yfactscrollbar.config(command=fact.yview)
    Xfactscrollbar.config(command=fact.xview)

    FFact = Label(frame2,font=20, text='Fact')
    FFact.pack(fill=X, expand=True, padx=10,pady=20)

    addF = Button(frame2, text='Add Fact',command=addFactbtn)
    addF.pack(fill=X, expand=True, padx=10)

    delF = Button(frame2, text='Delete Fact', command=deleteFact)
    delF.pack(fill=X, expand=True, padx=10)

# Yfactscrollbar สร้าง scrollbar แกนX,Y
# fact = Listbox สร้าง Listbox เพื่อให้แสดงผล fact 
# สร้างปุ่ม  Button ไว้ เพิ่ม fact และจะเรียกใช้ adfunction
# สร้างปุ่ม  Button ไว้ deleate fact และจะเรียกใช้ delfunction

# ส่วนของแสดงRule
    Yrulescrollbar = Scrollbar(frame3)
    Yrulescrollbar.pack(side=RIGHT, fill=Y)

    Xrulescrollbar = Scrollbar(frame3,orient=HORIZONTAL)
    Xrulescrollbar.pack(side=BOTTOM,fill=X)

    rule = Listbox(frame3, font=16, height=5, yscrollcommand=Yrulescrollbar.set, xscrollcommand=Xrulescrollbar.set)
    for x in myruleresult:
        rule.insert(END, x)
    rule.pack(side=LEFT, fill=BOTH, expand=True)
    Yrulescrollbar.config(command=rule.yview)
    Xrulescrollbar.config(command=rule.xview)

    RRule = Label(frame4,font=20, text='Rule')
    RRule.pack(fill=X, expand=True, padx=10,pady=20)

    addR = Button(frame4, text='Add Rule',command=addRulebtn)
    addR.pack(fill=X, expand=True, padx=10)

    delR = Button(frame4, text='Delete Rule', command=deleteRule)
    delR.pack(fill=X, expand=True, padx=10)

    window.mainloop()

# Yfactscrollbar สร้าง scrollbar แกนX,Y
# Rule = Listbox สร้าง Listbox เพื่อให้แสดงผล rule
# สร้างปุ่ม  Button ไว้ เพิ่ม rule และจะเรียกใช้ adfunction
# สร้างปุ่ม  Button ไว้ deleate rule และจะเรียกใช้ delfunction