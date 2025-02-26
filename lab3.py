import tkinter as tk

# Conversion factor from MPG to KM/L
MPG_TO_KML = 0.425143707

def convert_mpg_to_kml(event=None):
    """Converts MPG to KM/L and updates the label."""
    try:
        mpg = float(mpg_entry.get())
        kml = mpg * MPG_TO_KML
        result_label.config(text=f'{kml:.2f} KM/L')
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("MPG to KM/L Converter")

# Create and position the widgets
mpg_label = tk.Label(root, text="Enter MPG:")
mpg_label.grid(row=0, column=0, padx=10, pady=10)

mpg_entry = tk.Entry(root)
mpg_entry.grid(row=0, column=1, padx=10, pady=10)
mpg_entry.bind("<KeyRelease>", convert_mpg_to_kml)  # Trigger conversion on key release

result_label = tk.Label(root, text="Result: KM/L")
result_label.grid(row=1, columnspan=2, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
