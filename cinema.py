import tkinter as tk
import initDB
import queries

class cinema(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (mainPage, registerPage, loginPage):
            pageName = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[pageName] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showFrame("mainPage")

    def showFrame(self, pageName):
        frame = self.frames[pageName]
        frame.tkraise()

class mainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button1 = tk.Button(self, text="Admin Login", command=lambda: controller.showFrame('loginPage'), fg='purple', bg='black', font=('Arial', 38))
        button1.pack()
        button2 = tk.Button(self, text="Reserve", command= lambda: controller.showFrame('registerPage'), fg='purple', bg='black',  font=('Arial', 38))
        button2.pack()

class registerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f_name_label = tk.Label(self, text="First Name")
        f_name_label.grid(row=0, column=0)
        f_name = tk.Entry(self, width=30)
        f_name.grid(row=0, column=1)

        l_name_label = tk.Label(self, text="Last Name")
        l_name_label.grid(row=1, column=0)
        l_name = tk.Entry(self, width=30)
        l_name.grid(row=1, column=1)

        age_label = tk.Label(self, text="Age")
        age_label.grid(row=2, column=0)
        age = tk.Entry(self, width=30)
        age.grid(row=2, column=1)

        phone_label = tk.Label(self, text="Phone")
        phone_label.grid(row=3, column=0)
        phone = tk.Entry(self, width=30)
        phone.grid(row=3, column=1)

        email_label = tk.Label(self, text="Email")
        email_label.grid(row=4, column=0)
        email = tk.Entry(self, width=30)
        email.grid(row=4, column=1)
        rows = 4
        v = tk.IntVar()
        for movie in queries.get_movies():
            rows += 1
            tk.Radiobutton(self, text=movie[1] + " " + str(movie[2]) + " " + movie[3], variable=v, value=movie[0]).grid(row=rows, column=1)
        button = tk.Button(self, text="Back", command=lambda: controller.showFrame('mainPage'), fg='purple', bg='black', font=('Arial', 38))
        button.grid(row=10, column=0)
        button = tk.Button(self, text="Reserve", command=lambda: queries.reservation(f_name, l_name, age, phone, email, v), fg='purple', bg='black',font=('Arial', 38))
        button.grid(row=10, column=1)


class loginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button = tk.Button(self, text="Back", command=lambda: controller.showFrame('mainPage'), fg='purple', bg='black',
                           font=('Arial', 38))
        button.grid(row=5, column=0)


if __name__ == "__main__":
    initDB.start()
    app = cinema()
    app.mainloop()