from whisper_module import (
    record_audio,
    transcribe_audio
)

record_audio()

transcript = transcribe_audio()

print("\nFinal Transcript:")
print(transcript)