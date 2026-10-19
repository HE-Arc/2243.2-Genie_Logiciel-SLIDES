"""Render the *.plantuml files of this folder to SVG in the parent folder (medias/).

Usage:
    python render.py                  # every *.plantuml file
    python render.py etat_garde ...   # only the given diagrams (names without extension)
"""

import sys
import urllib.error
import urllib.request
from pathlib import Path

SERVER = "https://yk-hes-ete.k8s-ext.ing.he-arc.ch/svg"
SOURCE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SOURCE_DIR.parent


def render(source: Path) -> bool:
    request = urllib.request.Request(
        SERVER,
        data=source.read_bytes(),
        headers={"Content-Type": "text/plain; charset=utf-8"},
        method="POST",
    )
    target = OUTPUT_DIR / f"{source.stem}.svg"
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            target.write_bytes(response.read())
    except urllib.error.HTTPError as error:
        # The server answers 400 with an SVG describing the syntax error: keep it to look at, but report the failure
        target.write_bytes(error.read())
        print(f"FAILED {source.name} (HTTP {error.code}, see {target.name})")
        return False
    print(f"ok     {source.name} -> {target.name}")
    return True


def main() -> int:
    names = sys.argv[1:]
    sources = [SOURCE_DIR / f"{name}.plantuml" for name in names] if names else sorted(SOURCE_DIR.glob("*.plantuml"))
    missing = [source.name for source in sources if not source.exists()]
    if missing:
        print("Not found: " + ", ".join(missing))
        return 1
    results = [render(source) for source in sources]
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
