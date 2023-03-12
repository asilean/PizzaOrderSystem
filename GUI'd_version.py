from csv import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox

global_cost = 0


class pizza:

    def __innit__(self, name, cost):
        self.name = name
        self.cost = cost

    @property
    def get_cost(self):
        return self.cost

    @property
    def get_name(self):
        return self.name


Order = []

writer = open('orders_database.csv', 'w', newline='', encoding="utf-8")
writer.write('Bill\n')


class Klasik(pizza):
    name = "Klasik"
    cost = 70

    @staticmethod
    def get_description():
        return f"This recipe contains an exceptional pizza dough, low-moisture mozzarella cheese,tomato sauce and simple garnish of fresh herbs."


class Margherita(pizza):
    name = "Margherita"
    cost = 65

    @staticmethod
    def get_description():
        return f"Margherita pizza features a bubbly crust, crushed San Marzano tomato sauce, fresh mozzarella and basil, a drizzle of olive oil, and a sprinkle of salt."


class TurkPizza(pizza):
    name = "TürkPizza"
    cost = 90

    @staticmethod
    def get_description():
        return f"This is a sausage pizza, with onions, green peppers, and bacon."


class SadePizza(pizza):
    name = "SadePizza"
    cost = 60

    @staticmethod
    def get_description():
        return f"The delicious combination of crispy pizza crust, flavorful tomato sauce, and bubbly cheese."


class Decorator(pizza):
    pass


class zeytin(Decorator):
    name = "zeytin"
    cost = 5


class mantarlar(Decorator):
    name = "mantarlar"
    cost = 15


class keci_peyniri(Decorator):
    name = "Keçi Peyniri"
    cost = 10


class Et(Decorator):
    name = "Et"
    cost = 25


class sogan(Decorator):
    name = "Soğan"
    cost = 5


class Misir(Decorator):
    name = "Mısır"
    cost = 5


class No_Topping(Decorator):
    name = "No Topping"
    cost = 0


class MainWindow(tk.Frame):


    def __init__(self, *args, **kwargs):

        tk.Frame.__init__(self, *args, **kwargs)
        l1=Label(self,text="Classic Pizza\n\nThis recipe contains an exceptional pizza dough, low-moisture mozzarella cheese,tomato sauce and simple garnish of fresh herbs.",pady=26,bg="#7ed6df")
        l1.pack(side="top", expand=True)
        self.button1 = tk.Button(self, text="Add to cart",
                                 command=lambda: [self.create_window(), get_ClassicPizza()], pady=10, padx=5, bg='#A3CB38', bd='0')
        self.button1.pack(side="top", expand=True)
        l2 = Label(self,
                   text="Margherita pizza\n\nThis recipe features a bubbly crust, crushed San Marzano tomato sauce, fresh mozzarella and basil, a drizzle of olive oil, and a sprinkle of salt.",pady=26,bg="#7ed6df")
        l2.pack(side="top",  expand=True)
        self.button2 = tk.Button(self, text="Add to cart",
                                 command=lambda: [self.create_window(), get_MargheritaPizza()], pady=10, padx=5, bg='#A3CB38', bd='0')
        self.button2.pack(side="top", expand=True)
        l3 = Label(self,
                  text="Turkish Pizzza\n\nThis is a sausage pizza, with onions, green peppers, and bacon.",pady=26,bg="#7ed6df")
        l3.pack(side="top",  expand=True)
        self.button3 = tk.Button(self, text="Add to cart",
                                 command=lambda: [self.create_window(), get_TurkPizza()], pady=10, padx=5, bg='#A3CB38', bd='0')
        self.button3.pack(side="top", expand=True)
        l4 = Label(self,
                   text="Plain Pizza\n\nThe delicious combination of crispy pizza crust, flavorful tomato sauce, and bubbly cheese.",pady=26,bg="#7ed6df")
        l4.pack(side="top",  expand=True)
        self.button4 = tk.Button(self, text="Add to cart",
                                 command=lambda: [self.create_window(), get_PlainPizza()], pady=10, padx=5, bg='#A3CB38', bd='0')
        self.button4.pack(side="top", expand=True)
        name = Entry(self, width=30, borderwidth=3)
        ID_number = Entry(self, width=30, borderwidth=3)
        Card_number = Entry(self, width=30, borderwidth=3)
        main_lst = []

        def Add():
            writer.write("\nName:"+name.get()+"\n"+"ID number:"+ID_number.get()+"\n"+"Card Number:"+Card_number.get()+"\n")
            messagebox.showinfo("Information", "Order Completed")


        label1 = Label(self, text="Name: ", padx=20, pady=10)
        label1.pack(side="top", expand=True)
        name.pack(side="top", expand=True)
        label2 = Label(self, text="ID number: ", padx=20, pady=10)
        label2.pack(side="top", expand=True)
        ID_number.pack(side="top", expand=True)
        label3 = Label(self, text="Card Number: ", padx=20, pady=10)
        label3.pack(side="top", expand=True)
        Card_number.pack(side="top", expand=True)
        add = Button(self, text="Complete Order", padx=20, pady=10, command=Add)

        add.pack(side="top")






    def create_window(self):
        def exit_btn():
            t.destroy()
            t.update()

        def control():
            if var1.get():
                get_zeytin()
            if var2.get():
                get_mantar()
            if var3.get():
                get_keci()
            if var4.get():
                get_et()
            if var5.get():
                get_sogan()
            if var6.get():
                get_misir()
            if var7.get():
                get_NoTopping()

        t = tk.Toplevel(self)
        t.wm_title("Window")
        l = tk.Label(t, text="toppings?").grid(row=0, sticky=W)
        var1 = IntVar()
        Checkbutton(t, text="zeytin", variable=var1).grid(row=1, sticky=W)
        var2 = IntVar()
        Checkbutton(t, text="mantar", variable=var2).grid(row=2, sticky=W)
        var3 = IntVar()
        Checkbutton(t, text="Keçi Peyniri", variable=var3).grid(row=3, sticky=W)
        var4 = IntVar()
        Checkbutton(t, text="Et", variable=var4).grid(row=4, sticky=W)
        var5 = IntVar()
        Checkbutton(t, text="Soğan", variable=var5).grid(row=5, sticky=W)
        var6 = IntVar()
        Checkbutton(t, text="Mısır", variable=var6).grid(row=6, sticky=W)
        var7 = IntVar()
        Checkbutton(t, text="No Topping", variable=var7).grid(row=7, sticky=W)
        Button(t, text='complete', command=lambda: [control(), exit_btn(), w.config(text="Total cost "+str(global_cost))]).grid(row=8,
                                                                                                             sticky=W,
                                                                                                             pady=4)


r = tk.Tk()
w = Label(r, text="Total cost "+str(global_cost),bg="#A3CB38",padx=10,pady=5)  # shows as text in the window
r.config(background="#F79F1F")
w.pack()
# w.place(anchor=S)



main = MainWindow(r)
main.config(background="#F79F1F")
main.pack(side="top", fill="both", expand=True)

r.title('Kopernik Pizza')
r.geometry("1200x1000")
r.resizable(0, 0)




def get_zeytin():
    global global_cost
    Order.append(zeytin())
    writer.write('+zeytin' + '5₺')
    global_cost += 5


def get_mantar():
    global global_cost
    Order.append(mantarlar())
    writer.write('+mantar' + '10₺')
    global_cost += 10


def get_keci():
    global global_cost
    Order.append(keci_peyniri())
    writer.write('+Keçi peyniri' + '12₺')
    global_cost += 12


def get_et():
    global global_cost
    Order.append(Et())
    writer.write('+Et' + '25₺')
    global_cost += 25


def get_sogan():
    global global_cost
    Order.append(sogan())
    writer.write('+Soğan' + '5₺')
    global_cost += 5


def get_misir():
    global global_cost
    Order.append(Misir())
    writer.write('+Mısır' + '3₺')
    global_cost += 3


def get_NoTopping():
    Order.append(No_Topping())
    writer.write('No topping')


def get_ClassicPizza():
    global global_cost
    Order.append(Klasik())
    writer.write('Klasik Pizza' + '65₺')
    global_cost += 65


def get_MargheritaPizza():
    global global_cost
    Order.append(Margherita())
    writer.write('Margherita' + '60₺')
    global_cost += 60


def get_TurkPizza():
    global global_cost
    Order.append(TurkPizza())
    writer.write('Türk Pizza' + '90₺')
    global_cost += 90


def get_PlainPizza():
    global global_cost
    Order.append(SadePizza())
    writer.write('Sade Pizza' + '50₺')
    global_cost += 50


r.mainloop()





class Main:
    writer.write('Total cost ' + str(global_cost) + '₺')
    writer.close()
    print("Total cost: " + str(global_cost) + "₺")

