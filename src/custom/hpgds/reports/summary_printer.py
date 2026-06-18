def print_summary(title, summary):
    print(f"\n=========== {title} ===========\n")

    for category, hours in summary.items():
        print(f"{category}: " f"{hours:.2f}h")
