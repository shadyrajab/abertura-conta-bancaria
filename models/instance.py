import pickle
from sklearn.pipeline import Pipeline

def load_sklearn_model():
    with open("models/pickle/model_sklearn.pkl", "rb") as file:
        model = pickle.load(file)
    return model


SKLEARN_MODEL: Pipeline = load_sklearn_model()


X_TRAIN_COLUMNS = [
    "qtd_filhos",
    "idade",
    "tempo_emprego",
    "qt_pessoas_residencia",
    "renda",
    "sexo_F",
    "sexo_M",
    "posse_de_veiculo_N",
    "posse_de_veiculo_S",
    "posse_de_imovel_N",
    "posse_de_imovel_S",
    "tipo_renda_Assalariado",
    "tipo_renda_Bolsista",
    "tipo_renda_Empresário",
    "tipo_renda_Pensionista",
    "tipo_renda_Servidor público",
    "educacao_Fundamental",
    "educacao_Médio",
    "educacao_Pós graduação",
    "educacao_Superior completo",
    "educacao_Superior incompleto",
    "estado_civil_Casado",
    "estado_civil_Separado",
    "estado_civil_Solteiro",
    "estado_civil_União",
    "estado_civil_Viúvo",
    "tipo_residencia_Aluguel",
    "tipo_residencia_Casa",
    "tipo_residencia_Com os pais",
    "tipo_residencia_Comunitário",
    "tipo_residencia_Estúdio",
    "tipo_residencia_Governamental",
]
