from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def pick_excel_file(title: str) -> Path:

    root = Tk()
    root.withdraw()

    file_path = askopenfilename(
        title=title, filetypes=[("Excel Files", "*.xlsx *.xls"), ("All Files", "*.*")]
    )

    root.destroy()

    if not file_path:
        raise RuntimeError(f"No file selected: {title}")

    return Path(file_path)


def pick_output_file() -> Path:

    root = Tk()
    root.withdraw()

    file_path = asksaveasfilename(
        title="Save Report As",
        defaultextension=".xlsx",
        filetypes=[("Excel Files", "*.xlsx")],
    )

    root.destroy()

    if not file_path:
        raise RuntimeError("No output file selected")

    return Path(file_path)
