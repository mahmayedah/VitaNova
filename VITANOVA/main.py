from tkinter import *
from tkinter import messagebox
import json

root = Tk()

root.title("VITANOVA")
root.geometry("800x700")
root.configure(bg="#E8F5E9")

title = Label(
    root,
    text="🌿 VITANOVA Health Tracker",
    font=("Arial", 24, "bold"),
    bg="#E8F5E9",
    fg="#2E7D32"
)
title.pack(pady=20)

# Name
Label(root, text="Name:").pack()
name_entry = Entry(root, width=30, font=("Arial", 11))
name_entry.pack()

# Age
Label(root, text="Age:").pack()
age_entry = Entry(root, width=30, font=("Arial", 11))
age_entry.pack()

# Water Intake
Label(root, text="Water Intake (Glasses):").pack()
water_entry = Entry(root, width=30, font=("Arial", 11))
water_entry.pack()

# Sleep Hours
Label(root, text="Sleep Hours:").pack()
sleep_entry = Entry(root, width=30, font=("Arial", 11))
sleep_entry.pack()

# Exercise
Label(root, text="Exercise (Minutes):").pack()
exercise_entry = Entry(root, width=30, font=("Arial", 11))
exercise_entry.pack()

# Steps
Label(root, text="Steps Walked:").pack()
steps_entry = Entry(root, width=30, font=("Arial", 11))
steps_entry.pack()

# Weight
Label(root, text="Weight (kg):").pack()
weight_entry = Entry(root, width=30, font=("Arial", 11))
weight_entry.pack()

# Height
Label(root, text="Height (cm):").pack()
height_entry = Entry(root, width=30, font=("Arial", 11))
height_entry.pack()


def save_record():



    weight = float(weight_entry.get())
    height = float(height_entry.get())

    height_meter = height / 100
    bmi = weight / (height_meter * height_meter)

    bmi_label.config(text=f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    category_label.config(text=f"Category: {category}")

    score = 100

    water = int(water_entry.get())
    sleep = float(sleep_entry.get())
    exercise = int(exercise_entry.get())
    steps = int(steps_entry.get())

    if water < 8:
        score -= 20

    if sleep < 7:
        score -= 20

    if exercise < 30:
        score -= 20

    if steps < 8000:
        score -= 20

    score_label.config(text=f"Health Score: {score}/100")

    suggestions = ""

    if water < 8:
        suggestions += "• Drink more water\n"

    if sleep < 7:
        suggestions += "• Sleep at least 7 hours\n"

    if exercise < 30:
        suggestions += "• Exercise at least 30 minutes\n"

    if steps < 8000:
        suggestions += "• Walk more\n"

    if suggestions == "":
        suggestions = "Excellent! Keep it up! 🎉"

    suggestion_label.config(text=suggestions)

    record = {
        "name": name_entry.get(),
        "age": age_entry.get(),
        "water": water,
        "sleep": sleep,
        "exercise": exercise,
        "steps": steps,
        "weight": weight,
        "height": height,
        "bmi": round(bmi, 2),
        "health_score": score
    }

    try:
        with open("health_data.json", "r") as file:
            data = json.load(file)
    except:
        data = []

    data.append(record)

    with open("health_data.json", "w") as file:
        json.dump(data, file, indent=4)

    messagebox.showinfo("Success", "Record Saved Successfully!")
save_button = Button(root, text="Save Record", command=save_record)




def view_history():
    try:
        with open("health_data.json", "r") as file:
            data = json.load(file)

        history = ""

        for record in data:
            history += f"Name: {record['name']}\n"
            history += f"BMI: {record['bmi']}\n"
            history += f"Score: {record['health_score']}\n"
            history += "-" * 20 + "\n"

        messagebox.showinfo("Health History", history)

    except:
        messagebox.showinfo("History", "No records found!")

save_button.pack(pady=10)

history_button = Button(
    root,
    text="View History",
    command=view_history
)

def clear_form():
    answer = messagebox.askyesno(
        "Confirm",
        "Do you want to clear all fields?"
    )

    if answer:
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        water_entry.delete(0, END)
        sleep_entry.delete(0, END)
        exercise_entry.delete(0, END)
        steps_entry.delete(0, END)
        weight_entry.delete(0, END)
        height_entry.delete(0, END)


history_button.pack(pady=5)

clear_button = Button(
    root,
    text="Clear Form",
    command=clear_form
)
clear_button.pack(pady=5)

bmi_label = Label(root, text="BMI: ")
bmi_label.pack()

category_label = Label(root, text="Category: ")
category_label.pack()

score_label = Label(root, text="Health Score: ")
score_label.pack()

suggestion_label = Label(root, text="", justify="left")
suggestion_label.pack()

root.mainloop()
