```markdown
# Exercício de ETL com Apache Airflow

## Descrição

Este exercício tem como objetivo implementar um processo de ETL (Extração, Transformação e Carga) utilizando o Apache Airflow. O Airflow é uma plataforma de gerenciamento de workflows que permite programar e monitorar pipelines de dados de forma eficiente.

## Objetivos do Exercício

- **Familiarização com o Airflow:** Compreender como o Airflow funciona, incluindo a criação de DAGs (Directed Acyclic Graphs).
- **Implementação de ETL:** Desenvolver um pipeline de ETL que extraia dados de uma fonte, os transforme conforme as necessidades do negócio e os carregue em um destino.
- **Práticas de Melhoria Contínua:** Aprender a monitorar e gerenciar a execução de jobs, identificando pontos de falha e implementando melhorias.

## Estrutura do Projeto

```
/airflow-etl-exercise
│
├── dags/
│   └── etl_dag.py       # Definição do DAG de ETL
│
├── logs/                # Logs gerados pelo Airflow
│
├── requirements.txt     # Dependências do projeto
│
└── docker-compose.yml    # Arquivo de configuração do Docker Compose
```

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Configuração do Ambiente

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/blcsilva/EtlCase
   cd airflow-etl-exercise
   ```

2. **Configure as variáveis de ambiente** no arquivo `docker-compose.yml` se necessário.

3. **Inicie os serviços do Airflow:**

   ```bash
   docker-compose up -d
   ```

4. **Acesse a interface web do Airflow** em `http://localhost:8080`. Use as credenciais abaixo:

   - **Usuário:** admin
   - **Senha:** admin

5. **Crie um usuário administrador (opcional):**

   Execute o seguinte comando para criar um usuário administrador:

   ```bash
   docker-compose exec airflow-webserver airflow users create \
       --username admin \
       --firstname Admin \
       --lastname User \
       --role Admin \
       --email admin@example.com
   ```

## Executando o DAG

1. **Ative o DAG** `etl_dag` na interface do Airflow.
2. **Inicie a execução** manualmente clicando no botão "Trigger DAG".

## Estrutura do DAG

O DAG `etl_dag.py` implementa o seguinte fluxo de trabalho:

1. **Extração:** Conectar-se a uma fonte de dados (por exemplo, API ou banco de dados) e extrair informações relevantes.
2. **Transformação:** Processar e transformar os dados extraídos conforme as necessidades do negócio (limpeza, agregação, formatação, etc.).
3. **Carga:** Armazenar os dados transformados em um destino apropriado (por exemplo, banco de dados, arquivo CSV).

## Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir issues ou pull requests. Todas as sugestões e melhorias são bem-vindas!

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## Contato

Para dúvidas ou mais informações, entre em contato:

- **Email:** bruno.tasc@gmail.com
```

