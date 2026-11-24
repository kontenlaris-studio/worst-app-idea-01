"""The Worst App Idea Ever Pitched entry: SnoozeDebt, the alarm that fines you."""

import os

JOKE = (
    "Introducing SnoozeDebt: an alarm app that charges your card $5 for every "
    "minute you oversleep, then spends it on coffee for your boss, who is told "
    "exactly why."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {path} ({len(JOKE)} characters)")


if __name__ == "__main__":
    main()
