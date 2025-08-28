Um bot em Python + Selenium que pesquisa vagas no InfoJobs, coleta informações e salva os resultados em CSV automaticamente.

Ideal para estudos de automação web, raspagem de dados e para compor um portfólio de desenvolvedor júnior.


🚀 Funcionalidades

Pesquisa vagas por cargo e cidade.

Navega automaticamente entre páginas de resultados.

Coleta os seguintes dados:

Título da vaga

Empresa

Localização

Link da vaga

Exporta os dados em CSV (data/jobs.csv).

Estrutura modular (bot.py, main.py, utils.py) para facilitar manutenção.

📂 Estrutura do Projeto
job-bot-selenium/
│── src/
│   ├── bot.py        # Classe principal do bot
│   ├── main.py       # Arquivo principal para rodar
│   ├── utils.py      # Funções utilitárias (ex: salvar CSV)
│── data/
│   └── jobs.csv      # Saída dos dados coletados
│── requirements.txt  # Dependências do projeto
│── README.md         # Documentação


🛠️ Tecnologias Utilizadas

Python

Selenium

WebDriver Manager


📦 Instalação e Uso

Clone o repositório:

git clone https://github.com/seu-usuario/job-bot-selenium.git
cd job-bot-selenium/src


Crie um ambiente virtual e instale as dependências:

pip install -r requirements.txt


Execute o bot:

python main.py


O resultado será salvo em:

data/jobs.csv


🧩 Próximos Passos (Roadmap)

 Adicionar coleta de salário, tipo de contratação e modalidade (CLT/PJ, remoto, híbrido).

 Exportar também em JSON e Excel.

 Criar gráficos com pandas/matplotlib (ex: top 5 empresas com mais vagas).

 Interface de linha de comando (CLI) com argparse.

 Deploy simples em Flask ou FastAPI para exibir resultados no navegador.


👨‍💻 Autor

Feito Luan Santos
🔗 LinkedIn - linkedin.com/in/luan-carlos-dos-santos/
 | GitHub - github.com/luansantos-code