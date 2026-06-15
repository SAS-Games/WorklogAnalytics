def print_summary(title: str, summary: dict[str, float]):

    print()
    print(f"=========== {title} ===========")
    print()

    for key, hours in sorted(summary.items()):
        print(f"{key}: {hours:.2f}h")