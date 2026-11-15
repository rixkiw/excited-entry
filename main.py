"""Copy entry.png byte for byte into the output directory (MAKEFUN_OUTPUT_DIR or /output)."""
# ai-excited-01 entry

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
