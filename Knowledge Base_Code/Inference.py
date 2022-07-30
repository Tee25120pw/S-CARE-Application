from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import connect

mycursor = connect.mydb.cursor()
mycursor.execute("SELECT `fact` FROM `Fact`")
myresult = mycursor.fetchall()

def fInference():
    window = Tk()
    window.title('Rule')
    window.geometry('400x220')

    def Then():
        sql = "SELECT `then1`, `then2`, `then3`, `then4`, `then5` FROM `rule` WHERE if1 = %s AND if2 = %s AND if3 = %s AND if4 = %s AND if5 = %s"
        val1 = (f1.get())
        val2 = (f2.get())
        val3 = (f3.get())
        val4 = (f4.get())
        val5 = (f5.get())
        mycursor.execute(sql, (val1,val2,val3,val4,val5))
        myresult = mycursor.fetchall()
        if myresult == ():
            tkinter.messagebox.showinfo('Then', 'No rule/Please add rule')
            print("No rule/Please add rule")
        else:
            tkinter.messagebox.showinfo('Then',myresult)
            print(myresult)

    Label(window, text='IF').pack()

    f1=ttk.Combobox(window, values=myresult)
    f1.pack(pady=5)

    f2=ttk.Combobox(window, values=myresult)
    f2.pack(pady=5)

    f3=ttk.Combobox(window, values=myresult)
    f3.pack(pady=5)

    f4=ttk.Combobox(window, values=myresult)
    f4.pack(pady=5)

    f5=ttk.Combobox(window, values=myresult)
    f5.pack(pady=5)

    CreRule = Button(window, text='แสดงผล',command=Then)
    CreRule.pack()

    window.mainloop()