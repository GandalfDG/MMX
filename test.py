import librosa as lr
from beats import *

audio1 = lr.core.load('test/clicktrack.ogg', duration=10)
audio2 = lr.core.load('test/clicktrack.ogg', duration=5, offset=.1)

print(match_beats(audio1[0], audio2[0], .2))

print(average_delta(audio1[0], audio2[0]))

