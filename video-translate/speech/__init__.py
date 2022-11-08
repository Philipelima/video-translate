import azure.cognitiveservices.speech as speechsdk

class Speech:

    def __init__(self, azure_key: str, region: str) -> None:
        self.azure_key = azure_key
        self.region    = region
    
    def text_to_mp3(self, text: str):

        speech_config = speechsdk.SpeechConfig(subscription=self.azure_key, region=self.region);   
        speech_config.speech_synthesis_voice_name = 'pt-BR-FranciscaNeural'

        speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3)


        filename = 'audio.mp3'

        audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        
        audio = synthesizer.speak_text_async(text).get()

        if audio.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized  audio was saved to [{}]".format(filename))
        elif audio.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = audio.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details)) 