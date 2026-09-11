import tkinter as tk
from tkinter import ttk
import math

def calculate():
    try:
        W0 = float(entry_initial.get())
        f = float(entry_fraction.get())
        r_percent = float(entry_rate.get())
        years = float(entry_years.get())
        
        r = r_percent / 100
        
        interval_type = interval_var.get()
        
        if interval_type == "6 Months":
            intervals_per_year = 2
        else:
            intervals_per_year = 1
        
        n = int(years * intervals_per_year)
        
        growth_factor = 1 + f * r
        
        Wn = W0 * (growth_factor ** n)
        
        yearly_growth = (growth_factor ** intervals_per_year - 1) * 100
        
        # Reverse Calculations (example target = 2x initial weight)
        target = 2 * W0
        
        required_r = ((target / W0) ** (1/n) - 1) / f
        required_intervals = math.log(target / W0) / math.log(growth_factor)
        
        result_text.set(
            f"--- RESULTS ---\n\n"
            f"Total Intervals: {n}\n"
            f"Growth Factor per Interval: {growth_factor:.6f}\n"
            f"Final Weight: {Wn:.6f}\n"
            f"Effective Yearly Growth: {yearly_growth:.4f}%\n\n"
            f"--- REVERSE ANALYSIS (Target = 2 × Initial) ---\n"
            f"Required Growth Rate per Interval: {required_r*100:.4f}%\n"
            f"Required Intervals to Double: {required_intervals:.2f}\n"
        )
        
    except:
        result_text.set("Please enter valid numeric values.")

# GUI Setup
root = tk.Tk()
root.title("Exponential Weight Growth Calculator")
root.geometry("500x550")

tk.Label(root, text="Initial Weight (W0)").pack()
entry_initial = tk.Entry(root)
entry_initial.pack()

tk.Label(root, text="Fraction Deposited Each Interval (f)").pack()
entry_fraction = tk.Entry(root)
entry_fraction.pack()

tk.Label(root, text="Growth Rate per Interval (%)").pack()
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Number of Years").pack()
entry_years = tk.Entry(root)
entry_years.pack()

tk.Label(root, text="Select Interval Type").pack()
interval_var = tk.StringVar()
interval_dropdown = ttk.Combobox(root, textvariable=interval_var)
interval_dropdown['values'] = ("6 Months", "1 Year")
interval_dropdown.current(0)
interval_dropdown.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.pack(pady=20)

root.mainloop()