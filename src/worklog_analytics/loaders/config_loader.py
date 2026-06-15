import json
from pathlib import Path


def load_json(path: str | Path) -> dict:

    path = Path(path)

    with open( path, "r", encoding="utf-8") as file:
        return json.load(file)