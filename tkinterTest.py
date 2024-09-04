import tkinter as tk


def getValue():
    entryValue = entry.get()
    entryValue2 = entry2.get()
    Sum = int(entryValue) + int(entryValue2) #have to typecast this to int to do math ops
    #print(entryValue) #---> this prints the value to the console
    label1 = tk.Label(window, text=Sum)
    label1.pack()


window = tk.Tk()
window.geometry("800x500")
window.title("Tkinter test")


label = tk.Label(window, text="Hello tkinter test", font=('Arial', 18)) #the window parameter just means that the label is for the window that we created.
label.pack(padx=20, pady=20) #pack() adds the text label to the window

#textBox = tk.Text(window, height=4)
#textBox.pack()

entry = tk.Entry(window)
entry.pack()
entry2 = tk.Entry(window)
entry2.pack()
button = tk.Button(command=getValue, text="Submit")
button.pack()














window.mainloop()