import tkinter
window=tkinter.Tk()
window.title("Ree")
label=tkinter.Label(window, text="Ree",font=("Bell MT",25)).pack()
window.geometry("400x200")
bt=tkinter.Button(window,text="Enter",bg="Orange",fg="Red")
bt.grid(row = 1, coloumn = 0)
window.mainloop()
