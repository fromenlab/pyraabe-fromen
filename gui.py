import tkinter as tk
from tkinter import filedialog
from pyraabe_3199c8b import pyraabe
import os
import entry

fields = 'x', 'y', 'z'

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='center')
        ent = tk.Entry(row)
        row.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.TOP)
        ent.pack(side=tk.BOTTOM, expand=tk.NO, fill=tk.X)
        entries.append((field, ent))
    return entries

def selectfile():
    file_path = filedialog.askopenfilename(filetypes = [('STL Files', '*.stl')])
    entry_file.delete(0,tk.END)
    entry_folder.delete(0, tk.END)
    entry_file.insert(0, file_path)
    entry_folder.insert(0, os.path.dirname(file_path))

def selectfolder():
    folder_path = filedialog.askdirectory()
    entry_folder.delete(0,tk.END)
    entry_folder.insert(0, folder_path)

def run():
    # Check file input
    file_path = entry_file.get()
    folder_path = entry_folder.get()

    if (not file_path or not os.path.splitext(file_path)[1] == '.stl'):
        bar_status.config(text = "Please select a .stl file")
        return

    # Check coordinate input
    x = ents[0][1].get()
    y = ents[1][1].get()
    z = ents[2][1].get()

    if (not (x or y or z)):
        bar_status.config(text = "Please set a 3D gravity vector")
        return

    # Run PyRaabe
    entry.main(file_path, folder_path, [int(x), int(y), int(z)])
    bar_status.config(text = "GUI by Fromen Lab")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("PyRaabe v" + pyraabe.__version__)
    # root.geometry('200x200+200+200')
    
    # Set frames for layout
    frame_input_path = tk.Frame(root)
    frame_input_path.pack(side=tk.TOP, fill=tk.X)

    frame_output_path = tk.Frame(root)
    frame_output_path.pack(side=tk.TOP, fill=tk.X)

    frame_vector = tk.Frame(root)
    frame_vector.pack(side=tk.TOP, fill=tk.X)

    frame_run = tk.Frame(root)
    frame_run.pack(side=tk.TOP, fill=tk.X)

    frame_status = tk.Frame(root)
    frame_status.pack(side=tk.TOP, fill=tk.X)

    # Add labels
    label_gravity = tk.Label(frame_vector, text = 'Gravity vector (integer values only)')
    label_gravity.pack(side = tk.TOP, padx=5, anchor='w')

    # Populate fields
    ents = makeform(frame_vector, fields)

    # Configure buttons, text, labels
    button_file = tk.Button(frame_input_path, text = 'Input File', command = selectfile)
    button_file.pack(side = tk.LEFT, padx=5, pady=5)
    entry_file = tk.Entry(frame_input_path)
    entry_file.pack(side = tk.RIGHT, padx=5, pady=5, expand = tk.YES, fill = tk.X)

    button_folder = tk.Button(frame_output_path, text = 'Output Folder', command = selectfolder)
    button_folder.pack(side = tk.LEFT, padx=5, pady=5)
    entry_folder = tk.Entry(frame_output_path)
    entry_folder.pack(side = tk.RIGHT, padx=5, pady=5, expand = tk.YES, fill = tk.X)

    button_run = tk.Button(frame_run, text = 'OK', command = run)
    button_run.pack(side = tk.RIGHT, padx=10, pady=10)

    bar_status = tk.Label(frame_status, text='GUI by Fromen Lab', bd=1, relief=tk.SUNKEN, anchor='w')
    bar_status.pack(side=tk.BOTTOM, fill=tk.X)

    # Run GUI
    root.mainloop()