from worklog_analytics.reports.report_writer import write_report


def _default_resolver(workbook, report):

    sheet_name = (report.worksheet_name or report.title)
    if sheet_name in workbook.sheetnames:
        return workbook[sheet_name]

    return workbook.create_sheet(sheet_name)


def write_reports(workbook, reports, worksheet_resolver=None):

    worksheet_resolver = (worksheet_resolver or _default_resolver)

    for report in reports:
        if not report.render_excel:
            continue
        worksheet = worksheet_resolver(workbook, report)
        write_report(worksheet, report)