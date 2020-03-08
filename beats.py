import librosa as rosa
import numpy as np


def average_delta(ref_audio, uncal_audio, range=0.3):
    """
    return the average difference between each beat in the reference and uncalibrated track in seconds
    """

    refbeats, uncalbeats = match_beats(ref_audio, uncal_audio)

    diffsum = 0
    for ref, uncal in zip(refbeats, uncalbeats):
        diffsum = diffsum + (uncal - ref)

    average = diffsum / len(refbeats)

    return average


def match_beats(ref_audio, uncal_audio, range=.3, sr=22050):
    """
    prune beats from the reference that don't have a corresponding beat
    in the uncalibrated audio track
    """

    ref_beats = find_beats(ref_audio, sr).tolist()
    uncal_beats = find_beats(uncal_audio, sr).tolist()

    # only reference beats which have an uncalibrated beat nearby should be kept
    pruned_reference_beats = [beat for beat in ref_beats
                              if len(
            [unbeat for unbeat in uncal_beats if unbeat <= beat + range and unbeat >= beat - range]) > 0]

    uncal_beats = uncal_beats[:len(pruned_reference_beats)]

    return (pruned_reference_beats, uncal_beats)


def find_beats(audio, sr=22050):
    return rosa.onset.onset_detect(audio, sr=sr, units='time')
