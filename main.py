import os

TEXT = (
    "You ride on your father's shoulders through the dusk field. "
    "His hands hold your ankles. A cricket. A low cricket. Cut hay. "
    "Your sister holds his hand. The path has carried a hundred "
    "fathers home, and the hills were old when the first fence was "
    "built. He walks on. You are home."
)


def main():
    # Gate: entry.txt must be 1-280 Unicode code points, not only whitespace.
    # v3 targets 275-280 chars: second-person, father carries the reader,
    # sister as second presence, path of a hundred fathers as deep time.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} chars"
    assert TEXT.strip(), "text must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
