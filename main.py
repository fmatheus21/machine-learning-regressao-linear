from RegressaoLinear import LinearRegression


def print_hi(name):
    print(f"Hi, {name}")

    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    lr = LinearRegression(x, y)
    previsao = lr.previsao(6)
    print(f"Previsão: {previsao}")
    print(f"Coeficiente de Correlação: {lr.coeficiente_correlacao}")
    print(f"Inclinação: {lr.inclinacao}")
    print(f"Interceptação: {lr.interceptacao}")
    print(f"Previsão para x=6: {lr.previsao(6)}")


if __name__ == "__main__":
    print_hi("PyCharm")
