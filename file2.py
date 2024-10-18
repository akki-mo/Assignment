from google.cloud import speech_v1p1beta1 as speech
import os

def transcribe_audio(audio_path):
    client = speech.SpeechClient()
    with open(audio_path, 'rb') as audio_file:
        audio_data = audio_file.read()

    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='en-US',
    )

    response = client.recognize(config=config, audio=audio)
    transcription = ''
    for result in response.results:
        transcription += result.alternatives[0].transcript
    return transcription
