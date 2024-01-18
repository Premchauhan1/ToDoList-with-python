from tkinter import *

#to add item into the list
def addItem():
    item = listEntry.get()
    task_listbox.insert("end", item)
    listEntry.delete(0, END) #clear the Entry box

#to delete item from list
def deleteItem():
    item = listEntry.get()
    index = task_listbox.get(0, END).index(item)
    task_listbox.delete(index)
    listEntry.delete(0, END)

#to delete all items
def deleteAll():
    task_listbox.delete(0, END)

#to close the window
def close():
    window.destroy()


if __name__ == '__main__':
    window = Tk()

    window.geometry("850x780")
    window.title("To Do List")
    window.config(bg="#638889")

    heading = Label(text="To Do List", font=("Impact", 50), bg="#638889")
    heading.pack()

    task_listbox = Listbox(
        width=30,
        height=15,
        font=(20),
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#CD853F",
        selectforeground="#FFFFFF"
    )
    task_listbox.pack(padx=10, pady=10) #represent the to do list

    enter = Label(text="Enter the To Do Item", font=(20), bg="#638889")
    enter.pack()

    listEntry = Entry(width=30, font=("Consolas", "20")) #enter to-do item
    listEntry.pack(pady=10)

    addButton = Button(text="Add to List", font=(10), width=25, bg="#7E6363", command=addItem) #to add to-do item into list
    addButton.pack(pady=5)

    deleteButton = Button(text="Delete Item", font=(10), bg="#7E6363", width=25, command=deleteItem)#to remove to-do item from list
    deleteButton.pack(pady=5)

    deleteAllButton = Button(text="Delete All Items", font=(10), bg="#7E6363", width=25, command=deleteAll)#to remove all to-do items from list
    deleteAllButton.pack(pady=5)

    exitButton = Button(text="Exit", font=(10), width=25, bg="#D24545", command=close)
    exitButton.pack()


    window.mainloop()

