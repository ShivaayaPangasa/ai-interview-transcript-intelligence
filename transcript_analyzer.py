import re
import numpy as np


def analyze_transcript(transcript):

    words = re.findall(
        r"\b\w+\b",
        transcript.lower()
    )

    total_words = len(words)

    unique_words = len(set(words))

    if total_words == 0:
        vocabulary_richness = 0
    else:
        vocabulary_richness = (
            unique_words /
            total_words
        )

    sentences = re.split(
        r"[.!?]+",
        transcript
    )

    sentences = [
        s.strip()
        for s in sentences
        if s.strip()
    ]

    sentence_lengths = []

    for sentence in sentences:

        sentence_words = re.findall(
            r"\b\w+\b",
            sentence
        )

        sentence_lengths.append(
            len(sentence_words)
        )

    if len(sentence_lengths) > 1:
        sentence_consistency = float(
            np.std(sentence_lengths)
            )
       
    else:
        sentence_consistency = 0

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "vocabulary_richness": round(
            vocabulary_richness,
            3
        ),
        "sentence_consistency": round(
            sentence_consistency,
            3
        )
    }