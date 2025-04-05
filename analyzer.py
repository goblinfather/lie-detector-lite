import librosa
import numpy as np

def analyze_audio(filepath):
    y, sr = librosa.load(filepath, sr=None, duration=3.0)

    if len(y) < sr * 1:
        raise ValueError("녹음이 너무 짧습니다.")

    energy = np.mean(np.abs(y))
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))

    score = 0
    if energy > 0.15:
        score += 1
    if zcr > 0.1:
        score += 1

    confidence = int((score / 2) * 100)
    result = "lie" if confidence >= 60 else "truth"

    return {
        'result': result,
        'confidence': confidence,
        'energy': round(energy, 3),
        'zcr': round(zcr, 3)
    }
