#!/usr/bin/env python3
"""Entry for make.fun news-image-20261117: sum up 17 November 2026's world
news in one image.

The program writes one image to /output/entry.png. The image is bundled
with the repository as entry.png (a 1024x1024 PNG front page: masthead,
Shenzhen hero illustration, and six headline stories from Tuesday
17 November 2026). This program copies it byte for byte, so two runs
always produce identical output. No network, no randomness, no clock.
"""
import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, IMAGE_NAME)
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    if size != os.path.getsize(src):
        raise RuntimeError(f"copied size {size} != source size {os.path.getsize(src)}")
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
