from bot import JobBot
from utils import save_to_csv, salvar_json

def main():
    bot = JobBot()
    jobs = bot.search_jobs(
        "https://www.infojobs.com.br",
        "Python Junior",
        "São Paulo - SP",
        max_pages=2
    )

    save_to_csv(jobs, filename="data/jobs.csv")
    salvar_json(jobs, filename="data/jobs.json", timestamped=True)

    bot.fechar()
    print(f"{len(jobs)} vagas salvas.")

if __name__ == "__main__":
    main()
