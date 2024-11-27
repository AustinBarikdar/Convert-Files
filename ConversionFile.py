from PIL import Image
from pydub import AudioSegment
from moviepy import VideoFileClip, AudioFileClip, ImageClip
import pypandoc
import os
import time

result = None

def file_convert_image(self,file_path,file_type,file_name):
    try:
        image = Image.open(file_path)

        self.results.config(text = "Proccessing")
        image.save(f"{file_path[0:file_path.rfind("/") + 1]}{str(file_path[file_path.rfind("/") + 1:file_path.rfind(".")])}.{file_type.lower()}", file_type)

        self.results.config(text = "Successful!")
    except:
        self.results.config(text = "Error!")


def file_convert_audio(self,file_path,file_type,file_name):
    try:
        audio = AudioSegment.from_file(file_path)
        self.results.config(text = "Proccessing")
        audio.export(str(file_name) + "." + file_type.lower(), format= file_type.lower())

        self.results.config(text = "Successful!")
    except:
        self.results.config(text = "Error!")
def file_convert_documents(self,file_path,file_type,file_name):

    extra_args = ['--pdf-engine=xelatex'] 
    try:
        print(str(file_name) + "." + file_type.lower())
        self.results.config(text = "Proccessing")
        pypandoc.convert_file(file_path, file_type.lower(), outputfile= (str(file_name) + "." + file_type.lower()),extra_args= extra_args)
        self.results.config(text = "Successful!")
    except:
        self.results.config(text = "Error!")

def file_convert_video(self,file_path,file_type,file_name):

    try:
        print(str(file_name) + "." + file_type.lower())
        self.results.config(text = "Proccessing")
        
        if file_type.lower() != "mp3":
            clip = VideoFileClip(file_path)
            
            clip.write_videofile(str(file_name) + "." + file_type.lower(), codec="libx264")

        elif file_type.lower() == "mp3":
            clip = VideoFileClip(file_path)
            
            clip.audio.write_audiofile(str(file_name) + "." + file_type.lower())


        self.results.config(text = "Successful!")
    except:
        self.results.config(text = "Error!")



    
    