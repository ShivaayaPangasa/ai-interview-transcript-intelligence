import os

os.environ["PATH"] += os.pathsep + r"C:\Users\Shivaaya\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin"

import os
import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(
        duration=10,
        sample_rate=16000,
        output_file="temp_audio/answer.wav"
):

    print("Recording started...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    os.makedirs("temp_audio", exist_ok=True)

    write(
        output_file,
        sample_rate,
        audio
    )

    print(f"Audio saved to {output_file}")

import whisper


def transcribe_audio(
        audio_file="temp_audio/answer.wav"
):
    """
    Transcribes audio using Whisper.
    """

    print("Loading Whisper model...")

    model = whisper.load_model("base")

    print("Transcribing audio...")

    result = model.transcribe(audio_file)

    transcript = result["text"]

    print("\nTranscript:")
    print(transcript)

    return transcript