from string import ascii_lowercase, ascii_uppercase
import hashlib
import random
from os import cpu_count
from multiprocessing import Process, current_process, Queue
import itertools
import argparse
import sys

queue = Queue(maxsize=1)


def _parser():
    parser = argparse.ArgumentParser(
        description="Multiprocessing tool for cracking sha256 hash"
    )
    parser.add_argument("-s", "--hash", type=str, help="sha256 raw hash", required=True)
    parser.add_argument(
        "-l", "--length", type=int, help="length of plain text", required=True
    )
    parser.add_argument(
        "-a",
        "--alpha",
        type=str,
        help="alphabet for cracking:\n\t"
        + "l -> letters lowercase\n\t"
        + "n -> numbers\n\t"
        + "u -> letters uppercase\n\t"
        + "ln -> lowercase + numbers\n\t"
        + "un -> uppercase + numbers\n\t"
        + "lu -> lowercase + uppercase\n\t"
        + "lun -> lowercase + uppercase + numbers\n\t"
        + "default -> ln",
        choices=("l", "n", "u", "ln", "un", "lu", "lun"),
        default="ln",
        required=False,
    )
    parser.add_argument(
        "-f", "--first", type=str, help="first letters", default="", required=False
    )
    return parser.parse_args()


def sha256_cracker(hash, length, alpha, first_letters):
    while True:
        plain_text = first_letters + "".join(
            random.choice(alpha) for _ in range(length - len(first_letters))
        )
        if hashlib.sha256(plain_text.encode()).hexdigest() == hash:
            queue.put(f"Found key -> {plain_text}")
            break


if __name__ == "__main__":
    try:
        args = _parser()
        numbers = "0123456789"
        # Each alphabet for each -a option
        alpha_dict = {
            "l": ascii_lowercase,
            "n": numbers,
            "u": ascii_uppercase,
            "ln": ascii_lowercase + numbers,
            "un": ascii_uppercase + numbers,
            "lu": ascii_lowercase + ascii_uppercase,
            "lun": ascii_lowercase + ascii_uppercase + numbers,
        }

        # Check for valid hash
        if len(args.hash) != 64:
            print("Invalid sha256 hash")
            sys.exit()

        # Create list of processes with length of
        # cpu cores
        process_list = [
            Process(
                target=sha256_cracker,
                args=(args.hash, args.length, alpha_dict.get(args.alpha), args.first),
            )
            for _ in range(cpu_count())
        ]

        # Start all
        for process in process_list:
            process.start()
        print("Iterating...")

        # When something appears in queue
        # then stop all
        ret = queue.get()

        for process in process_list:
            process.terminate()

        print(ret)
    except Exception as exc:
        print(f"Error occures: {str(exc)}")
