import os
import platform
import tkinter as tk
from tkinter import filedialog 
from PIL import Image
import ConversionFile 

image_formats = ["JPEG", "PNG", "BMP", "GIF", "TIFF","JPG","WEBP"]

audio_formats = ["MP3", "WAV", "OGG", "FLAC", "AAC"]

doucment_formats = ["DOCX", "PDF", "PLAIN", "HTML"]

class ConverterGui:
    
    def __init__(self):
        
        self.file_buttons = dict()
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

        self.file_type = tk.Label(self.root, text="File Type: None", pady=10)
        self.file_type.pack()
        self.file_type['background'] = '#1f1f1f'

        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame['background'] = '#1f1f1f'

        self.buttonFrame.columnconfigure(0,weight=1)
        self.buttonFrame.columnconfigure(1,weight=1)
        self.buttonFrame.columnconfigure(2,weight=1)

        self.buttonFrame.pack(fill="x")

        self.root.mainloop()

    def select_file(self):
        print(self)
        file_path = filedialog.askopenfilename()
        if file_path:

            file_extension, file_name = os.path.splitext(file_path)
            self.label_file.config(text=f"Selected: {file_extension}")
            self.file_type.config(text= f"File Type: {file_name}" )

            for button in self.file_buttons.values():
                button.destroy()
            self.file_buttons.clear()

            clounmNumber = 0
            rownumber = 0
            
            if file_name[1:].upper() in image_formats:
                print("Image")

                for fmt in image_formats:
                    if file_name[1:].upper() != fmt:
                        try:
                           
                            print(f" - {fmt}: Supported")
                            btn = tk.Button(self.buttonFrame, text = f"Convert to {fmt}" , command= lambda fmt=fmt: ConversionFile.file_convert_image(file_path,fmt) ,highlightbackground = '#1f1f1f' )
                            btn['background'] = '#1f1f1f'
                            btn.grid(row = rownumber,column = clounmNumber, sticky ="nsew")
                            self.file_buttons[fmt] = btn
                            
                            clounmNumber += 1
                            if clounmNumber == 3:
                                clounmNumber = 0
                                rownumber += 1
                           
                           
                        except Exception as e:
                            print(f" - {fmt}: Not supported ({e})")

            if file_name[1:].upper() in audio_formats:

                for fmt in audio_formats:
                    if file_name[1:].upper() != fmt:
                        try:
                            
                            print(f" - {fmt}: Supported")
                            btn = tk.Button(self.buttonFrame, text = f"Convert to {fmt}" , command= lambda fmt=fmt: ConversionFile.file_convert_audio(file_path,fmt,file_extension) ,highlightbackground = '#1f1f1f' )
                            btn['background'] = '#1f1f1f'
                            btn.grid(row = rownumber,column = clounmNumber, sticky ="nsew")
                            self.file_buttons[fmt] = btn
                            
                            clounmNumber += 1
                            if clounmNumber == 3:
                                clounmNumber = 0
                                rownumber += 1
                           
                           
                        except Exception as e:
                            print(f" - {fmt}: Not supported ({e})")
            if file_name[1:].upper() in doucment_formats:

                for fmt in doucment_formats:
                    if file_name[1:].upper() != fmt:
                        try:
                            
                            print(f" - {fmt}: Supported")
                            btn = tk.Button(self.buttonFrame, text = f"Convert to {fmt}" , command= lambda fmt=fmt: ConversionFile.file_convert_documents(file_path,fmt,file_extension) ,highlightbackground = '#1f1f1f' )
                            btn['background'] = '#1f1f1f'
                            btn.grid(row = rownumber,column = clounmNumber, sticky ="nsew")
                            self.file_buttons[fmt] = btn
                            
                            clounmNumber += 1
                            if clounmNumber == 3:
                                clounmNumber = 0
                                rownumber += 1
                           
                           
                        except Exception as e:
                            print(f" - {fmt}: Not supported ({e})")
            
            
        else:
            self.label_file.config(text="No file selected.")
            self.file_type.config(text="File Type: None")


ConverterGui()
