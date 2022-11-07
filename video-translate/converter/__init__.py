from gtts import gTTS
from moviepy.editor import *


class Converter:

    def __init__(self,  file: any) -> None:
        self.file = file
    

    def mp3_from_video(self):

        videoFile = VideoFileClip(self.file)
        videoFile.audio.write_audiofile('audio.mp3')

        return 'audio.mp3'

    def text_to_audio(self, text: str):

        textToSpeech = gTTS(text=text, tld='com.br', lang='pt');
        textToSpeech.save('audio.mp3');

        return 'audio.mp3'


    def change_audio_from_video(self, audioPath: str):

        audioFile =  AudioFileClip(audioPath)

        videoFile =  VideoFileClip(self.file).set_audio(audioFile)
        videoFile.write_videofile("final.mp4")