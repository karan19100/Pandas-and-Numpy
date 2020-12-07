import speech_recognition as sr

audio = ('Sample.wav')

r = sr.Recognizer()

with sr.AudioFile(audio) as source:
    audio = r.record(source)

try:
    print('audio file contains  ' + r.recognize_google(audio))
except sr.UnknownValueError:
    print('Google speech recognition could understand audio')
except sr.RequestError:
    print('Could not get the result from Google Speech Recognition')



    


