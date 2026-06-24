from dataclasses import dataclass


@dataclass
class Report:
    title: str
    worksheet_name: str | None = None

    render_console: bool = True
    render_excel: bool = True


@dataclass
class SummaryReport(Report):
    data: dict[str, float] | None = None


@dataclass
class MatrixReport(Report):
    data: dict | None = None
    columns: list[str] | None = None
    row_header: str = "Row"


@dataclass
class TableReport(Report):
    rows: list[dict] | None = None