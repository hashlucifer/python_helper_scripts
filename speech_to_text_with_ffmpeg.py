import io,requests,os
from google.cloud import speech
from google.cloud.speech import enums,types

def processAudio():
    client = speech.SpeechClient()
    global audio , config , finalRes
    finalRes = "none"
    with io.open('audio.flac', 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig( encoding=enums.RecognitionConfig.AudioEncoding.FLAC, sample_rate_hertz=48000, language_code='en-US')
    response = client.recognize(config, audio)
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        return '{}'.format(result.alternatives[0].transcript)


def download(url):
    os.system("del /f audio1.mp3")
    print("Starting to download " + url)
    r = requests.get(url, allow_redirects=True)
    open('audio1.mp3', 'wb').write(r.content)
    os.system("del /f audio.flac")
    os.system("\"D:\Harsh\My Work\Python Naruto WS\\reacptcha\\ffmpeg-20180914-6304268-win64-static\\bin\\ffmpeg\" -i audio1.mp3 -ac 1 -sample_fmt s16 -ar 48000 audio.flac")

#download("")
# print(processAudio())
