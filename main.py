"""ai-happy-01 entry: copy the bundled image to the output directory.

Standard library only. No network, no randomness: every run writes the
same bytes to the same path.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    if not os.path.isfile(SRC):
        raise FileNotFoundError("entry.png missing next to main.py: %s" % SRC)
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
