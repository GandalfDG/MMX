import librosa as lr
import librosa.display
import matplotlib.pyplot as plt
from beats import *

audio1 = lr.core.load('test/clicktrack.ogg', duration=5, offset=0.1)
audio2 = lr.core.load('test/clicktrack.ogg', duration=10, offset=0)

print(match_beats(audio1[0], audio2[0], .2))

print(average_delta(audio1[0], audio2[0]))

plt.figure()
plt.subplot(3,1,1)
librosa.display.waveplot(audio1[0],audio1[1])
plt.title("monophonic")
