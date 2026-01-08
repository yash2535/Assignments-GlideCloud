import re

def chunk_text(
    text: str,
    max_chars: int = 300,
    overlap_sentences: int = 1
):
    # 1. Split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        sentence_length = len(sentence)

        # If adding sentence exceeds max size, finalize chunk
        if current_length + sentence_length > max_chars:
            chunks.append(" ".join(current_chunk))

            # Keep overlap sentences for context
            current_chunk = current_chunk[-overlap_sentences:]
            current_length = sum(len(s) for s in current_chunk)

        current_chunk.append(sentence)
        current_length += sentence_length

    # Add remaining chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
