import os
import platform
import tkinter as tk
from tkinter import filedialog 

class ConverterGui:
    
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Convert Files")
        self.root.geometry("600x400")
        self.root['background'] = '#1f1f1f'

        self.titleLabel = tk.Label(self.root, text = "Convert Files",font=("Arial",18))
        self.titleLabel.pack(padx= 10,pady=10)
        self.titleLabel['background'] = '#1f1f1f'

        self.SelectButtonFile = tk.Button(self.root, text="Select File", command= self.select_file,highlightbackground = '#1f1f1f' )
        self.SelectButtonFile['background'] = '#1f1f1f'
        self.SelectButtonFile.pack(padx= 10,pady=10)

        self.label_file = tk.Label(self.root, text="No file selected.", pady=10)
        self.label_file.pack()
        self.label_file['background'] = '#1f1f1f'

        self.root.mainloop()

    def select_file(self):
        print(self)
        file_path = filedialog.askopenfilename()
        if file_path:
            self.label_file.config(text=f"Selected: {os.path.basename(file_path)}")
        else:
            self.label_file.config(text="No file selected.")


ConverterGui()
