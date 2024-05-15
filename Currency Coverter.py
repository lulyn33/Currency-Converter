from currency_converter import CurrencyConverter
import tkinter as tk

c = CurrencyConverter()
#print(c.convert(100, 'USD', 'EUR'))

window = tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")

def clicked():
    amount = int(entry1.get())
    cur1 = entry2.get()
    cur2 = entry3.get()
    data = c.convert(amount,cur1,cur2)
    label4 = tk.Label(window,text=data,font="Times 16 bold").place(x=150,y=300)

label = tk.Label(window,text ="Currency Converter",font='Times 20 bold').place(x = 100,y = 40)
label1 = tk.Label(window,text ="Enter Amount Here: ",font = "Times 16 bold").place(x = 90,y = 100 )
entry1 = tk.Entry(window)

label2 = tk.Label(window,text ="Enter Your Currency Here: ",font = "Times 16 bold").place(x = 30,y = 150 )
entry2 = tk.Entry(window)

label3 = tk.Label(window,text ="Enter Your Desired Currency: ",font = "Times 16 bold").place(x = 5,y = 200 )
entry3 = tk.Entry(window)

button = tk.Button(window,text = "click",font="Times 16 bold",command=clicked).place(x = 220,y = 250)

entry1.place(x = 280, y = 105)
entry2.place(x = 280, y = 155)
entry3.place(x = 280, y = 205)

window.mainloop()

