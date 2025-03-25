import customtkinter
from PIL import Image
from CTkTable import *
import os

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Test 1')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.my_image = customtkinter.CTkImage(light_image=Image.open('pngs/table_with_numbers.png'), size=(300, 150))
        self.table = customtkinter.CTkLabel(self, image=self.my_image, text='')
        self.table.grid(row=1, column=0, pady=150)

        self.label = customtkinter.CTkLabel(self, text='У вас есть 20 секунд на запоминание чисел в таблице')
        self.label.grid(padx=10, pady=10, row=0, column=0)


app = App()
app.after(20000, app.destroy)
app.mainloop()
