import json
from pathlib import Path


def load_json(path: str | Path, optional: bool = False) -> dict | None:

    path = Path(path)

    if not path.exists():
        if optional:
            return None
        raise FileNotFoundError(f"Config file not found: {path}")

    content = path.read_text(encoding="utf-8").strip()

    if not content:
        if optional:
            return None
        raise ValueError(f"Config file is empty: {path}")

    return json.loads(content)
