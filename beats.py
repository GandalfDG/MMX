import librosa as rosa
import numpy as np


def match_beats(ref_audio, uncal_audio, range, sr=22050):
    """
    prune beats from the reference that don't have a corresponding beat
    in the uncalibrated audio track
    """
    
    ref_beats = find_beats(ref_audio, sr).tolist()
    uncal_beats = find_beats(uncal_audio, sr).tolist()

    # only reference beats which have an uncalibrated beat nearby should be kept
    pruned_reference_beats = []
    for ref in ref_beats:
        for uncal in uncal_beats:
            if uncal <= ref + range and uncal >= ref - range:
                pruned_reference_beats.append(ref)
                break

    return(pruned_reference_beats, uncal_beats)


def find_beats(audio, sr=22050):
    return rosa.onset.onset_detect(audio, sr=sr)