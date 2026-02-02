
def _to_ubbi_dubbi(word: str) -> str:
    result = []

    for letter in word:
        if letter in 'aeiou':
            result.append('u')
            result.append('b')
        result.append(letter)

    return "".join(result)

def to_ubbi_dubbi(sentence: str) -> str:
    result = []
    for word in sentence.split(" "):
        result.append(_to_ubbi_dubbi(word))

    return " ".join(result)

def main() -> None:
    assert to_ubbi_dubbi("milk") == "mubilk", to_ubbi_dubbi("milk")
    assert to_ubbi_dubbi("program") == "prubogrubam", to_ubbi_dubbi("program")

    print("pass")

if __name__ == "__main__":
    main()