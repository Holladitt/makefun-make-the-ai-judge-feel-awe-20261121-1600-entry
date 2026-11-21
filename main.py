import os

TEXT = (
    "You sleep in the night train. The wheels find their rhythm. "
    "Clack. A low clack. A sway. Beyond the glass, the valley falls "
    "away, and the river below has been cutting the stone since before "
    "the first road, before the first town. It still cuts, softly, "
    "under the train, under you."
)


def main():
    # Gate: entry.txt must be 1-280 Unicode code points, not only whitespace.
    # v2 targets 275-280 chars: second-person, reader carried asleep.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} chars"
    assert TEXT.strip(), "text must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
