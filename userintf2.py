import tkinter as tk

def foo():
	color=text_box.get()
	label.config(bg=color)

root=tk.Tk()

label=tk.Label(root,text="places",fg="black",bg="pink")
label.grid(row=0)

text_box=tk.Entry(root)
text_box.grid(row=1,column=0)

btn=tk.Button(root,text="submit",command=foo)
btn.grid(row=1,column=1)

root.mainloop()