import re
from collections import Counter
from typing import Dict

def countFrequencies(text: str) -> Dict[str, int]:
    text = text.lower()
    textClean = re.sub(r"[^\w\s]", "", text, flags=re.UNICODE)
    words = textClean.split()
    return dict(Counter(words))

if __name__ == "__main__":
    userInput = input("Introduce una frase o párrafo:\n").strip()
    if not userInput:
        print("No se ha introducido texto.")
    else:
        frequencies = countFrequencies(userInput)
        print("\nPalabra -> Frecuencia")
        for word in sorted(frequencies):
            print(f"{word} -> {frequencies[word]}")
