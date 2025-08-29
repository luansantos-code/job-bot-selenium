import csv
import os

def save_to_csv(jobs, filename="data/jobs.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    header = [
        "Título",
        "Empresa",
        "Localização",
        "Salário",
        "Tipo de Contratação",
        "Modalidade",
        "Link"
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(jobs)

    print(f"Arquivo salvo em {filename}")
