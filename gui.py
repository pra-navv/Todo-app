import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a To-Do")
input_box = PySimpleGUI.InputText(tooltip="Enter Todo", key='todo')
add_button = PySimpleGUI.Button("Add")

window = PySimpleGUI.Window('My To-Do App', layout=[[label],
                            [input_box, add_button]],
                            font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case PySimpleGUI.WINDOW_CLOSED:
            break


window.close()

