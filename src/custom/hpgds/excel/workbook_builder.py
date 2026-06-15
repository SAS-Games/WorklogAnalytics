from openpyxl import Workbook

from custom.hpgds.reports.executive_summary import build_executive_summary
from custom.hpgds.reports.studio_support_breakdown import build_studio_support_breakdown
from custom.hpgds.reports.validation_summary import build_validation_summary


def generate_workbook(worklogs, validation_issues, studio_groups_config, output_file):

    workbook = Workbook()

    # Executive Summary
    worksheet = workbook.active
    worksheet.title = "Executive Summary"
    worksheet.append(["Category", "Hours"])

    executive_summary = build_executive_summary(worklogs, studio_groups_config)

    for category, hours in executive_summary.items():
        worksheet.append([category, hours])

    # Studio Breakdown
    worksheet = workbook.create_sheet("Studio Breakdown")
    worksheet.append(["Studio", "Hours"])

    studio_breakdown = build_studio_support_breakdown(worklogs, studio_groups_config)

    for studio, hours in studio_breakdown.items():
        worksheet.append([studio, hours])

    # Validation Summary
    worksheet = workbook.create_sheet("Validation Summary")
    worksheet.append(["Issue", "Hours"])
    
    validation_summary = build_validation_summary(validation_issues)

    for issue, hours in sorted(validation_summary.items()):
        worksheet.append([issue, hours])

    workbook.save(output_file)
