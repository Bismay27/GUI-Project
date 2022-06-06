from tkinter import *

window = Tk()
window.title("Voltage Regulator")

Label1 = Label(window, text="• KVA Rating of Transformer", borderwidth=5)
Label2 = Label(window, text="• No-Load Secondary Voltage", borderwidth=5)
Label3 = Label(window, text="• Secondary Resistance in Ωs", borderwidth=5)
Label4 = Label(window, text="• Secondary Reactance in Ωs", borderwidth=5)
Label5 = Label(window, text="• Load Power-Factor", borderwidth=5)
Label6 = Label(window, text="• %Regulation", borderwidth=5)


Label1.grid(row=0, column=0)
Label2.grid(row=1, column=0)
Label3.grid(row=2, column=0)
Label4.grid(row=3, column=0)
Label5.grid(row=4, column=0)
Label6.grid(row=5, column=0)
d1 = Entry(window, width=50, borderwidth=5)
d1.grid(row=0, column=1)
d2 = Entry(window, width=50, borderwidth=5)
d2.grid(row=1, column=1)
d3 = Entry(window, width=50, borderwidth=5)
d3.grid(row=2, column=1)
d4 = Entry(window, width=50, borderwidth=5)
d4.grid(row=3, column=1)
d5 = Entry(window, width=50, borderwidth=5)
d5.grid(row=4, column=1)
d6 = Entry(window, width=50, borderwidth=5)
d6.grid(row=5, column=1)


def calculate():
    d6.delete(0, "end")
    num1 = float(d1.get())
    num2 = float(d2.get())
    num3 = float(d3.get())
    num4 = float(d4.get())
    num5 = float(d5.get())

    result = (
        ((num1 / num2) * ((num3 * num5) + (num4 * (1 - num5 * num5) ** 0.5))) / num2
    ) * 100
    d6.insert(END, str(round(result,2)))


b1 = Button(window, text="Calculate", padx=2, command=calculate)
b1.grid(row=6, column=1)



window.mainloop()
