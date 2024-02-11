import tkinter
import customtkinter
import convert

# function to Convert the Temperature only when the Button is clicked
def convert_temperature():
    converted_temp = convert.CelsiusToFahr(temp.get())
    temp_output.delete(1.0, customtkinter.END)  # Clear previous output
    temp_output.insert(customtkinter.END, converted_temp) # insert new Converted Temp into Textbox

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("400x260")
app.title("Temperature Converter (Celsius to Fahrenheit)")

# adding UI Elements
title = customtkinter.CTkLabel(app, text = "Insert Temperature in Celsius:")
title.pack(padx=10, pady=10)

# Temperature Input
temp = tkinter.DoubleVar()
temp_input = customtkinter.CTkEntry(app, width=350, height=40, textvariable=temp)
temp_input.pack(padx=10, pady=10)

# Convert Button
convert_btn = customtkinter.CTkButton(app, text="Convert", command=convert_temperature)
convert_btn.pack(padx=10, pady=10)

title2 = customtkinter.CTkLabel(app, text = "Converted to Fahrenheit :")
title2.pack(padx=10, pady=10)

# Display Converted Temperature
temp_output = customtkinter.CTkTextbox(app, height=40, width=350)
temp_output.pack(padx=10, pady=10)

# Insert initial text into Text Widget
temp_output.insert(customtkinter.END, "")

# run app
app.mainloop()