"""Byte-for-byte copy entry.png from the script's directory into MAKEFUN_OUTPUT_DIR (default /output), creating that directory if missing."""

import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
