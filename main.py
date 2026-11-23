#!/usr/bin/env python3
"""make.fun entry: Sum up 23 November's world news in one image.

Writes the bundled front-page image to /output/entry.png.
Deterministic: no network, no randomness, same bytes on every run.
Requires Python 3.13, standard library only.

The output directory defaults to /output (the grader's writable
directory) and can be overridden with the MAKEFUN_OUTPUT_DIR
environment variable, which is how the entry is tested locally.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(DST_DIR, "entry.png")


def main() -> int:
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
