from PIL import Image
from pydub import AudioSegment


result = None

def file_convert_image(file_path,file_type):
    print(file_path,file_type)
    image = Image.open(file_path)
    image.save(f"output.{file_type.lower()}", file_type)

    global result
    result = "Worked"

def file_convert_audio(file_path,file_type,file_name):
    print(file_path,file_type,file_name)

    audio = AudioSegment.from_file(file_path)
    print(str(file_name) + "." + file_type.lower(),file_type.lower())
    audio.export(str(file_name) + "." + file_type.lower(), format= file_type.lower())

    global result
    result = "Worked"
    