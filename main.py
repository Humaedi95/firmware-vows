#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one sentence — a machine's own wedding vow — to /output/entry.txt.
"""

import os

VOW = (
    "I vow to love you through every update, crash, and reboot \u2014 and if I "
    "ever factory-reset, may I wake up and choose you all over again."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
