"""Variant C - flags first, menu as fallback.

Behaves like a real command-line tool when given arguments, and drops into the
interactive menu when run bare. This is the shape most Unix tools have.

    python variant_c_argparse.py -e -c caesar -k 3 "attack at dawn"
    python variant_c_argparse.py -d -c vigenere -k lemon "lxfopv ef rnhr"
    echo "secret" | python variant_c_argparse.py -e -c xor -k hunter2
    python variant_c_argparse.py                 # interactive menu
"""

import argparse
import sys

from decrypt import Decryptor
from encrypt import Encryptor

CIPHERS = {
    "caesar": ("Caesar", int, "shift amount, e.g. 3"),
    "vigenere": ("Vigenere", str.lower, "keyword, letters only"),
    "xor": ("XOR", str, "any string"),
}


def run(mode, cipher, text, key):
    """Single place where the actual work happens, shared by both paths."""
    engine = Encryptor() if mode == "encrypt" else Decryptor()
    _, parse_key, _ = CIPHERS[cipher]
    if cipher != "xor":
        text = text.lower()
    return getattr(engine, cipher)(text, parse_key(key))


def build_parser():
    parser = argparse.ArgumentParser(
        prog="cipher",
        description="Encrypt or decrypt text with a classical cipher.",
        epilog="Run with no arguments for an interactive menu.",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("-e", "--encrypt", action="store_true", help="encrypt the input")
    mode.add_argument("-d", "--decrypt", action="store_true", help="decrypt the input")
    parser.add_argument("-c", "--cipher", choices=CIPHERS, help="which cipher to use")
    parser.add_argument("-k", "--key", help="the key (see --help for each cipher)")
    parser.add_argument("text", nargs="?", help="text to process; reads stdin if omitted")
    return parser


# --- interactive fallback -------------------------------------------------


def pick(prompt, options):
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        answer = input("  > ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        print(f"  Enter a number from 1 to {len(options)}.")


def interactive():
    print("cipher tool - ctrl-c to quit")
    while True:
        mode = pick("Mode:", ["encrypt", "decrypt"])
        cipher = pick("Cipher:", list(CIPHERS))
        noun = "plaintext" if mode == "encrypt" else "ciphertext"

        text = input(f"  {noun}: ")
        hint = CIPHERS[cipher][2]
        while True:
            key = input(f"  key ({hint}): ").strip()
            try:
                CIPHERS[cipher][1](key)
                break
            except ValueError:
                print(f"  Needs a {hint}.")

        print(f"\n  -> {run(mode, cipher, text, key)}")


def main():
    parser = build_parser()
    args = parser.parse_args()

    # No flags at all means the user wants the menu.
    if not (args.encrypt or args.decrypt or args.cipher or args.key or args.text):
        interactive()
        return

    if not (args.encrypt or args.decrypt):
        parser.error("choose one of -e/--encrypt or -d/--decrypt")
    if not args.cipher:
        parser.error("--cipher is required, one of: " + ", ".join(CIPHERS))
    if args.key is None:
        parser.error("--key is required")

    text = args.text if args.text is not None else sys.stdin.read().rstrip("\n")
    if not text:
        parser.error("no text given on the command line or stdin")

    mode = "encrypt" if args.encrypt else "decrypt"
    try:
        print(run(mode, args.cipher, text, args.key))
    except ValueError:
        parser.error(f"bad key for {args.cipher}: needs a {CIPHERS[args.cipher][2]}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)