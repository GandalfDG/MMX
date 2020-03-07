import librosa as lr
from beats import *

audio1 = lr.core.load('test/clicktrack.ogg', duration=2)
audio2 = lr.core.load('test/clicktrack.ogg', duration=1, offset=.1)

print(match_beats(audio1[0], audio2[0], 10))
