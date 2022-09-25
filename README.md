# subtitle_generator
Automatically generates subtitles in srt format for a video via google's speech_recognition and googletrans

---
## Purpose

The goal of this project is to have a home brew version of an automatic subtitle generator, where the audio is Language A and the text is Language B.

The project uses [speech_recognition](https://github.com/Uberi/speech_recognition#readme) as the tool to identify audio speech.

For the translation, [googletrans](https://github.com/ssut/py-googletrans) is used.  
Due to a bug in some versions of googletrans, a pip installation of version **googletrans==3.1.0a0** is required.

The project requires **ffmpeg**.

Check out the [subtitles.yml](subtitles.yml) file.

---
## How to

So far, this is WIP.  

The notebook first extracts the audio into a WAV file, for easiness of handing.  
The the silences are detected and the non-silent moments are stored into the local directory **audio-chunks**.  
Non-silent time intervals are detected with a manual threshold which is still not detected automatically and must be adjusted case by case.  
Conversion of non-silent timestamps is done into a __hh:mm:ss,SSS__ format, used in .srt files.