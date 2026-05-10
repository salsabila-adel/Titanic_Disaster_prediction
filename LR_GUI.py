import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import joblib
from PIL import Image, ImageTk



# Load Model


model = joblib.load("model2.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")



# Main Window


root = tk.Tk()
root.title("Titanic Survival Prediction")
root.geometry("700x650")
root.resizable(False, False)



# Background


bg_image = Image.open("download (99).png")
bg_image = bg_image.resize((700, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)



# Fonts


title_font = ("Helvetica", 20, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")



# Title (GRID بدل PACK)


title = tk.Label(
    root,
    text="Titanic Survival Prediction",
    font=title_font,
    bg="#1e1e2f",
    fg="white"
)
title.grid(row=0, column=0, columnspan=2, pady=10)



# Label Function


def create_label(text, row):
    tk.Label(
        root,
        text=text,
        font=label_font,
        bg="#2b2b40",
        fg="white"
    ).grid(row=row, column=0, sticky="w", padx=10, pady=5)



# Inputs


create_label("Name", 1)
name_entry = tk.Entry(root, font=label_font)
name_entry.grid(row=1, column=1)

create_label("Gender", 2)
gender_combo = ttk.Combobox(root, values=["male", "female"], state="readonly")
gender_combo.grid(row=2, column=1)

create_label("Passenger Class", 3)
pclass_combo = ttk.Combobox(root, values=[1, 2, 3], state="readonly")
pclass_combo.grid(row=3, column=1)

create_label("Embarked(الميناء اللى ركبت منه)", 4)
embarked_combo = ttk.Combobox(root, values=["S", "C", "Q"], state="readonly")
embarked_combo.grid(row=4, column=1)

create_label("Age", 5)
age_entry = tk.Entry(root, font=label_font)
age_entry.grid(row=5, column=1)

create_label("Fare(سعر التذكرة)", 6)
fare_entry = tk.Entry(root, font=label_font)
fare_entry.grid(row=6, column=1)

create_label("Siblings/Spouses(عدد الاخوة)", 7)
sibsp_entry = tk.Entry(root, font=label_font)
sibsp_entry.grid(row=7, column=1)

create_label("Parents/Children(عدد الاباء و الاطفال )", 8)
parch_entry = tk.Entry(root, font=label_font)
parch_entry.grid(row=8, column=1)



# Result


result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 16, "bold"),
    bg="#1e1e2f"
)
result_label.grid(row=9, column=0, columnspan=2, pady=10)



# Predict Function


def predict_survival():
    try:

        name = name_entry.get().strip()
        if not all(part.isalpha() for part in name.split(",")):
            messagebox.showerror("Invalid Name", " Please enter only LETTERS 🙂")
            return

        fare = float(fare_entry.get())
        if fare < 200 or fare > 500:
            messagebox.showerror("Invalid Fare", " Please enter between 200 and 500 🙂")
            return
        
        sex = 0 if gender_combo.get() == "male" else 1

        pclass = int(pclass_combo.get())
        age = float(age_entry.get())
        fare = float(fare_entry.get())
        sibsp = int(sibsp_entry.get())
        parch = int(parch_entry.get())

        family_size = sibsp + parch + 1
        is_alone = 1 if family_size == 1 else 0

        embarked = embarked_combo.get()

        data = {
            'Pclass': pclass,
            'Sex': sex,
            'Age': age,
            'SibSp': sibsp,
            'Parch': parch,
            'Fare': fare,
            'FamilySize': family_size,
            'IsAlone': is_alone,
            'Embarked_C': 1 if embarked == 'C' else 0,
            'Embarked_Q': 1 if embarked == 'Q' else 0,
            'Embarked_S': 1 if embarked == 'S' else 0,
            'Title_Mr': 0,
            'Title_Miss': 0,
            'Title_Mrs': 0,
            'Title_Master': 0,
            'Title_Other': 0
        }

        df_input = pd.DataFrame([data])
        df_input = df_input.reindex(columns=columns, fill_value=0)

        cols_to_scale = ['Age', 'Fare', 'SibSp', 'Parch', 'FamilySize']
        df_input[cols_to_scale] = scaler.transform(df_input[cols_to_scale])

        prediction = model.predict(df_input)[0]

        if prediction == 1:
            result_label.config(text="🎉 Passenger Survived", fg="#00ff99")
        else:
            result_label.config(text="💀 Passenger Did Not Survive", fg="#ff4d4d")

    except Exception as e:
        messagebox.showerror("Error", str(e))



# Clear Function


def clear_fields():
    name_entry.delete(0, tk.END)
    gender_combo.set("")
    pclass_combo.set("")
    embarked_combo.set("")
    age_entry.delete(0, tk.END)
    fare_entry.delete(0, tk.END)
    sibsp_entry.delete(0, tk.END)
    parch_entry.delete(0, tk.END)
    result_label.config(text="")



# Buttons


predict_btn = tk.Button(
    root,
    text="Predict",
    font=button_font,
    bg="#4CAF50",
    fg="white",
    command=predict_survival
)
predict_btn.grid(row=10, column=0, pady=10)

clear_btn = tk.Button(
    root,
    text="Clear",
    font=button_font,
    bg="#f44336",
    fg="white",
    command=clear_fields
)
clear_btn.grid(row=10, column=1, pady=10)



# Run


root.mainloop()