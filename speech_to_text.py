# from time import sleep
# import requests
# api_key = "1f72885e472b49859fec6c63f0082ce9"
# def read_file(filename, chunk_size=5242880):
#         with open(filename, 'rb') as _file:
#             while True:
#                 data = _file.read(chunk_size)
#                 if not data:
#                     break
#                 yield data
# def speech_to_text(filename):
#     headers = {'authorization': api_key}
#     response = requests.post('https://api.assemblyai.com/v2/upload',
#                          headers=headers,
#                          data=read_file(filename))
#     audio_url = response.json()['upload_url']
#     endpoint = "https://api.assemblyai.com/v2/transcript"
#     json = {
#         "audio_url": audio_url,
#     }
#     headers = {
#         "authorization": api_key,
#         "content-type": "application/json"
#     }
#     response = requests.post(endpoint, json=json, headers=headers)
#     tr = response.json()['id']
#     endpoint = f"https://api.assemblyai.com/v2/transcript/{tr}"
#     headers = {
#     "authorization": api_key,
# }
#     response = requests.get(endpoint, headers=headers)
#     st = response.json()
#     while st["status"] != 'completed':
#         sleep(1)
#         st = requests.get(endpoint, headers=headers).json()
#     return st["text"]
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
def speech_to_uzb(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
        audio_data = r.record(source)
    # recognize (convert from speech to text)
        text = r.recognize_google(audio_data,language="uz-UZ")
        print(text)
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text
    
print(get_large_audio_transcription("7601.ogg"))