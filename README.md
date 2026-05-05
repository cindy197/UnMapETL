# UnMap-ETL
 
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Status](https://img.shields.io/badge/Status-Concluído-success)

Projeto desenvolvido para o desafio de seleção **Dev Jr**, com foco na análise de registros de tempo (timesheet) utilizando um pipeline de dados estruturado no padrão **ETL (Extract, Transform, Load)**.
 
---
 
## Sobre o Projeto
 
O **UnMap-ETL** realiza um processo completo de **Extração, Transformação e Carga (ETL)** sobre dados de apontamento de horas. A partir de um arquivo `data.json`, o pipeline filtra, agrupa e analisa registros de tempo gastos por tarefas e funcionários, gerando um relatório consolidado em `result.json`.
 
---
 
## O que o pipeline faz
 
1. **Extração** — Lê os dados brutos do arquivo `data.json`
2. **Transformação**
   - Filtra registros inválidos (registros com `minutes <= 0`)
   - Agrupa minutos por tarefa (`taskId` / `taskName`)
   - Calcula a porcentagem de tempo de cada tarefa em relação ao total
   - Identifica a tarefa mais trabalhada e o top 3
   - Agrupa minutos e tarefas distintas por funcionário (`userId` / `userName`)
   - Identifica o top 3 de funcionários por minutos trabalhados
   - Identifica o funcionário com mais tarefas distintas
3. **Carga** — Exporta os resultados para `result.json`
---
 
## Estrutura do Repositório
 
```
UnMapETL/
├── data.json            
├── result.json          
├── script.py            # Script principal do ETL
├── notebook_etl.ipynb   # Notebook Jupyter com o mesmo pipeline
├── requirements.txt     # Dependências Python
├── Dockerfile           # Imagem Docker para execução
├── docker-compose.yml   # Orquestração com Docker Compose
└── .gitignore
```
 
---
 
## Formato de Entrada (`data.json`)
 
O arquivo de entrada deve conter uma lista de registros com a seguinte estrutura:
 
```json
[
  {
    "taskId": 1,
    "taskName": "Nome da Tarefa",
    "userId": 101,
    "userName": "Nome do Funcionário",
    "minutes": 60
  }
]
```
 
> Registros com `minutes <= 0` são automaticamente ignorados e contabilizados em `ignoredRecords`.
 
---
 
## Formato de Saída (`result.json`)
 
```json
{
  "totalMinutes": 1500,
  "tasks": [...],
  "mostWorkedTask": {
    "taskId": 1,
    "taskName": "Nome da Tarefa",
    "totalMinutes": 300,
    "percentage": "20.00%"
  },
  "top3TasksPercentage": [...],
  "top3Employees": [...],
  "mostDistinctUserOnTasks": {
    "userId": 101,
    "userName": "Nome do Funcionário",
    "distinctTasks": 5,
    "taskIds": [1, 2, 3, 4, 5]
  },
  "ignoredRecords": 2
}
```
 
---
 
## Como Executar
 
Execute o projeto utilizando Docker:
 
```bash
docker compose up --build
```
> O processo é executado automaticamente dentro do container, utilizando o arquivo `script.py` como ponto de entrada.
 
O container irá:
 
1. Instalar as dependências
2. Ler o `data.json`
3. Processar os dados
4. Gerar o `result.json`

---

### Jupyter Notebook

O arquivo `notebook_etl.ipynb` foi incluído como suporte para visualização do pipeline ETL de forma interativa e organizada.

Ele não é necessário para a execução do projeto, mas permite acompanhar cada etapa do processamento (Extração, Transformação e Carga) de forma detalhada.

Para visualizar, abra o notebook em ferramentas como JupyterLab, VS Code ou Google Colab para explorar o fluxo passo a passo.

 
---

## Decisões Técnicas
 
Algumas decisões foram tomadas para garantir consistência, legibilidade e aderência ao desafio:
 
### Uso de Pandas
A biblioteca Pandas foi utilizada por sua eficiência em manipulação de dados tabulares, permitindo:
- Agrupamentos rápidos (`groupby`)
- Transformações declarativas
- Código mais limpo e legível
 
---
 
### Agrupamento por `taskId` e `taskName`
Embora o enunciado mencione agrupamento por `taskId`, o `taskName` também foi incluído para:
- Preservar a informação descritiva da tarefa
- Garantir compatibilidade com o formato de saída esperado
 
---
 
### Ordenação determinística
As ordenações foram implementadas seguindo rigorosamente as regras do desafio:
- Evitar inconsistências entre execuções
- Garantir que o output seja sempre idêntico
 
---
 
### Formatação de percentual
Os percentuais foram formatados como string com duas casas decimais (ex: `10.25%`) para:
- Melhor legibilidade
- Compatibilidade com o padrão esperado no output
 
---
 
### Uso de Docker
A aplicação foi containerizada para:
- Garantir ambiente consistente
- Evitar problemas de dependência
- Facilitar execução em qualquer máquina
 
---
 
### Separação Script vs Notebook
- `script.py`: execução oficial da aplicação
- `notebook_etl.ipynb`: apoio visual e exploração
 
## Tecnologias Utilizadas
 
| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.11+ | Linguagem principal |
| Pandas | latest | Manipulação e análise de dados |
| Docker | — | Containerização |
| Jupyter Notebook | — | Exploração interativa |
 
---
 
## Dependências
 
```
pandas
```
 
> Instale via `pip install -r requirements.txt`
 
---

## Destaques do Projeto
 
Este projeto demonstra habilidades importantes para atuação como desenvolvedora na área de dados e backend:
 
- ✔ Estruturação de pipeline ETL
- ✔ Manipulação e análise de dados com Pandas
- ✔ Aplicação de regras de negócio reais
- ✔ Organização e clareza de código
- ✔ Containerização com Docker
- ✔ Geração de saída determinística (reprodutibilidade)
 
---
 
## Possíveis Melhorias Futuras
 
- Transformar o script em uma API (FastAPI)
- Adicionar testes automatizados (pytest)
- Persistência em banco de dados
- Dashboard para visualização dos resultados
- Pipeline automatizado (CI/CD)
 
---
 
## Sobre este Projeto
 
Este projeto foi desenvolvido como parte de um desafio técnico, com foco em demonstrar:
 
- Capacidade de resolver problemas com dados
- Organização de código e boas práticas
- Conhecimento em ferramentas modernas (Docker, Pandas)
 
---

## Autora
 
Desenvolvido por **Cindy Pessoa**  
🔗 [GitHub](https://github.com/cindy197)
