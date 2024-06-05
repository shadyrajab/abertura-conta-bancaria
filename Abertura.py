import pandas as pd
import streamlit as st

from models.instance import SKLEARN_MODEL, X_TRAIN_COLUMNS

st.title("Simulação abertura de conta bancária")

sexo = st.selectbox(label="Qual seu sexo?", options=["M", "F"])
posse_de_veiculo = st.selectbox(label="Você possui veículo?", options=["S", "N"])
posse_de_imovel = st.selectbox(label="Você possui imóvel?", options=["S", "N"])
qtd_filhos = st.number_input(
    label="Você possui filhos? Se sim, quantos?(informe 0 caso não tenha)"
)
tipo_renda = st.selectbox(
    label="Qual seu tipo de renda?",
    options=[
        "Empresário",
        "Assalariado",
        "Servidor público",
        "Pensionista",
        "Bolsista",
    ],
)
educacao = st.selectbox(
    label="Qual seu nível de escolaridade?",
    options=[
        "Médio",
        "Superior incompleto",
        "Superior completo",
        "Fundamental",
        "Pós graduação",
    ],
)
estado_civil = st.selectbox(
    label="Qual seu estado civil?",
    options=["Solteiro", "Casado", "União", "Separado", "Viúvo"],
)
tipo_residencia = st.selectbox(
    label="Qual seu tipo de residência?",
    options=[
        "Casa",
        "Com os pais",
        "Aluguel",
        "Comunitário",
        "Governamental",
        "Estúdio",
    ],
)
idade = st.number_input(label="Qual sua idade?")
tempo_emprego = st.number_input(label="Quanto tempo você tem de emprego?(em meses)")
qt_pessoas_residencia = st.number_input(label="Quantas pessoas moram na sua casa?")
renda = st.number_input(label="Qual sua renda mensal aproximada? ")


X = pd.get_dummies(
    pd.DataFrame(
        [
            {
                "sexo": sexo,
                "posse_de_veiculo": posse_de_veiculo,
                "posse_de_imovel": posse_de_imovel,
                "qtd_filhos": qtd_filhos,
                "tipo_renda": tipo_renda,
                "educacao": educacao,
                "estado_civil": estado_civil,
                "tipo_residencia": tipo_residencia,
                "idade": idade,
                "tempo_emprego": tempo_emprego,
                "qt_pessoas_residencia": qt_pessoas_residencia,
                "renda": renda,
            }
        ]
    )
)

for col in X_TRAIN_COLUMNS:
    if col not in X.columns:
        X[col] = 0


result_sklearn = SKLEARN_MODEL.predict(X)

if result_sklearn == 0:
    st.title("Parabéns, sua solicitação de crédito foi aprovada com sucesso!")
else:
    st.title("Infelizmente não poderemos te oferecer crédito!")