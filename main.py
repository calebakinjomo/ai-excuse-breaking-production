"""One-line AI excuse for breaking production — make.fun bounty entry."""

import os

ENTRY = "It worked on my machine — which, for the record, is the same machine that just took production down."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
