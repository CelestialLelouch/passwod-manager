
import customtkinter as ctk;
from tkinter import messagebox;
import passManager as passMan;

root = ctk.CTk();
root.title("Password Generator/Manager");
root.geometry('600x400')
root.grid_columnconfigure(0, weight=1)
''' FONTS '''
font_1 = ctk.CTkFont(family= 'Britanic Bold', weight= 'bold');

""" FUNCTIONS """
def createProfile():
    username = entry_username.get()
    platform = entry_platform.get()
    pin = ctk.CTkInputDialog(font=font_1, title='PIN', text='Enter Safe Pin').get_input()
    length = int(spn_len.get())

    if passMan.check_code(pin) == False:
        messagebox.showwarning('INVALID PIN', 'The PIN you have entered does not match the SAFE PIN')
    elif(username == '') or (platform == ''):
        messagebox.showwarning('Empty Fields', 'Please fill in  all fields')
    else:
        cypher = passMan._getcypher()
        password = passMan.generate_password(length)
        passMan.save_password('passwords.txt', platform, username, passMan._shifter(cypher, password))
        ctk.CTkLabel(root, text= password, font=font_1).grid()


def getProfiles():
    pin = ctk.CTkInputDialog(font=font_1, title='PIN', text='Enter Safe Pin').get_input()
    if not(passMan.check_code(pin)):
        messagebox.showwarning('INVALID PIN', 'The PIN you have entered does not match the SAFE PIN')
    else:
        textwidget = ctk.CTkTextbox(root)
        textwidget.insert('end',text=passMan.read_passwords())
        textwidget.grid()

def logIn():
    pin = ctk.CTkInputDialog(font=font_1, title='PIN', text='Enter Safe Pin').get_input() 
    if not(passMan.check_code(pin)):
        exit();

def createAcc():
    with open('safe_code.txt', 'r') as file:
        content = file.read()
        if content == '':
            pin = ctk.CTkInputDialog(font=font_1, title='PIN', text='Create A 4-Digit Safe Pin For You Account').get_input()
            open('safe_code.txt', 'w').write(pin)
        else:
            pass

""" CREATE ACC / LOG IN"""
createAcc()
logIn()

""" COMPONENTS """
btnGenPass = ctk.CTkButton(root, text= ' Generate Password', command=createProfile);
btnGetProf = ctk.CTkButton(root, text='Get Profiles',command= getProfiles);
entry_platform = ctk.CTkEntry(root, width=200,  placeholder_text='Platform');
entry_username = ctk.CTkEntry(root, width=200,placeholder_text='Username');
lbl_passlen = ctk.CTkLabel(root, text="Password Length", font=font_1);
spn_len = ctk.CTkComboBox(root,width=80,values=['6','8','10','12','14','16','18','20']);


""" LAYOUT """
entry_platform.grid(pady= 20);
entry_username.grid(pady= 5);
lbl_passlen.grid(pady=10);
spn_len.grid(pady=0);
btnGenPass.grid(pady=20);
btnGetProf.grid(pady=5);


""""""

root.mainloop();