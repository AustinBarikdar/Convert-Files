from PIL import Image
from pydub import AudioSegment
import pypandoc
import time

result = None

def file_convert_image(self,file_path,file_type):
    try:
        image = Image.open(file_path)
        image.save(f"{file_path[0:file_path.rfind("/") + 1]}Output.{file_type.lower()}", file_type)

        self.results.config(text = "Successful!")
        time.sleep(2)
        self.results.config(text = "")
    except:
        self.results.config(text = "Error!")
        time.sleep(2)
        self.results.config(text = "")


def file_convert_audio(self,file_path,file_type,file_name):
    try:
        audio = AudioSegment.from_file(file_path)
        audio.export(str(file_name) + "." + file_type.lower(), format= file_type.lower())

        self.results.config(text = "Successful!")
        time.sleep(2)
        self.results.config(text = "")
    except:
        self.results.config(text = "Error!")
        time.sleep(2)
        self.results.config(text = "")
def file_convert_documents(self,file_path,file_type,file_name):

    extra_args = ['--pdf-engine=xelatex'] 
    try:
        print(str(file_name) + "." + file_type.lower())
        pypandoc.convert_file(file_path, file_type.lower(), outputfile= (str(file_name) + "." + file_type.lower()),extra_args= extra_args)
        self.results.config(text = "Successful!")
        time.sleep(2)
        self.results.config(text = "")
    except:
        self.results.config(text = "Error!")
        time.sleep(2)
        self.results.config(text = "")


    
    