# video-translate

![python](https://img.shields.io/static/v1?label=Python&labelColor=07a0f8&message=v3.8.10&color=000000&logo=python&logoColor=ffffff&style=flat-square)
![python](https://img.shields.io/static/v1?label=pytube&labelColor=dd3838&message=v12.1.0&color=000000&logo=python&logoColor=ffffff&style=flat-square)
![](https://img.shields.io/static/v1?label=AssemblyAI&labelColor=7335da&message=+v2&color=000000&logo=&logoColor=ffffff&style=flat-square)
![Python](https://img.shields.io/static/v1?label=deep_translator&labelColor=7335da&message=+v1.9.1&color=000000&logo=Python&logoColor=ffffff&style=flat-square)

Have you ever thought about translate a YouTube video? That is the idea for this project. 

## How's it works?

Consuming a set of python modules and a text-to-speech api from AssemblyAI, the video-translate system downloads the video with the pytube module based on its url, which must be entered by the user. 

When the download is finished, the pymovie module is called to create an .mp3 file from the downloaded .mp4. 

When the file creation is finished, the api for AssemblyAI's text-to-speech service is requested, sending the .mp3 file as data, the api returns a string containing what is said in the audio.
