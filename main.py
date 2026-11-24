#!/usr/bin/env python3
import os

PART_A = "fix: I broke prod at 3 AM and blamed the intern; "
PART_B = "there is no intern, I hallucinated him in standup"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PART_A + PART_B)

if __name__ == "__main__":
    main()
