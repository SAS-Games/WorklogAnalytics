from custom.hpgds.reports.executive_summary import (build_executive_summary)
from custom.hpgds.reports.studio_support_breakdown import ( build_studio_support_breakdown)
from custom.hpgds.reports.validation_summary import (build_validation_summary)

def run_hpgds_reports(worklogs, validation_issues, studio_groups_config):

    # HP-GDS Effort Summary
    executive_summary = (build_executive_summary(worklogs, studio_groups_config))
    print("\n=========== HP-GDS EFFORT SUMMARY ===========\n")
    for category, hours in (executive_summary.items()):
        print(f"{category}: "f"{hours:.2f}h")

    
    # Studio Support Breakdown
    studio_breakdown = (build_studio_support_breakdown(worklogs, studio_groups_config))
    print("\n=========== STUDIO SUPPORT BREAKDOWN ===========\n")
    for project, hours in(studio_breakdown.items()):
        print(f"{project}: "f"{hours:.2f}h")

    
    # Validation Summary
    validation_summary = (build_validation_summary(validation_issues))
    print("\n=========== VALIDATION SUMMARY ===========\n")
    for reason, hours in sorted(validation_summary.items()):
        print( f"{reason}: " f"{hours:.2f}h")