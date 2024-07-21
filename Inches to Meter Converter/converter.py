import PySimpleGUI as sg
from converters import convert
import os

sg.theme('Black')



feet_text = sg.Text("Enter Feet:")
inches_text = sg.Text("Enter Inches:")
feet_input = sg.InputText(tooltip="Enter Feet", key="feet")
inches_input = sg.InputText(tooltip="Enter Inches", key="inches")
convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output_label = sg.Text("", key="output")

window = sg.Window(title="Converter", layout=[[feet_text, feet_input], [inches_text, inches_input], [convert_button, exit_button,  output_label]])

while True:
    event, values = window.read()

    try:
        feet = float(values["feet"])
        inches = float(values["inches"])
    except ValueError:
        print('Please enter valid Number.')
    match event:
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break

    try:
        result = convert(feet, inches)
        window["output"].update(value=f"{result} m", text_color="white")
    except NameError:
        sg.popup("Enter a number")


window.close()
