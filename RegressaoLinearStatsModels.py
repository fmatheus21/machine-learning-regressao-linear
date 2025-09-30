import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import seaborn as sns  # Importa a biblioteca seaborn para visualização de dados
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para gráficos


# Será analisado a coluna 'mpg' (milhas por galão) em função da coluna 'wt' (peso do carro)
class RegressaoLinearStatsModels:

    @staticmethod
    def executar():
        base = pd.read_csv(
            "files/mt_cars.csv"
        )  # Lê o arquivo CSV com os dados dos carros
        base = base.drop(
            columns=["Unnamed: 0"]
        )  # Remove a coluna desnecessária 'Unnamed: 0'
        corr = base.corr()  # Calcula a matriz de correlação entre as variáveis

        # Plota o mapa de calor da matriz de correlação, exibindo os valores numéricos formatados com duas casas decimais
        sns.heatmap(corr, cmap="coolwarm", annot=True, fmt=".2f")

        column_pairs = [
            (
                "mpg",
                "cyl",
            ),  # Par de colunas para análise: milhas por galão vs cilindros
            ("mpg", "disp"),  # milhas por galão vs deslocamento
            ("mpg", "hp"),  # milhas por galão vs potência
            ("mpg", "wt"),  # milhas por galão vs peso
            ("mpg", "drat"),  # milhas por galão vs relação de transmissão
            ("mpg", "vs"),  # milhas por galão vs tipo de motor
        ]
        n_plots = len(column_pairs)  # Número de gráficos a serem criados
        fig, axes = plt.subplots(
            nrows=n_plots, ncols=1, figsize=(6, 4 * n_plots)
        )  # Cria uma figura com subplots

        for i, pair in enumerate(column_pairs):  # Itera sobre cada par de colunas
            x_col, y_col = pair  # Separa os nomes das colunas
            sns.scatterplot(
                x=x_col, y=y_col, data=base, ax=axes[i]
            )  # Plota o gráfico de dispersão para o par
            axes[i].set_title(f"{y_col} vs {x_col}")  # Define o título do gráfico

        plt.tight_layout()  # Ajusta o layout dos gráficos para não sobrepor
        plt.show()  # Exibe todos os gráficos na tela
