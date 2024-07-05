import customtkinter as ctk;

app = ctk.CTk()
app.title("Test Site")
app.geometry("720x500")

btnClick = ctk.CTkButton(app, text="I'm Ready");


btnClick.grid(row=0, column=0, padx=20, pady= 30)

app.mainloop()