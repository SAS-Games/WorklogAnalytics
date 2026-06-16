from openpyxl import load_workbook
from custom.hpgds.reports.executive_summary import (build_executive_summary,)
from custom.hpgds.reports.studio_support_breakdown import (build_studio_support_breakdown,)
from custom.hpgds.reports.validation_summary import (build_validation_summary,)


def write_summary(worksheet, summary, start_row=2):

    row = start_row

    for category, hours in summary.items():
        worksheet.cell(row=row, column=1, value=category)
        worksheet.cell(row=row, column=2, value=hours)

        row += 1

    # Clear remaining template rows
    for clear_row in range(row, 101):
        worksheet.cell(row=clear_row, column=1, value=None)
        worksheet.cell(row=clear_row, column=2, value=None)


def generate_workbook(worklogs, validation_issues, studio_groups_config, output_file):

    workbook = load_workbook("input/report_template.xlsx")

    # =================================
    # Executive Summary
    # =================================

    worksheet = workbook["Executive Summary"]
    executive_summary = build_executive_summary(worklogs, studio_groups_config)

    write_summary(worksheet, executive_summary)

    # =================================
    # Studio Breakdown
    # =================================

    worksheet = workbook["Studio Breakdown"]
    studio_breakdown = build_studio_support_breakdown(worklogs, studio_groups_config)

    write_summary(worksheet, studio_breakdown)

    # =================================
    # Validation Summary
    # =================================

    worksheet = workbook["Validation Summary"]
    validation_summary = build_validation_summary(validation_issues)

    write_summary(worksheet, validation_summary)

    workbook.save(output_file)
