import tkinter as tk
from tkinter import messagebox
import openpyxl
import os

def enregistrer_profil():
    prenom = entry_prenom.get()
    nom = entry_nom.get()
    age = entry_age.get()
    telephone = entry_telephone.get()
    email = entry_email.get()
    registre_national = entry_registre.get()
    commentaire = entry_commentaire.get()

    #Determine the path to the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'desktop')

    # Create the file path
    file_path = os.path.join(desktop_path, 'profiles.xlsx')

    # Open the workbook (if it exists) or create a new one
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
    except FileNotFoundError:
        workbook = openpyxl.load_workbook(file_path)
        sheet=workbook.active
        sheet.append(['Prénom', 'Nom', 'Âge', 'Numéro de téléphone', 'Email', 'Registre national', 'Commentaire'])

    # Add the profile to the Excel sheet
    sheet.append([prenom, nom, age, telephone, email, registre_national, commentaire])

    # Save the workbook  
    workbook.save(file_path)

    # Display a success message
    tk.messagebox.showinfo('Succès', 'Le profil a été enregistré avec succès.')

    # Create the main window
fenetre = tk.Tk()
fenetre.title('Enregistrement de profils')

# Create labels and entry fields
label_prenom = tk.Label(fenetre, text='Prénom:')
label_prenom.pack()
entry_prenom = tk.Entry(fenetre)
entry_prenom.pack()

label_nom = tk.Label(fenetre, text='Nom:')
label_nom.pack()
entry_nom = tk.Entry(fenetre)
entry_nom.pack()

label_age = tk.Label(fenetre, text='Âge:')
label_age.pack()
entry_age = tk.Entry(fenetre)
entry_age.pack()

label_telephone = tk.Label(fenetre, text='Numéro de téléphone:')
label_telephone.pack()
entry_telephone = tk.Entry(fenetre)
entry_telephone.pack()

label_email = tk.Label(fenetre, text='Email:')
label_email.pack()
entry_email = tk.Entry(fenetre)
entry_email.pack()

label_registre = tk.Label(fenetre, text='Registre national:')
label_registre.pack()
entry_registre = tk.Entry(fenetre)
entry_registre.pack()

label_commentaire = tk.Label(fenetre, text='Commentaire:')
label_commentaire.pack()
entry_commentaire = tk.Entry(fenetre)
entry_commentaire.pack()

# Create the save button
bouton_enregistrer = tk.Button(fenetre, text='Enregistrer', command=enregistrer_profil)
bouton_enregistrer.pack()

# Start the main GUI loop
fenetre.mainloop()



   

