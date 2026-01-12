LOG_FILE = "sample.log"
OUTPUT_FILE = "log_summary.txt"


def read_log_file(file_name):
    try:
        with open(file_name, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("Error: Log file not found.")
        return []


def count_log_levels(log_lines):
    log_counts = {
        "INFO": 0,
        "ERROR": 0,
        "DEBUG": 0
    }

    for line in log_lines:
        if "INFO" in line:
            log_counts["INFO"] += 1
        elif "ERROR" in line:
            log_counts["ERROR"] += 1
        elif "DEBUG" in line:
            log_counts["DEBUG"] += 1

    return log_counts


def write_summary_to_file(summary, file_name):
    with open(file_name, "w") as file:
        for level, count in summary.items():
            file.write(f"{level}: {count}\n")


def display_summary(summary):
    for level, count in summary.items():
        print(f"{level}: {count}")


def main():
    log_lines = read_log_file(LOG_FILE)

    if not log_lines:
        return

    summary = count_log_levels(log_lines)
    display_summary(summary)
    write_summary_to_file(summary, OUTPUT_FILE)


if __name__ == "__main__":
    main()
