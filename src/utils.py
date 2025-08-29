import csv
import os
import json
from datetime import datetime

campos = [
    "Título",
    "Empresa",
    "Localização",
    "Salário",
    "Tipo de Contratação",
    "Modalidade",
    "Link"
]

def _ensure_dir(filename: str):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

def save_to_csv(jobs, filename="data/jobs.csv"):
    _ensure_dir(filename)

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(campos)
        writer.writerows(jobs)

    print(f"Arquivo salvo em {filename}")

def converter_dicionario (jobs):
    jobs_dicionario = []

    for linha in jobs:
        linha = (linha + [""] * len (campos))[: len(campos)]
        jobs_dicionario.append({k: v for k, v in zip(campos, linha)})

    return jobs_dicionario

def salvar_json (jobs, filename="data/jobs.json", indent=2, timestamped=False):
    if timestamped:
        base, ext = os.path.splitext(filename)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{base}_{stamp}{ext}"

    _ensure_dir(filename)

    data = converter_dicionario(jobs)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)

    print(f"JSON salvo em: {filename} ({len(jobs)} vagas)")
