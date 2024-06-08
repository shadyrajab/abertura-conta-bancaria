# Simulação de Abertura de Conta Bancária

Este projeto é uma aplicação web interativa desenvolvida em Python usando Streamlit para simular o processo de abertura de uma conta bancária. O objetivo é fornecer uma interface amigável onde os usuários podem inserir suas informações pessoais e, com base nesses dados, determinar se a conta pode ser aprovada.

## Funcionalidades

- Entrada de dados do usuário:
  - Idade
  - Tempo de emprego (em meses)
  - Quantidade de pessoas na residência

- Classificação de crédito:
  - Predição se o usuário receberá crédito baseado em um modelo preditivo treinado.
  - Exibição do resultado da predição na interface.

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [pandas](https://pandas.pydata.org/)
- [imbalanced-learn (SMOTE)](https://imbalanced-learn.org/stable/)

## Como Executar o Projeto

### Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório para sua máquina local:

```sh
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
python -m venv venv
pip install -r requirements.txt
streamlit run Abertura.py
```

abertura-conta-bancaria/
│
├── pages/
│   └── Escoragem.py   # Página de escoragem e predição
├── models/
│   └── instance.py   # Leitura do modelo usando pickle
├── test/
│   └── model_scoring.ftr   # Arquivo para testar a predição dos dados
│
├── Abertura.py             # Arquivo principal da aplicação
├── requirements.txt   # Arquivo de dependências do projeto
└── README.md          # Documentação do projeto
└── Criando o Modelo.ipynb   # Notebook para construção e treinamento do modelo preditivo

# Construção do Modelo Preditivo

O modelo preditivo utilizado na aplicação foi construído no notebook modelo_credito.ipynb. Fique a vontade para ler o notebook e entender todo o processo!

Para testar a funcionalidade de predição dos dados, um arquivo de teste model_scoring.ftr foi disponibilizado na pasta test/. Esse arquivo pode ser utilizado para verificar a precisão da predição do modelo antes de aplicá-lo a novos dados.


[streamlit-Abertura-2024-06-05-17-06-00.webm](https://github.com/shadyrajab/projeto-final-ebac/assets/65933264/887cb654-dc6a-47b4-97f7-be2a7650e9e7)
