import customtkinter


class Test1Q1(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("Question 1")
        self.geometry("400x220")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.radiobutton_frame = MyRadiobuttonFrame(self, title="1) 5 + 4 = ?", values=["9", "6", "4"])
        self.radiobutton_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.radiobutton_frame.configure(fg_color="transparent")

        self.button = customtkinter.CTkButton(self, text="Next", command=self.open_Q)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=2)

        self.T1Q2 = None

    def open_Q(self):
        if self.T1Q2 is None or not self.T1Q2.winfo_exists():
            self.withdraw()
            self.T1Q2 = Test1Q2(self)
        else:
            self.T1Q2.focus()


class Test2Q1(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("Question 1")
        self.geometry("400x220")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.radiobutton_frame = MyRadiobuttonFrame(self, title="1) 10 - 6 = ?", values=["14", "6", "4"])
        self.radiobutton_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.radiobutton_frame.configure(fg_color="transparent")

        self.button = customtkinter.CTkButton(self, text="Next", command=self.open_Q)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=2)

        self.T2Q2 = None

    def open_Q(self):
        if self.T2Q2 is None or not self.T2Q2.winfo_exists():
            self.withdraw()
            self.T2Q2 = Test2Q2(self)
        else:
            self.T2Q2.focus()


class Test1Q2(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("Question 2")
        self.geometry("400x220")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.radiobutton_frame = MyRadiobuttonFrame(self, title="2) 6 + 5 = ?", values=["1", "11", "4"])
        self.radiobutton_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.radiobutton_frame.configure(fg_color="transparent")

        self.button = customtkinter.CTkButton(self, text="Next", command=self.open_Q)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=2)

        self.T1Q3 = None

    def open_Q(self):
        if self.T1Q3 is None or not self.T1Q3.winfo_exists():
            self.withdraw()
            self.T1Q3 = Test1Q3(self)
        else:
            self.T1Q3.focus()


class Test2Q2(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("Question 2")
        self.geometry("400x220")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.radiobutton_frame = MyRadiobuttonFrame(self, title="2) 61 - 5 = ?", values=["56", "46", "76"])
        self.radiobutton_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.radiobutton_frame.configure(fg_color="transparent")

        self.button = customtkinter.CTkButton(self, text="Next", command=self.open_Q)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=2)

        self.T2Q3 = None

    def open_Q(self):
        if self.T2Q3 is None or not self.T2Q3.winfo_exists():
            self.withdraw()
            self.T2Q3 = Test2Q3(self)
        else:
            self.T2Q3.focus()


class Test1Q3(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("Question 3")
        self.geometry("400x220")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.radiobutton_frame = MyRadiobuttonFrame(self, title="2) 6 - 5 = ?", values=["1", "11", "4"])
        self.radiobutton_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.radiobutton_frame.configure(fg_color="transparent")

        self.button = customtkinter.CTkButton(self, text="Main Page", command=self.main_Page)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=2)

    def main_Page(self):
        self.withdraw()


class Test2Q3(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("Question 3")
        self.geometry("400x220")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.radiobutton_frame = MyRadiobuttonFrame(self, title="2) 16 - 5 = ?", values=["12", "11", "10"])
        self.radiobutton_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.radiobutton_frame.configure(fg_color="transparent")

        self.button = customtkinter.CTkButton(self, text="Main Page", command=self.main_Page)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=2)

    def main_Page(self):
        self.withdraw()

# -----------------------------------------------------------------------------------------------------


class MyRadiobuttonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("my app")
        self.geometry("400x220")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.T1Q1 = None
        self.T2Q1 = None

        self.radiobutton_frame = MyRadiobuttonFrame(self, "Tests", values=["Test 1", "Test 2"])
        self.radiobutton_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.radiobutton_frame.configure(fg_color="transparent")

        self.button = customtkinter.CTkButton(self, text="Start", command=self.open_Q)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def open_Q(self):
        if self.radiobutton_frame.get() == "Test 1":
            if self.T1Q1 is None or not self.T1Q1.winfo_exists():
                self.T1Q1 = Test1Q1(self)  # create window if its None or destroyed
            else:
                self.T1Q1.focus()
        elif self.radiobutton_frame.get() == "Test 2":
            if self.T2Q1 is None or not self.T2Q1.winfo_exists():
                self.T2Q1 = Test2Q1(self)  # create window if its None or destroyed
            else:
                self.T2Q1.focus()


if __name__ == "__main__":
    app = App()
    app.mainloop()
