import pandas as pd


def remove_outliers(df: pd.DataFrame, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


def agroup_columns(df: pd.DataFrame):
    df["educacao"] = df["educacao"].replace(
        ["Superior completo", "Superior incompleto", "Pós graduação"],
        "Alta Escolaridade",
    )

    df["educacao"] = df["educacao"].replace(
        ["Médio", "Fundamental"], "Baixa Escolaridade"
    )

    df["tipo_renda"] = df["tipo_renda"].replace(
        ["Assalariado", "Servidor público"], "Assalariado"
    )

    df["estado_civil"] = df["estado_civil"].replace(
        ["Viúvo", "Separado", "Solteiro"], "Solteiro"
    )
    df["estado_civil"] = df["estado_civil"].replace(
        ["Casado", "União"], "Compromissado"
    )
