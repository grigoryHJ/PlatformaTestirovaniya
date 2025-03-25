import customtkinter
from CTkTable import *


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('500x500')
        self.title('Test 1')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        value = [[1, 2, 3, 4],
                 [1, 2, 3, 4]]

        self.table = CTkTable(self, row=4, column=4, values=value, write=1)
        self.table.grid(row=0, column=0, padx=20)


app = App()
app.mainloop()
