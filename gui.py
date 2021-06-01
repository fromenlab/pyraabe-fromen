import os
import sys
import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
from extensions import entry
from extensions import __info__

vector_components = 'x', 'y', 'z'

class MessageRedirector(object):
    def __init__(self, text_output):
        self.output = text_output
    
    def write(self, string):
        self.output.configure(state = 'normal')
        self.output.insert(tk.END, string)
        self.output.configure(state = 'disabled')
        self.output.see('end')

    def flush(self):
        pass

def make_vector_form(root, fields):
    try:
        vector_default = get_vector_default()
    except:
        vector_default = [0,0,-1]

    entries = []
    for field in fields:
        row = tk.Frame(root)
        label = tk.Label(row, text=field, anchor='center')
        entry = tk.Entry(row, width = 5, justify=tk.CENTER)
        row.grid(column = fields.index(field), row=1, padx=5, pady=5)
        label.grid(column=0, row=0, padx=5, sticky=tk.EW)
        entry.grid(column=0, row=1, padx=5, sticky=tk.EW)
        entry.insert(0, vector_default[fields.index(field)])
        entries.append((field, entry))
    return entries

def select_file():
    file_path = filedialog.askopenfilename(filetypes = [('STL Files', '*.stl')])
    entry_file.delete(0,tk.END)
    entry_folder.delete(0, tk.END)
    entry_file.insert(0, file_path)
    entry_folder.insert(0, os.path.dirname(file_path))

def select_folder():
    folder_path = filedialog.askdirectory()
    entry_folder.delete(0,tk.END)
    entry_folder.insert(0, folder_path)

def set_vector_default():
    print(os.getcwd())
    try:
        write_vector_default()
    except:
        print('Error setting default vector')
    else:
        print('Default gravity vector:\n ', get_vector_default())

def get_vector_default():
    with open('pyraabe_vector_default.csv') as csv_file:
            default_vector_read = csv.reader(csv_file, delimiter=',')
            vector_default = next(default_vector_read)
            return vector_default

def write_vector_default():
    # Check coordinate input
    x = entry_vector[0][1].get()
    y = entry_vector[1][1].get()
    z = entry_vector[2][1].get()

    with open('pyraabe_vector_default.csv', mode='w') as csv_file:
        default_vector_write = csv.writer(csv_file, delimiter = ',')
        default_vector_write.writerow([x,y,z])

def show_about():
    messagebox.showinfo("About", open("resources/about.md", "r").read())

def show_usage():
    messagebox.showinfo("Usage", open("resources/usage.md", "r").read())

def show_license():
    messagebox.showinfo("License", open("resources/LICENSE", "r").read())

def show_output():
    if (root.winfo_height() < 250):
        w = root.winfo_width()
        h = 400
        root.geometry(f'{w}x{h}')

def run():
    # Check file input
    file_path = entry_file.get()
    folder_path = entry_folder.get()
    # Check coordinate input
    x = entry_vector[0][1].get()
    y = entry_vector[1][1].get()
    z = entry_vector[2][1].get()

    # Window should be large enough to show console output
    show_output()

    if (not file_path or not os.path.splitext(file_path)[1] == '.stl'):
        msg = 'Note:\n Please select a .stl file'
        print(msg)
        return
    elif (not folder_path):
        msg = 'Note:\n Please set an output folder'
        print(msg)
        return
    elif ((x == '' or y == '' or z =='')):
        msg = 'Note:\n Please set a 3D gravity vector'
        print(msg)
        return
    else:
        # Run PyRaabe
        entry.main(file_path, folder_path, [int(x), int(y), int(z)], bool_extruded.get())
        return

if __name__ == '__main__':
    # Set up window
    root = tk.Tk()
    root.title('PyRaabe GUI by Fromen Lab')
    root.geometry('250x230+200+200')
    root.minsize(200, 230)
    root.iconbitmap('resources/pyraabe-fromen-icon.ico')
    root.columnconfigure(0,weight=1)

    # Set menus
    menu = tk.Menu(root)

    menu_file = tk.Menu(menu, tearoff = 0)
    menu.add_cascade(label = 'File', menu = menu_file)
    menu_file.add_command(label = 'Choose input file', command = select_file)
    menu_file.add_command(label = 'Choose output folder', command = select_folder)

    menu_edit = tk.Menu(menu, tearoff = 0)
    menu.add_cascade(label = 'Edit', menu = menu_edit)
    menu_edit.add_command(label = 'Set default vector', command = set_vector_default)
    
    menu_help = tk.Menu(menu, tearoff = 0)
    menu.add_cascade(label = 'Help', menu = menu_help)
    menu_help.add_command(label = 'Usage', command = show_usage)
    menu_help.add_separator()
    menu_help.add_command(label = 'About', command = show_about)
    menu_help.add_command(label = 'License', command = show_license)

    root.config(menu = menu)

    
    # Set frames for layout
    frame_paths = tk.Frame(root)
    frame_paths.grid(sticky = tk.EW)
    frame_paths.columnconfigure(1, weight=1)

    frame_vector = tk.Frame(root)
    frame_vector.grid(sticky=tk.EW)
    frame_vector_components = tk.Frame(frame_vector)
    frame_vector_components.grid(column = 0, row = 1)

    frame_run = tk.Frame(root)
    frame_run.grid(sticky=tk.EW)
    frame_run.columnconfigure(0, weight=1)
    frame_run.columnconfigure(1, weight=1)

    frame_stdout = tk.Frame(root)
    frame_stdout.grid(sticky=tk.NSEW)
    frame_stdout.columnconfigure(0, weight=1)
    frame_stdout.rowconfigure(0,weight=1)
    root.rowconfigure(3, weight=1)

    frame_info = tk.Frame(root)
    frame_info.grid(sticky=(tk.S, tk.EW))
    frame_info.columnconfigure(0, weight=1)

    # Path input fields
    button_file = tk.Button(frame_paths, text = 'Input File', command = select_file)
    button_file.grid(row = 0, column = 0, padx=5, pady=5, sticky=tk.EW)
    entry_file = tk.Entry(frame_paths)
    entry_file.grid(row=0, column=1, padx = 5, pady=5, sticky=tk.EW)

    button_folder = tk.Button(frame_paths, text = 'Output Folder', command = select_folder)
    entry_folder = tk.Entry(frame_paths)
    button_folder.grid(row = 1, column = 0, padx=5, pady=5, sticky=tk.EW)
    entry_folder.grid(row=1, column=1, padx = 5, pady=5, sticky=tk.EW)

    # Vector input
    label_gravity = tk.Label(frame_vector, text = 'Gravity vector (integer values only)')
    label_gravity.grid(column=0, row = 0, padx=5, columnspan=2)
    
    entry_vector = make_vector_form(frame_vector_components, vector_components)
    frame_vector.columnconfigure(0, weight=1)

    # Run options
    bool_extruded = tk.BooleanVar()
    checkbox_extruded = tk.Checkbutton(frame_run, text='Extruded Inlet', variable=bool_extruded)
    checkbox_extruded.grid(column=0, row = 0, padx=5, sticky=tk.E)

    button_run = tk.Button(frame_run, text = 'Run', command = run, padx=10, pady=10)
    button_run.grid(column=1, row = 0, padx=10, pady=10, sticky=tk.W)

    # Configure stdout scroll view
    scrolledtext_console = scrolledtext.ScrolledText(frame_stdout, height = 1)
    scrolledtext_console.grid(padx=5, pady=5, sticky=tk.NSEW)
    sys.stdout = MessageRedirector(scrolledtext_console)

    # Bottom info
    bar_status = tk.Label(frame_info, text=('GUI by Fromen Lab - v{}'.format(__info__.__version__)), bd=1, relief=tk.SUNKEN, anchor='w')
    # bar_status = tk.Label(frame_info, text=('GUI by Fromen Lab - v{}'.format(0)), bd=1, relief=tk.SUNKEN, anchor='w')
    bar_status.grid(sticky=(tk.S, tk.EW))

    # Run GUI
    root.mainloop()