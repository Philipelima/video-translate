

import settings;
import utils;

from download import Download;
from converter import Converter
from transcribe import Transcribe
from translate  import Translator


def run():

    set_url();

    videoPath = video_download()

    converter = Converter(videoPath)
    mp3audio  = converter.mp3_from_video()

    transcribe = Transcribe(settings.ASSEMBLYAPI_KEY)
    transcribe = transcribe.transcribe(mp3audio)
    
    translator =  Translator(transcribe)
    translate  =  translator.to('pt')

    audioPath  =  converter.text_to_audio(translate)
    converter.change_audio_from_video(audioPath)
    
    utils.remove_file(videoPath)
    utils.remove_file(audioPath)

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












