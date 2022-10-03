
import tkinter as tk
import os
import tempfile, base64, zlib
from tkinter import filedialog
from tkinter import font
from objects.Template import Template
from PIL import Image, ImageTk # Install by using: pip install Pillow

# Create a window
root = tk.Tk()

# Change Tkinter feather Icon to a custom one
root.iconbitmap(r"logo.ico")

# App Name
root.title('Odin')

# Global variables declarations
location = tk.StringVar()
error_message = tk.Label(root)
file_message = tk.Text(root)
txt_box = tk.Text(root)

# Create Canvas
canvas = tk.Canvas(root, width=500, height=470)
root.resizable(False, False)
canvas.grid(columnspan=3, rowspan=20)

logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
# logo_label.image = logo
logo_label.grid(columnspan=3, row=0)

# create a label for the project name
instructions = tk.Label(root, 
    text="Enter the project name:")
instructions.grid(column=0, row=1)

# create an input field for the project name
project_name = tk.Entry(root, font="Consolas")
project_name.grid(column=1, row=1)
project_types = [
    "Basic", 
    "Advanced"
]

# Create a dropdown menu for the project type
project_type = tk.StringVar(root)
project_type.set("Select Project Type")
project_type_menu = tk.OptionMenu(root, project_type, *project_types)

# Add the dropdown menu to the window
project_type_menu.grid(column=1, row=2)


# Create Template
def CreateTemplate(*args):    
    # Check if the project name is empty
    global error_message
    global txt_box
    if project_name.get() == "":
        # if it is, display an error message
        error_message.destroy()
        error_message = tk.Label(root, text="Please enter a project name", font="Consolas")
        error_message.place(x=210, y=215)

    # Check if the project location is empty
    elif location.get() == "":
        # if it is, display an error message
        error_message.destroy()
        error_message = tk.Label(root, text="Please enter a project folder", font="Consolas")
        error_message.place(x=210, y=215)
    else:
        # Basic Template
        if project_type.get() == "Basic":
            projName = project_name.get()
            Template("basic", projName, location)

            # Text Box with folder/projName info
            txt_box = tk.Text(root,
                height = 8,
                width = 45)
            txt_box.insert(tk.INSERT, 'Location:\n' + dir_name + '\nProject Name:\n' +
                                projName + '\nAll files created Successfully!')
            txt_box.configure(state='disabled')
            txt_box.place(x=22.5, y=300)

        # Advanced Template
        else:
            projName = project_name.get()
            Template("advanced", projName, location)

            # Text Box with folder/projName info
            txt_box = tk.Text(root, font="Consolas",
                            height = 8,
                            width = 45)
            txt_box.insert(tk.INSERT, 'Location:\n' + dir_name + '\nProject Name:\n' +
                                projName + '\nAll files created Successfully!')
            txt_box.configure(state='disabled')
            txt_box.place(x=22.5, y=300)

# Link function to change dropdown
project_type.trace('w', CreateTemplate)


def SetDirectory():
    global dir_name
    dir_name = filedialog.askdirectory()
    location.set(dir_name)
    print(dir_name)

# Add directory button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text,command=lambda:SetDirectory(),
    bg="#0052cc", fg="#fff")
browse_text.set("Select Directory")
browse_btn.grid(column=0, row=2)

# Path Description
# location = tk.StringVar()
path_label_desc = tk.Label(text='Current Folder Path:')
path_label_desc.place(x=22.5, y=250)

# Folder Path
folder_path_label = tk.Label(master=root, textvariable=location)
folder_path_label.place(x=22.5, y=270 )

# TextBox Creation
txt_box = tk.Text(root,
                   height = 8,
                   width = 45)
txt_box.configure(state='disabled')
txt_box.place(x=22.5, y=300)

# start the main loop
root.mainloop()