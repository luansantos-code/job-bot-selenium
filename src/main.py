from bot import JobBot
from utils import save_to_csv

def main():
    bot = JobBot()
    jobs = bot.search_jobs("https://www.infojobs.com.br", "Junior", "São Paulo - SP", max_pages=2)

    save_to_csv(jobs)

    bot.fechar()
    print(f"{len(jobs)} vagas salvas em data/jobs.csv")

if __name__ == "__main__":
    main()