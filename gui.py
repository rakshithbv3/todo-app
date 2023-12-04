import functions
import PySimpleGUI as sg

sg.theme("Dark")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter the todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todo(), key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Select an item first", font=('Helvetica', 15))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todo()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Select an item first", font=('Helvetica', 15))


        case ("Exit"):
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])


        case sg.WIN_CLOSED:
            break




window.close()