import requests
from bs4 import BeautifulSoup
import csv


URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_FILE = "jobs.csv"


def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        print("Failed to fetch the webpage.")
        return None


def scrape_jobs(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    job_elements = soup.find_all("div", class_="card-content")

    jobs = []

    for job in job_elements:
        title = job.find("h2", class_="title")
        company = job.find("h3", class_="company")
        location = job.find("p", class_="location")

        job_data = {
            "Title": title.text.strip() if title else "N/A",
            "Company": company.text.strip() if company else "N/A",
            "Location": location.text.strip() if location else "N/A"
        }

        jobs.append(job_data)

    return jobs


def save_to_csv(jobs, file_name):
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Company", "Location"])
        writer.writeheader()
        writer.writerows(jobs)


def main():
    html_content = fetch_page(URL)

    if not html_content:
        return

    jobs = scrape_jobs(html_content)
    save_to_csv(jobs, OUTPUT_FILE)

    print(f"{len(jobs)} jobs scraped and saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
