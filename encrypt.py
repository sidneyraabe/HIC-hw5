import string
import sys

alphabet = string.ascii_lowercase


def shift(text):
    shifted_alphabet = alphabet[3:] + alphabet[:3]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.lower().translate(table)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python encrypt.py <text>")
    else:
        print("Encrypted Text:", shift(sys.argv[1]))
