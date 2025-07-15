import requests
import csv

# professor token 
TOKEN = "REDACTED"

# my token 
#TOKEN = "REDACTED"

url = "https://www.fflogs.com/api/v2/client"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

query = """
query ReportData($page: Int) {
  reportData {
    reports(zoneID: 68, page: $page) {
      total
      per_page
      current_page
      from
      to
      last_page
      has_more_pages
      data {
        startTime
        endTime
        rankings(playerMetric: bossdps)
      }
    }
  }
}
"""

csv_filename = "cw_data.csv"
fieldnames = ["startTime", "endTime", "rankings"]

def fetch_page(page):
    variables = {"page": page}
    response = requests.post(
        url,
        headers=headers,
        json={"query": query, "variables": variables}
    )
    if response.status_code != 200:
        print(f"Failed on page {page}: {response.status_code}")
        print(response.text)
        return None
    return response.json()

# Fetch the first page to determine total pages
first_page_data = fetch_page(1)
if not first_page_data:
    print("Failed to fetch the first page.")
    exit()

reports_info = first_page_data["data"]["reportData"]["reports"]
last_page = reports_info["last_page"]

with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Process first page
    for report in reports_info["data"]:
        writer.writerow({
            "startTime": report["startTime"],
            "endTime": report["endTime"],
            "rankings": report["rankings"]
        })

    # Process remaining pages
    for page in range(2, last_page + 1):
        page_data = fetch_page(page)
        if not page_data:
            break

        reports_info = page_data["data"]["reportData"]["reports"]
        for report in reports_info["data"]:
            writer.writerow({
                "startTime": report["startTime"],
                "endTime": report["endTime"],
                "rankings": report["rankings"]
            })

print(f"All data written to {csv_filename}")
