

import settings;
import utils;

from download import Download;
from converter import Converter
from transcribe import Transcribe
from translate  import Translator

from speech import Speech


class VideoTranslate:

    def __init__(self, settings: any) -> None:
        self.settings = settings
    

    def translate_from_url(self):

        self.__get_url_from_video()

        video_path = self.__download_video()
        mp3_file   = self.__get_mp3_from_mp4(video_path)
        
        transcribe = self.__get_text_from_audio(mp3_file)
        translated = self.__translate_text(transcribe, 'pt')

        self.__translated_to_speech(translated)
        self.__change_audio_from_video_to_translated(video_path)

        final_message = "[{}] has been successfully translated"
        print(final_message.format(self.video_url))


    def __get_url_from_video(self) -> None:

        url = input("Please, type the video url: ");

        if(utils.is_url(url)):
             self.video_url = url
        else:
             print('the url is not valid');



    def __download_video(self) -> str:

        video_path = self.settings.VIDEOS_PATH

        if(self.video_url):

             video      = Download(video_path, self.video_url)
             video_path = video.dowload()

             return video_path

            

    def __get_mp3_from_mp4(self, video_path: str) -> str:

        converter  = Converter(video_path);
        return converter.mp3_from_video()



    def __get_text_from_audio(self, file_mp3: str) -> str:
        
        assemblyAi_key = self.settings.ASSEMBLYAPI_KEY

        transcribe = Transcribe(assemblyAi_key)
        return transcribe.transcribe(file_mp3)


    def __translate_text(self, text_to_translate: str, language: str) -> str:

        translator = Translator(text_to_translate)
        return translator.to(language)


    def __translated_to_speech(self, text: str) -> None:

         azure_key = self.settings.AZURE_SPEECH_SERVICE

         speech  = Speech(azure_key, 'brazilsouth')
         speech.text_to_mp3(text)


    def __change_audio_from_video_to_translated(self, video_path: str) -> None:

         converter = Converter(video_path)
         converter.change_audio_from_video('audio.mp3')



video_translate = VideoTranslate(settings)

video_translate.translate_from_url()
