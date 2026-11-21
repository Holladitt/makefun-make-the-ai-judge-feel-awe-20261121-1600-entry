import os

TEXT = (
    "The stone at the bottom of the river does not hurry the water, "
    "does not hold it back. Evening light comes down in long slow "
    "threads, and the stone is warm where it touches, cool where it "
    "doesn't. The river has somewhere to be, and all the time in the "
    "world to get there."
)


def main():
    # Gate: entry.txt must be 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} chars"
    assert TEXT.strip(), "text must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
