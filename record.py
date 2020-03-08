import sounddevice as sd


def record(duration=10, sr=22050):
    recording = sd.rec(duration * sr, sr, channels=1)
    sd.wait()
    return recording
