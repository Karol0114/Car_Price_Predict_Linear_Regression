import tkinter as tk
from tkinter import messagebox
import customtkinter as ct
import machine_learning as ml
import numpy as np
import analysis as an
import pandas as pd


#df_for_application = pd.read_csv('cena_samochodow_regresja/transormed_data.csv')

#df_for_application.info()


#Funkcja słuzy do przewidywania ceny na podstawie zestawu danych wejsciowych. Wykorzystujemy tu model regresji liniowej.
def predict_price():
    predict_array = np.array([data_list])
    price_predict = np.exp(ml.model.predict(predict_array))[0]
    return price_predict

# Funkcja przechowyuwująca oraz w przypadku potrzeby zamieniająca dane podane przez użytkownika oraz dodająca ją owe dane do listy.
def save_data():
    symboling = symboling_txt.get()
    data_list.append(int(symboling))
    symboling_txt.delete(0, tk.END)
    
    fueltype = fueltype_txt.get()
    fueltype = an.fueltype_swap(fueltype)
    data_list.append(fueltype)
    fueltype_txt.delete(0, tk.END)
    
    aspiration = aspiration_txt.get()
    aspiration = an.aspiration_swap(aspiration)
    data_list.append(aspiration)
    aspiration_txt.delete(0, tk.END)
    
    doornumber = doornumber_txt.get()
    doornumber = an.doornumber_swap(doornumber)
    data_list.append(doornumber)
    doornumber_txt.delete(0, tk.END)
    
    
    enginelocation = enginelocation_txt.get()
    enginelocation = an.enginelocation_swap(enginelocation)
    data_list.append(enginelocation)
    enginelocation_txt.delete(0, tk.END)
    
    wheelbase = wheelbase_txt.get()
    data_list.append(float(wheelbase))
    wheelbase_txt.delete(0, tk.END)
    
    carlength = carlength_txt.get()
    data_list.append(float(carlength))
    carlength_txt.delete(0, tk.END)
    
    carwidth = carwidth_txt.get()
    data_list.append(float(carwidth))
    carwidth_txt.delete(0, tk.END)
    
    carheight = carheight_txt.get()
    data_list.append(float(carheight))
    carheight_txt.delete(0, tk.END)
    
    curbweight = curbweight_txt.get()
    data_list.append(int(curbweight))
    curbweight_txt.delete(0, tk.END)
    
    
    enginesize = enginesize_txt.get()
    data_list.append(int(enginesize))
    enginesize_txt.delete(0, tk.END)
    
    
    boreratio = boreratio_txt.get()
    data_list.append(float(boreratio))
    boreratio_txt.delete(0, tk.END)
    
    
    stroke = stroke_txt.get()
    data_list.append(float(stroke))
    stroke_txt.delete(0, tk.END)
    
    
    compressionratio = compressionratio_txt.get()
    data_list.append(float(compressionratio))
    compressionratio_txt.delete(0, tk.END)
    
    
    horsepower = horsepower_txt.get()
    data_list.append(int(horsepower))
    horsepower_txt.delete(0, tk.END)
    
    
    peakrpm = peakrpm_txt.get()
    data_list.append(int(peakrpm))
    peakrpm_txt.delete(0, tk.END)
    
    
    citympg = citympg_txt.get()
    data_list.append(int(citympg))
    citympg_txt.delete(0, tk.END)
    
    
    highwaympg = highwaympg_txt.get()
    data_list.append(int(highwaympg))
    highwaympg_txt.delete(0, tk.END)
    
    
    carbody = carbody_txt.get()
    #Lista cech kodowana One-Hot Encoding
    carbody_features = ['convertible', 'hardtop ', 'hatchback ', 'sedan ', 'wagon' ]
    
    #Słownik z wartościami zerowymi
    carbody_encoded = {feature: 0 for feature in carbody_features}
    
    #Przypisanie wartości 1 dla podanej przez użytkownika cechy
    if carbody in carbody_encoded:
        carbody_encoded[carbody] = 1
    
    #Dodanie cechy w formie one hot encoding do listy danych
    data_list.extend(list(carbody_encoded.values()))
    
    carbody_txt.delete(0, tk.END)
    
    
    drivewheel = drivewheel_txt.get()
    
    drivewheel_features = ['4wd', 'fwd', 'rwd']
    
    drivewheel_encoded = {feature: 0 for feature in drivewheel_features}
    
    if drivewheel in drivewheel_encoded:
        drivewheel_encoded[drivewheel] = 1
        
    
    data_list.extend(list(drivewheel_encoded.values()))
    
    drivewheel_txt.delete(0, tk.END)
    
    
    enginetype = enginetype_txt.get()
    
    enginetype_features = ['dohc', 'dohcv', 'l', 'ohc', 'ohcf', 'ohcv', 'rotor']
    
    enginetype_encoded = {feature: 0 for feature in enginetype_features}
    
    if enginetype in enginetype_features:
        enginetype_encoded[enginetype] = 1
    
    
    data_list.extend(list(enginetype_encoded.values()))
    
    enginetype_txt.delete(0, tk.END)
    
    
    fuelsystem = fuelsystem_txt.get()
    fuelsystem_features = ['1bbl', '2bbl', '4bbl', 'idi', 'mfi', 'mpfi', 'spdi', 'spfi']
    
    fuelsystem_encoded = {feature: 0 for feature in fuelsystem_features}
    
    if fuelsystem in fuelsystem_features:
        fuelsystem_encoded[fuelsystem] = 1
        
    data_list.extend(list(fuelsystem_encoded.values()))
    
    fuelsystem_txt.delete(0, tk.END) 
    
    
    cylindernumber = cylindernumber_txt.get()
    
    cylindernumber_features = ['eight', 'five', 'four', 'six', 'three', 'twelve', 'two']
    
    cylindernumber_encoded = {feature: 0 for feature in cylindernumber_features}
    
    if cylindernumber in cylindernumber_features:
        cylindernumber_encoded[cylindernumber] = 1
    
    data_list.extend(list(cylindernumber_encoded.values()))
    
    cylindernumber_txt.delete(0, tk.END)
    
    predicted_price = predict_price()
    
    messagebox.showinfo("Przewidywana cena", f"Przewidywana cena samochodu: {predicted_price}")
    

#Funkcja służąca do resetowania danych  
def reset_data():
    data_list.clear()

data_list = []


#Wygląda aplikacji
ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

app=ct.CTk()
app.geometry("1200x900")

symboling_label = ct.CTkLabel(master = app, text = 'symboling')
symboling_label.place(relx=0.1, rely=0.05, anchor=tk.CENTER)
symboling_txt=ct.CTkEntry(master=app)
symboling_txt.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

fueltype_label = ct.CTkLabel(master = app, text = 'fueltype')
fueltype_label.place(relx=0.3, rely=0.05, anchor=tk.CENTER)
fueltype_txt=ct.CTkEntry(master=app)
fueltype_txt.place(relx=0.3, rely=0.1, anchor=tk.CENTER)

aspiration_label = ct.CTkLabel(master = app, text = 'aspiration')
aspiration_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
aspiration_txt=ct.CTkEntry(master=app)
aspiration_txt.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

doornumber_label = ct.CTkLabel(master = app, text = 'doornumber')
doornumber_label.place(relx=0.7, rely=0.05, anchor=tk.CENTER)
doornumber_txt=ct.CTkEntry(master=app)
doornumber_txt.place(relx=0.7, rely=0.1, anchor=tk.CENTER)

carbody_label = ct.CTkLabel(master = app, text = 'carbody')
carbody_label.place(relx=0.9, rely=0.05, anchor=tk.CENTER)
carbody_txt=ct.CTkEntry(master=app)
carbody_txt.place(relx=0.9, rely=0.1, anchor=tk.CENTER)

drivewheel_label = ct.CTkLabel(master = app, text = 'drivewheel')
drivewheel_label.place(relx=0.1, rely=0.25, anchor=tk.CENTER)
drivewheel_txt=ct.CTkEntry(master=app)
drivewheel_txt.place(relx=0.1, rely=0.3, anchor=tk.CENTER)

enginelocation_label = ct.CTkLabel(master = app, text = 'enginelocation')
enginelocation_label.place(relx=0.3, rely=0.25, anchor=tk.CENTER)
enginelocation_txt=ct.CTkEntry(master=app)
enginelocation_txt.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

wheelbase_label = ct.CTkLabel(master = app, text = 'wheelbase')
wheelbase_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
wheelbase_txt=ct.CTkEntry(master=app)
wheelbase_txt.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

carlength_label = ct.CTkLabel(master = app, text = 'carlength')
carlength_label.place(relx=0.7, rely=0.25, anchor=tk.CENTER)
carlength_txt=ct.CTkEntry(master=app)
carlength_txt.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

carwidth_label = ct.CTkLabel(master = app, text = 'carwidth')
carwidth_label.place(relx=0.9, rely=0.25, anchor=tk.CENTER)
carwidth_txt=ct.CTkEntry(master=app)
carwidth_txt.place(relx=0.9, rely=0.3, anchor=tk.CENTER)

carheight_label = ct.CTkLabel(master = app, text = 'carheight')
carheight_label.place(relx=0.1, rely=0.45, anchor=tk.CENTER)
carheight_txt=ct.CTkEntry(master=app)
carheight_txt.place(relx=0.1, rely=0.5, anchor=tk.CENTER)

curbweight_label = ct.CTkLabel(master = app, text = 'curbweight')
curbweight_label.place(relx=0.3, rely=0.45, anchor=tk.CENTER)
curbweight_txt=ct.CTkEntry(master=app)
curbweight_txt.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

enginetype_label = ct.CTkLabel(master = app, text = 'carheight')
enginetype_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
enginetype_txt=ct.CTkEntry(master=app)
enginetype_txt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

cylindernumber_label = ct.CTkLabel(master = app, text = 'cylindernumber')
cylindernumber_label.place(relx=0.7, rely=0.45, anchor=tk.CENTER)
cylindernumber_txt=ct.CTkEntry(master=app)
cylindernumber_txt.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

enginesize_label = ct.CTkLabel(master = app, text = 'enginesize')
enginesize_label.place(relx=0.9, rely=0.45, anchor=tk.CENTER)
enginesize_txt=ct.CTkEntry(master=app)
enginesize_txt.place(relx=0.9, rely=0.5, anchor=tk.CENTER)

fuelsystem_label = ct.CTkLabel(master = app, text = 'fuelsystem')
fuelsystem_label.place(relx=0.1, rely=0.65, anchor=tk.CENTER)
fuelsystem_txt=ct.CTkEntry(master=app)
fuelsystem_txt.place(relx=0.1, rely=0.7, anchor=tk.CENTER)

boreratio_label = ct.CTkLabel(master = app, text = 'boreratio')
boreratio_label.place(relx=0.3, rely=0.65, anchor=tk.CENTER)
boreratio_txt=ct.CTkEntry(master=app)
boreratio_txt.place(relx=0.3, rely=0.7, anchor=tk.CENTER)

stroke_label = ct.CTkLabel(master = app, text = 'stroke')
stroke_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
stroke_txt=ct.CTkEntry(master=app)
stroke_txt.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

compressionratio_label = ct.CTkLabel(master = app, text = 'compressionratio')
compressionratio_label.place(relx=0.7, rely=0.65, anchor=tk.CENTER)
compressionratio_txt=ct.CTkEntry(master=app)
compressionratio_txt.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

horsepower_label = ct.CTkLabel(master = app, text = 'horsepower')
horsepower_label.place(relx=0.9, rely=0.65, anchor=tk.CENTER)
horsepower_txt=ct.CTkEntry(master=app)
horsepower_txt.place(relx=0.9, rely=0.7, anchor=tk.CENTER)

peakrpm_label = ct.CTkLabel(master = app, text = 'peakrpm')
peakrpm_label.place(relx=0.1, rely=0.85, anchor=tk.CENTER)
peakrpm_txt=ct.CTkEntry(master=app)
peakrpm_txt.place(relx=0.1, rely=0.9, anchor=tk.CENTER)

citympg_label = ct.CTkLabel(master = app, text = 'citympg')
citympg_label.place(relx=0.3, rely=0.85, anchor=tk.CENTER)
citympg_txt=ct.CTkEntry(master=app)
citympg_txt.place(relx=0.3, rely=0.9, anchor=tk.CENTER)

highwaympg_label = ct.CTkLabel(master = app, text = 'highwaympg')
highwaympg_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
highwaympg_txt=ct.CTkEntry(master=app)
highwaympg_txt.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


save_button = tk.Button(master = app, text = 'Sprawdź cenę', command = save_data)
save_button.place(relx = 0.7, rely = 0.9, anchor= tk.CENTER)

reset_button = tk.Button(master = app, text = 'Zresetuj Dane', command = reset_data)
reset_button.place(relx = 0.9, rely = 0.9, anchor= tk.CENTER)

app.mainloop()
