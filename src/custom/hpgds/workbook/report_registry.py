from custom.hpgds.workbook.definitions import ReportDefinition
from custom.hpgds.workbook.writers import write_summary


def build_report_registry(final_summary, final_breakdown, validation_summary):
    return [
        ReportDefinition(
            sheet_name="Effort Summary",
            data=final_summary,
            writer=write_summary,
        ),
        ReportDefinition(
            sheet_name="Studio Support Summary",
            data=final_breakdown,
            writer=write_summary,
        ),
        ReportDefinition(
            sheet_name="Validation Summary",
            data=validation_summary,
            writer=write_summary,
        ),
    ]