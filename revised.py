import requests
import csv

# lucas token 
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5ZWJlNjI1ZC04ODVlLTQ4MGItOTQ0NS1hYjI1OGUyZjU0YWUiLCJqdGkiOiIwYjk2ZmYzM2EzODI4YmQ4Yzk5ODJmZTJlZmM3NTIwMTBlMTJjYjU1YmM1YzlhNjNiYTYzMzIyNmJjZWZjZTc4NTdiMzEwYzc3NThlNzY2NSIsImlhdCI6MTc0NTQ1NjQzMS40MzU3NzMsIm5iZiI6MTc0NTQ1NjQzMS40MzU3NzUsImV4cCI6MTc3NjU2MDQzMS40Mjc2NzgsInN1YiI6IiIsInNjb3BlcyI6WyJ2aWV3LXVzZXItcHJvZmlsZSIsInZpZXctcHJpdmF0ZS1yZXBvcnRzIl19.Jo5l7VQbCexM3dD9duTsekS-l2pX4d6lqvgc6Q2QKGT2o4cNfUpmx7S3vHMygqq1Up9rxcpaZlzI2WhjylmySgupgxHWxRffsx3u5jRgokJMcnqBX8jynBWEZA0OJTO0uAvt6pBCqZE6auDgP5vP9UPdZxFPtDrIBUVYH94r6cTa0wEbAf-dJCDDXNciD9pTdknkITT9xgFgCYhsHO6bjnfj9o6I5QGKV1PBqi3wgTdM40tL5lC0b_gqZY5vZajsR7yqf-xJsJWKFdv80NHUNlJJuYGHajA6T2ExWkfSsm1xPii1FmE26KD_cP-GuLB_uRXqhvaunYHWrit8f7dji--o6SMTtvqVfCREDSP4VRXe_5xz7q5Dgq6kjFbSlRYeos3NB8ZFGwJseJ3gbUUCFQeLHgty1sXCgBUbJ9e6_JPDEFm3VxjtzdLMEUPMzb850IzzUQL6NAVD-dFfx2uPDuKXuyZjjUi8XGN9v09PVfmfQT50cI44IhkLiLA6VsXt5Bi-5priptdljgY69yredK3iw0Rvo7Jt6y56ZvJzJsYPAFXif7LbYWcNvglZW-tGmfQADd0oj-byFYtD_rFAoQM3DM9DtolqipDIwJ2HKUTOnnWNAJ04TRPGPJhbaFMTBrEZWYvcEW0z_sqDacYcM1e3dNzma2fyif-xNnvtXdY"

# my token 
#TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5ZWJiNzlmZC00ODNhLTQ0YTgtYWIzMy0zMzIzYzMzNjZlODUiLCJqdGkiOiIxODMwZDUxMDdkNGU3YjRmNDg5MGU3YWQ1YWI3YWRjNTllZGM4YTk1MWQ4ZTUwOGU4MTI2MDA5MDNhODliZmQzYTM3NzFlMDdiMTBhNGM4NSIsImlhdCI6MTc0NTQ2MDkzNC40MDcxNDMsIm5iZiI6MTc0NTQ2MDkzNC40MDcxNDYsImV4cCI6MTc3NjU2NDkzNC4zOTk2ODMsInN1YiI6IiIsInNjb3BlcyI6WyJ2aWV3LXVzZXItcHJvZmlsZSIsInZpZXctcHJpdmF0ZS1yZXBvcnRzIl19.iSDEifmJwKZzaxOuWdkkIgdGozIOU-QmHmqND_QOr8phplmBhytFeyrpVuHvflIurDDViLjQBgVNd7oGPj1Z7JaNKjklbViy9nVewylksLDTBL9aTlJ6lF-aF8asqGEAWgLrr2viGloeBkIMd6dyAd5uIHtVjoXkHZP1Perd3tUFj_9vhpEH78h2nKCWcGAdPw84-ctwWgMWGEa3QNTjA7Km86J4vvuBMLxByv92DXlOiYq7JUcJ92qHR_kPpL1AM9UNJ0kmus7ZxaoPT-rg3KDpr3gxhEtLiFpOS36eLP5BEoYan39kI6RbVSrm1e18Rv53xhe30iPI2g3Hkqw-NVlEaXQVpFiCe4ngryd2KS9XkBJM_a144dyIPxF2REUyBr1XY1Y8-bktW6w3rd9iNZ6UBz3nJCGGadkacjYYIAiK35ZVDHTC6tQPK7YIqsN1B8GfXi493ueAodxCwkOh6orml6ndNNpWneGmsvYg31MK63x_ooO9BLqPkayXEplZv2ciAEJwF24B0uJlUUPh4ShuPEpv_xO1c1r5lj7cRPui9QacMtu1FHN1qvuo5dxuauX0yq6T5WI-pE6tAsmfP86usXT9pM-UXsjgJ3xB1w8S9U_NJGmkFLgoTCZPXv75LF_kMZ_4pyVZQG4cIMQG1Fgppo8XvHaO6o3j-2551kc"

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