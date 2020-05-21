import tkinter as tk

on_hit = False
def ok():
    global on_hit
    if on_hit == False:
        var.set('you hit me')
    else:
        var.set('')
    on_hit = ~on_hit
window = tk.Tk()

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected ' + v)

window.title('Tuning')
window.geometry('400x300')
window.configure(background='white')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12),
        width=15, height=2)
l.pack()

b = tk.Button(window, text='ok', width=15, height=2, command=ok)
b.pack()

s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
        length=200, showvalue=0, tickinterval=2, resolution=0.01,
        command=print_selection)
s.pack()

window.mainloop()
