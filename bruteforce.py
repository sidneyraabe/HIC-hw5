import string
import sys

alphabet = string.ascii_lowercase


def shift(text, shift_amount):
    shifted_alphabet = alphabet[shift_amount:] + alphabet[:shift_amount]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.lower().translate(table)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bruteforce.py <text>")
    else:
        for i in range(1, 26):
            print("Shift:", i, shift(sys.argv[1], i))
