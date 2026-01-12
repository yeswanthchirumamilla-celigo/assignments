import pandas as pd


def analyze_employee_performance(file_name):
    df = pd.read_csv(file_name)

    df["PerformanceScore"] = pd.to_numeric(df["PerformanceScore"], errors="coerce")
    df = df.dropna(subset=["PerformanceScore"])

    department_avg = df.groupby("Department")["PerformanceScore"].mean()

    return department_avg


def generate_report(summary):
    print("\n--- Employee Performance Summary ---")
    for department, avg_score in summary.items():
        print(f"Department: {department}, Average Score: {avg_score:.2f}")


def main():
    file_name = "employee_performance.csv"
    summary = analyze_employee_performance(file_name)
    generate_report(summary)


if __name__ == "__main__":
    main()
