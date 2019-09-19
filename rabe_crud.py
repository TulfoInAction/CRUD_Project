from tkinter import *
from tkinter import ttk
import tkinter.messagebox

athlete = []


class Athlete:
    def __init__(self, name, sports, position, jerseynumber):
        self.name = name
        self.sports = sports
        self.position = position
        self.jerseynumber = jerseynumber

    def getName(self):
        return self.name
    def getSports(self):
        return self.sports
    def getPosition(self):
        return self.position
    def getJerseynumber(self):
        return self.jerseynumber

def addInfo():
    global athlete
    MsgBox = tkinter.messagebox.askquestion ('Confirmation','Are you sure you want to add this item?',icon = 'warning')
    if MsgBox == 'yes':
        info = Athlete(entry1.get(), entry2.get(), entry3.get(), entry4.get())
        athlete.append(info)
        tview.insert('', 'end', text='tree', values=(entry1.get(), entry2.get(), entry3.get(), entry4.get()))

        digit = (entry4.get())
        if (digit.isdigit()):
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry4.delete(0, 'end')
            return True
        else:
            error = "Wrong data type entered."
            tkinter.messagebox.showinfo("Warning", error)
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry4.delete(0, 'end')
            return False
    else:
        pass


def updateInfo():
    global athlete
    MsgBox = tkinter.messagebox.askquestion ('Confirmation','Are you sure you want to update this item?',icon = 'warning')
    if MsgBox == 'yes':
       selected_item = tview.selection()[0]
       tview.item(selected_item, values=(entry1.get(), entry2.get(), entry3.get(), entry4.get()))    

       entry1.delete(0, 'end')
       entry2.delete(0, 'end')
       entry3.delete(0, 'end')
       entry4.delete(0, 'end')
    else:
        pass

def deleteInfo():
    global Books
    MsgBox = tkinter.messagebox.askquestion ('Confirmation','Are you sure you want to delete this item?',icon = 'warning')
    if MsgBox == 'yes':
       selected_item = tview.selection()[0]
       tview.delete(selected_item)
    else:
        pass

def close():
    MsgBox = tkinter.messagebox.askquestion ('Exit Application','Are you sure you want to exit the program?',icon = 'warning')
    if MsgBox == 'yes':
       form.destroy()
    else:
        tkinter.messagebox.showinfo('Return','You will now be back on the Athletes Information')

def validateNumber(number):
    if number.isdigit():
        return True
    elif number is "":
        return True
    else:
        return False


def getSelection(event):
    global name_text
    global sports_text
    global position_text
    global jerseynumber_text

    selected_item = tview.selection()
    select = tview.item(selected_item,'values')

    name_text.set(select[0])
    sports_text.set(select[1])
    position_text.set(select[2])
    jerseynumber_text.set(select[3])




form = Tk()
form.resizable(False, False)
form.title("Athlete Information")
form.geometry("800x450")
form.config(bg="#161B21")
label = Label(form, text="Athlete's Information", font=10)
label.grid(row=0, column=1)
label.config(font=("OCR A EXTENDED", 20, "bold"), fg='#F4A950', bg="#161B21")


tview = ttk.Treeview(form, column=("Name", "Sports", "Position", "Jerseynumber"), show="headings")
tview.heading('#1', text='NAME')
tview.heading('#2', text='SPORTS')
tview.heading('#3', text='POSITION')
tview.heading('#4', text='JERSEY NUMBER')
tview.bind('<ButtonRelease-1>',getSelection)
tview.grid(row=2,column=0,columnspan=5)




label1 = Label(form, text="Name:", font="Broadway 12", fg = '#F4A950', bg="#161B21")
label1.grid(row=4, column=0)

label1 = Label(form, text="Sports:", font="Broadway 12", fg = '#F4A950', bg="#161B21")
label1.grid(row=5, column=0)

label1 = Label(form, text="Position:", font="Broadway 12", fg = '#F4A950', bg="#161B21")
label1.grid(row=6, column=0)

label1 = Label(form, text="Jersey Number:", font="Broadway 12", fg = '#F4A950', bg="#161B21")
label1.grid(row=7, column=0)

name_text=StringVar()
sports_text=StringVar()
position_text = StringVar()
jerseynumber_text = StringVar()

entry1 = Entry(form, background = '#F4F6F7', relief = RAISED, borderwidth = 5, textvariable=name_text)
entry1.grid(row=4, column=1)

entry2 = Entry(form, background = '#F4F6F7', relief = RAISED, borderwidth = 5, textvariable=sports_text)
entry2.grid(row=5, column=1)

entry3 = Entry(form, background = '#F4F6F7', relief = RAISED, borderwidth = 5, textvariable=position_text)
entry3.grid(row=6, column=1)

entry4 = Entry(form, background = '#F4F6F7', relief = RAISED, borderwidth = 5, textvariable=jerseynumber_text)
entry4.grid(row=7, column=1)


value = form.register(validateNumber)
entry4.config(validate="key",validatecommand=(value, '%P'))

button1 = Button(form, text="Add", font="Elephant 11", fg = '#161B21', bg = '#F4A950', command=addInfo, border=5)
button1.grid(row=4, column=2, padx=3, pady=3 )
button2 = Button(form, text="Update", font="Elephant 11", fg = '#161B21', bg = '#F4A950', command=updateInfo, border=5)
button2.grid(row=5, column=2, padx=3, pady=3)
button3 = Button(form, text="Delete", font="Elephant 11", fg = '#161B21', bg = '#F4A950', command=deleteInfo, border=5)
button3.grid(row=6, column=2, padx=3, pady=3)
button4 = Button(form, text="Exit", font="Elephant 11", fg = '#161B21', bg = '#F4A950', command=close, border=5)
button4.grid(row=7, column=2, padx=3, pady=3)
form.mainloop()
