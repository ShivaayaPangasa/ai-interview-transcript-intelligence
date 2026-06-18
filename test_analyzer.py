from transcript_analyzer import analyze_transcript

transcript = """
Transformers are neural networks.

Transformers use attention mechanisms.

Transformers improve sequence modeling.

Transformers enable parallel processing.
"""

results = analyze_transcript(
    transcript
)

print(results)