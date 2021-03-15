from _card_funcs import *
from cryptography.fernet import Fernet
import argparse
import json


def decrypt(token: bytes, key: bytes) -> bytes:
    text = Fernet(key).decrypt(token).decode('utf-8')
    text = text.split('#')
    return text


class MerryChristmas:

    def __init__(self, key, passcode):

        with open("aig_gl.json", "r") as f:
            aig_p = json.load(f)

        if not key in aig_p:
            print("The key ain't correct :p. But Merry Christmas!")

        else:
            name = aig_p[key]['name']
            pass_code_extracted = decrypt(token=name.encode("utf-8"), key=key)[0]
            if not passcode == pass_code_extracted:
                print("Gotcha :p. But Merry Christmas!")

            else:
                func_to_run = aig_p[key]['func']
                long_text = aig_p[key]['msg']

                func_to_run = decrypt(token=func_to_run.encode("utf-8"), key=key)[0]
                long_text = decrypt(token=long_text.encode("utf-8"), key=key)

                globals()[func_to_run](long_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--passphrase")
    args = parser.parse_args()
    _ = MerryChristmas(key=args.key, passcode=args.passphrase)

