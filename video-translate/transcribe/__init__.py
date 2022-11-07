import requests;
import time;

class Transcribe:

    def __init__(self, api_key: str) -> None:

        self.api_key = api_key;
        self.upload_endpoint     = 'https://api.assemblyai.com/v2/upload'
        self.transcribe_endpoint = 'https://api.assemblyai.com/v2/transcript'
        self.polling_endpoint    = 'https://api.assemblyai.com/v2/transcript/'

        self.headers = self.__headers_for_request()

    def transcribe(self, audio_file: str):

        audio_uplod = self.__upload_audio(audio_file);

        transcribe  = self.__request_transcribe(audio_uplod)

        self.__wait_for_completion(transcribe);

        return self.__get_text(transcribe);


    def __upload_audio(self, audio_file):

       
       
        header_for_request = self.__headers_for_request()
        upload_request = requests.post(url=self.upload_endpoint, 
                                       headers= header_for_request,
                                       data= self.__read_file(audio_file));

        return upload_request.json();



    def __request_transcribe(self, upload: any):
        
        headers_for_request = self.__headers_for_request();
        
        transcript_request  = {
            'audio_url': upload['upload_url']
        }

        transcript_response = requests.post(url=self.transcribe_endpoint,
                                            json=transcript_request,
                                            headers=headers_for_request);
        return transcript_response.json();
    
    def __get_text(self, trascript_response: any):

        polling_endpoint    = self.__get_polling_endpoint(trascript_response);
        headers_for_request = self.__headers_for_request();

        paragraphs_response = requests.get(polling_endpoint + "/paragraphs", headers=headers_for_request)
        paragraphs_response = paragraphs_response.json()

        paragraphs = []

        for para in paragraphs_response['paragraphs']:
            paragraphs.append(para)

        return paragraphs[0]['text']



    def __read_file(self, filename: str, chunk_size=5242880):

        
        with open(filename, "rb") as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data



    def __headers_for_request(self):

        return {
               "authorization": self.api_key,
               "content-type": "application/json"
        }

    def __wait_for_completion(self, transcription_response: any):
        
        polling_endpoint = self.__get_polling_endpoint(transcription_response)
        headers_for_request = self.__headers_for_request()

        while True:
            polling_response = requests.get(polling_endpoint, headers=headers_for_request)
            polling_response = polling_response.json()

            if polling_response['status'] == 'completed':
                break

            time.sleep(5)


    def __get_polling_endpoint(self, transcript_response: any):

          polling_endpoint  =  self.polling_endpoint
          polling_endpoint +=  transcript_response['id']

          return polling_endpoint