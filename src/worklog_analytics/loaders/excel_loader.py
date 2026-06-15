from pathlib import Path

import pandas as pd


def load_excel(file_path: str | Path) -> pd.DataFrame:
    """
    Load Jira Excel export.
    """

    return pd.read_excel(file_path)