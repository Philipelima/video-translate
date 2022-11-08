

import settings;
import utils;

from download import Download;
from converter import Converter
from transcribe import Transcribe
from translate  import Translator

from speech import Speech

def run():

    set_url();

    azure_key = settings.AZURE_SPEECH_SERVICE
    videoPath = video_download()

    converter = Converter(videoPath)
    mp3audio  = converter.mp3_from_video()

    transcribe = Transcribe(settings.ASSEMBLYAPI_KEY)
    transcribe = transcribe.transcribe(mp3audio)
    
    translator =  Translator(transcribe)
    translate  =  translator.to('pt')

    speech  = Speech(azure_key=azure_key, region='brazilsouth')
    speech.text_to_mp3(translate)

    converter.change_audio_from_video('audio.mp3')
    
    utils.remove_file(videoPath)
    utils.remove_file('audio.mp3')

    print(videoUrl+" has been successfully translated");
    

   

def set_url():
    
    url = input("Please, type the video url: ");

    if(utils.is_url(url)):

       global videoUrl;
       videoUrl = url
       
    else:
        print('the url is not valid');


def video_download():

    global videoUrl
    video     = Download(settings.VIDEOS_PATH, videoUrl)

    videoPath = video.dowload()
    return videoPath

run()












