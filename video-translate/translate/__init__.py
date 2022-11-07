from deep_translator import MyMemoryTranslator

class Translator:

    def __init__(self, text: str):
        self.text = text
    
    def to(self, language: str):
        
        translate = MyMemoryTranslator(source='en', target=language).translate(self.text)
        return translate