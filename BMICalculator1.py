import tkinter as tk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt

class BMICal():
    def __init__(self, root):
        self.root = root
        self.root.title('BMI CALCULATOR')
        self.root.geometry('300x200')

        self.weight_label = tk.Label(root, text='Weight(KG):')
        self.weight_label.pack()
        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        self.height_label = tk.Label(root, text='Height in (CM):')
        self.height_label.pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        self.calculate_button = tk.Button(root, text='Calculate BMI:', command=self.calculate_bmi)
        self.calculate_button.pack()
        self.viewData_button = tk.Button(root, text='View Historical Data', command=self.view_data)
        self.viewData_button.pack()
        self.analyze_button = tk.Button(root, text='Analyze BMI', command=self.analyze_bmi)
        self.analyze_button.pack()

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            height_in_meters = height / 100

            bmi = weight / (height_in_meters ** 2)

            with open("bmi_data.csv", "a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([weight, height, bmi])

            if bmi < 18.5:
                result = "Underweight"
            elif 18.5 <= bmi < 25.0:
                result = "Normal Weight"
            elif 25.0 <= bmi < 30.0:
                result = "Overweight"
            else:
                result = "Obesity"
            messagebox.showinfo('BMI Result', f"Your BMI is {bmi:.2f} and you are {result}")
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid weight and height value')

    def view_data(self):
        try:
            with open("bmi_data.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)
                messagebox.showinfo('Historical Data', '\n'.join([f"Weight: {row[0]}, Height: {row[1]}, BMI: {row[2]}" for row in data]))
        except FileNotFoundError:
            messagebox.showerror('Error', 'No historical data found')

    def analyze_bmi(self):
        try:
            with open("bmi_data.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)
                bmi_values = [float(row[2]) for row in data]
                plt.hist(bmi_values, bins=5)
                plt.xlabel('BMI')
                plt.ylabel('Frequency')
                plt.title('BMI Distribution')
                plt.show()
        except FileNotFoundError:
            messagebox.showerror('Error', 'No historical data found')

root = tk.Tk()
bmi_cal = BMICal(root)
root.mainloop()