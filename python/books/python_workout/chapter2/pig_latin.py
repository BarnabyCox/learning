

def _to_pig_latin(word: str) -> str:
    if word[0] in "aeiou":
        return word + "way"
    
    return word[1:] + word[0] + "ay"

def to_pig_latin(sentence: str) -> str:
    words = sentence.split(" ")
    results = []
    for word in words:
        results.append(_to_pig_latin(word))
    
    return " ".join(results)

def main() -> None:
    assert _to_pig_latin("air") == "airway"
    assert _to_pig_latin("eat") == "eatway"
    assert _to_pig_latin("python") == "ythonpay"

    assert to_pig_latin("this is a test translation") == "histay isway away esttay ranslationtay", f"Got ***{to_pig_latin("this is a test translation")}***"

    print("passed!")

if __name__ == "__main__":
    main()