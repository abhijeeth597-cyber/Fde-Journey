def count_word (path):
    with open(path) as f:
        text = f.read()
        words = text.lower().split()
        count = {}
    for w in words:
        if w in count:
            count[w] = count[w] + 1
        else:
            count[w] = 1
    return count
if __name__ == "__main__":
        counts = count_word("sample.txt")
        top = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        for word, n in top[:3]:
            print(f"{word}:{n}")