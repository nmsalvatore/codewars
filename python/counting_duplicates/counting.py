from collections import Counter

def duplicate_count(text: str) -> int:
    counter = Counter(text.lower())
    return sum(1 for v in counter.values() if v > 1)
