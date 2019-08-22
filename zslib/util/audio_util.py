from pydub import AudioSegment
import numpy as np

DEFAULT_RATE = 44100


def numpy_to_audio_segment(audio_arr, amp=1.0, rate=DEFAULT_RATE, channels=1, sample_width=4):
    audio_arr = audio_arr / (abs(audio_arr).max())
    audio_arr_trans = ((2**(8*sample_width-1)-1) * amp * audio_arr).astype(np.int32)
    audio_segment = AudioSegment(audio_arr_trans.tobytes(),
                                 frame_rate=rate,
                                 sample_width=sample_width,
                                 channels=channels)
    return audio_segment


def audio_segment_to_numpy(seg, th=1.0):
    frame_rate = seg.frame_rate
    seg_arr = np.array(seg.get_array_of_samples())
    seg_arr = th * seg_arr / seg.max_possible_amplitude
    return seg_arr, frame_rate