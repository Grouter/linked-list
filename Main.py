from LinkedList import *
from tkinter import *

linkedList = LinkedList()

Tk().title("LinkedList Demo")

active_edit = -1


def insert():
    if not check_entries():
        message(0, "Cannot insert empty input")
        return
    value = get_entries()
    linkedList.add(value)
    delete_entries()
    message(1, "Inserted {0}".format(value))


def find():
    value = get_entries()
    refresh()
    if linkedList.contains(value):
        message(1, "Found {0}".format(value))
        index = linkedList.index_of(value)
        listBox.selection_set(index)
    else:
        message(1, "Not found")


def refresh():
    for i in range(len(linkedList)):
        if listBox.get(i) != parse_list(linkedList.get(i)):
            replace([i], linkedList.get(i))
        if i > listBox.size() - 1:
            listBox.insert(END, parse_list(linkedList.get(i)))
    delete_entries()
    message(1, "List refreshed with {0} input/s".format(len(linkedList)))


def remove(indexes):
    for index in reversed(indexes):
        linkedList.remove_index(index)
        listBox.delete(index)


def replace(indexes, value):
    if not check_entries():
        return
    for index in indexes:
        linkedList.set(index, value)
        listBox.insert(index, parse_list(value))
        listBox.delete(index + 1)
    delete_entries()


def edit():
    global active_edit
    if len(listBox.curselection()) > 1:
        message(0, "Cannot edit multiple inputs")
        return
    active_edit = listBox.curselection()[0]
    edited_val = linkedList.get(listBox.curselection()[0])
    delete_entries()
    for i in range(len(entries)):
        entries[i].insert(0, edited_val[i])


def apply_edit():
    global active_edit
    print(active_edit)
    if active_edit >= 0:
        linkedList.set(active_edit, get_entries())
        refresh()
    else:
        message(0, "Use Edit before Apply Edit")
    active_edit = -1


def parse_list(raw_list):
    return " ".join(raw_list)


def delete_entries():
    for e in entries:
        e.delete(0, END)


def check_entries():
    for e in entries:
        if e.get() == "":
            return False
    return True


def get_entries():
    return [e.get() for e in entries]


def message(msg_type, text):
    tp = {0: "red", 1: "green"}
    info_text.config(text=text, bg=tp[msg_type])


info_text = Label(text="info text", width=40)
info_text.pack()

listBox = Listbox(width=40, selectmode="multiple")
listBox.pack()

entries = [Entry(), Entry(), Entry()]
for e in entries:
    e.pack()

Button(text="Apply Edit", command=apply_edit).pack(side=LEFT)
Button(text="Edit", command=edit).pack(side=LEFT)
Button(text="Insert", command=insert).pack(side=LEFT)
Button(text="Find", command=find).pack(side=LEFT)
Button(text="Refresh", command=refresh).pack(side=LEFT)
Button(text="Remove", command=lambda: remove(listBox.curselection())).pack(side=LEFT)

mainloop()
