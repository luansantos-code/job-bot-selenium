import csv
import os

def save_to_csv(data, filename="data/jobs.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Título", "Empresa", "Local", "Link"])
        writer.writerows(data)