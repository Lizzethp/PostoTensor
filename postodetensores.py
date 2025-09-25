# Posto de Tensores 2×2×2

#Este projeto implementa um algoritmo para verificar o posto de tensores 2×2×2 sobre os corpos reais (ℝ) e complexos (ℂ).

#O algoritmo:
# Analisa as fatias do tensor para verificar se são singulares.
# Detecta se existem fatias que são múltiplos escalares.
# Calcula o Hiperdeterminante de Cayley para distinguir casos especiais.
# Retorna um resultado textual indicando o posto do tensor de acordo com as condições do teorema aplicado.

## Primeiro, construímos um tensor a partir do produto tensorial de três fatores.
#Deixamos exemplos de listas nos comentários para calcular seu posto, caso o leitor queira testar os diferentes postos.
#Em seguida, começamos a testar as diferentes etapas: se a lista for nula, caso contrário, verificamos se ela é superdiagonal;
#caso contrário, verificamos se os fatores são singulares; se houver um que não seja,
#verificamos se há um fator não singular e um múltiplo de outro fator; caso contrário, passamos ao cálculo do hiperdeterminante de Cayley e,
# a partir daí, verificamos qual é o posto do tensor introduzido inicialmente.
import numpy as np
def produto_tensorial(a, b, c):
    """
    Producto tensorial a⊗b⊗c.
    Devuelve solo la lista en el orden:
      [a1*b1*c1, a1*b1*c2, a2*b1*c1, a2*b1*c2,
       a1*b2*c1, a1*b2*c2, a2*b2*c1, a2*b2*c2]
    """
    a1, a2 = a
    b1, b2 = b
    c1, c2 = c

    lista = [
        a1*b1*c1, a1*b1*c2, a2*b1*c1, a2*b1*c2,
        a1*b2*c1, a1*b2*c2, a2*b2*c1, a2*b2*c2
    ]
    return lista


# Ejemplo
#a = [2, 1]
#b = [0.5, -1]
#c = [-2, -3]
#t1 = produto_tensorial(a, b, c)
#t2 = produto_tensorial(c, b, a)
#t3 = [1, 0, 0, 1, 1, 1, 0, 1]

#print("T1:", t1)
#print("T2:", t2)
#print("T3:", t3)

#print("Soma:", soma_tensores([t1, t2, t3]))
#Se você quer testar o posto do tensor construído, deixa assim. Se quer testor outro exemplo abaixo, colocar em comment o seguinte print
#lista = produto_tensorial(a, b, c)   
#print("Lista:", lista)


# Lista unidimensional com os 8 números
#Produto tensorial de três fatores, a=[a1, a2], b = [b1, b2], c = [c1, c2]
#a⊗b=[a1b1, a1b2, a2b1, a2b2]⊗c=[a1b1c1, a1b1c2, a2b2c1, a2b1c2, a1b2c1, a1b2c2, a2b2c1, a2b2c2]
# Lista unidimensional com os 8 números
#Hiperdeterminante 0
#lista = [1, 0, 0, 1, 1, 1, 0, 1]
#Superdiagonal
#lista = [0, 0, 0, 1, 1, 0, 0, 0]
#Uma fatia multiplo escalar da outra
lista = [-1, 7, 2, 0, -2, 14, 4, 0]
#Hiperdeterminante de Cayley negativo
#lista = [2, 0, 0, 1, 0, 3, -5, 0]
#Todas as fatias singulares
#lista = [-1, 0, 5, 0, -6, 0, 30, 0]
#Hiperdeterminante de Cayley positivo
#lista = [2, 5, -6, -8, 4, 10, -12, 0]


# Reorganizar a lista para coincidir com a forma desejada: 2x2x2
tensor = np.array([[[lista[0], lista[4]], [lista[1], lista[5]]],
                   [[lista[2], lista[6]], [lista[3], lista[7]]]])
def soma_tensores(tensores):
    return list(np.sum(np.array(tensores, dtype=float), axis=0))
# Mostrar fatias do tensor
def mostrar_fatias(tensor):
    # Fatias frontais (fixo k)
    print("Fatias frontais:")
    fatias_frontais = []
    for k in range(tensor.shape[2]):
        f = tensor[:, :, k]
        fatias_frontais.append(f)
        print(f"Fatia frontal k={k}:")
        print(f)

    # Fatias horizontais (fixo i)
    print("\nFatias horizontais:")
    fatias_horizontais = []
    for i in range(tensor.shape[0]):
        f = tensor[i, :, :]
        fatias_horizontais.append(f)
        print(f"Fatia horizontal i={i}:")
        print(f)

    # Fatias verticais (fixo j)
    print("\nFatias verticais:")
    fatias_verticais = []
    for j in range(tensor.shape[1]):
        f = tensor[:, j, :]
        fatias_verticais.append(f)
        print(f"Fatia vertical j={j}:")
        print(f)

    return fatias_frontais, fatias_horizontais, fatias_verticais


# Passo 1: verifica se a lista é nula
def passo_1(lista):
    return np.all(np.array(lista) == 0)


# Passo 2: verifica se a lista é superdiagonal
def passo_2(lista):
    if lista[0] != 0 and lista[7] != 0 and all(x == 0 for x in lista[1:7]):
        return True
    if lista[1] != 0 and lista[6] != 0 and all(x == 0 for x in [lista[0], lista[2], lista[3], lista[4], lista[5], lista[7]]):
        return True
    if lista[2] != 0 and lista[5] != 0 and all(x == 0 for x in [lista[0], lista[1], lista[3], lista[4], lista[6], lista[7]]):
        return True
    if lista[3] != 0 and lista[4] != 0 and all(x == 0 for x in [lista[0], lista[1], lista[2], lista[5], lista[6], lista[7]]):
        return True
    return False


# Passo 3: verifica se todas as fatias são singulares
def passo_3(lista, mostrar=False):

    # Reconstruir tensor 2x2x2
    tensor = np.array([
        [[lista[0], lista[4]], [lista[1], lista[5]]],
        [[lista[2], lista[6]], [lista[3], lista[7]]]
    ], dtype=float)

    fatias_frontais, fatias_horizontais, fatias_verticais = mostrar_fatias(tensor) if mostrar else (
        [tensor[:, :, k] for k in range(2)],
        [tensor[i, :, :] for i in range(2)],
        [tensor[:, j, :] for j in range(2)]
    )

    # juntar as fatias
    todas_fatias = fatias_frontais + fatias_horizontais + fatias_verticais

    # Verificar singularidad de cada fatia
    for fatia in todas_fatias:
        if abs(np.linalg.det(fatia)) > 1e-12:
            return False
    return True

# Verifica se duas matrizes são múltiplos escalares
def e_multiplo_escalar(matriz1, matriz2):
    if np.all(matriz1 == 0) or np.all(matriz2 == 0):
        return True
    indices = np.argwhere(matriz1 != 0)
    i, j = indices[0]
    ratio = matriz2[i, j] / matriz1[i, j]
    for x in range(matriz1.shape[0]):
        for y in range(matriz1.shape[1]):
            if not np.isclose(matriz2[x, y], ratio * matriz1[x, y]):
                return False
    return True

# Passo 4: verifica se há fatias múltiplos escalares
def passo_4(fatias, mostrar=False):
    
    # Pega apenas fatias não singulares
    fatias_nao_sing = [f for f in fatias if abs(np.linalg.det(f)) > 1e-12]

    if len(fatias_nao_sing) == 2:
        f1, f2 = fatias_nao_sing
        v1, v2 = f1.flatten(), f2.flatten()

        # Escolhe as posições onde v1 não é zero
        idx = np.where(np.abs(v1) > 1e-12)[0]

        if len(idx) == 0:  # se todos eram zeros, não dá pra comparar
            return False

        # Calcula razão usando a primeira posição não nula
        ratio = v2[idx[0]] / v1[idx[0]]

        # Verifica se todas as entradas batem com essa razão
        if np.allclose(v2, ratio * v1):
            if mostrar:
                print(f"As fatias não singulares são múltiplos escalares")
            return True
    return False

# Cálculo do hiperdeterminante de Cayley
def calcular_hipderdeterminante(lista):
    a, b, c, d, e, f, g, h = lista

    delta = (
        a**2 * h**2 + b**2 * g**2 + c**2 * f**2 + d**2 * e**2
        - 2 * (a*b*g*h + a*c*f*h + a*d*e*h
               + b*c*f*g + b*d*e*g + c*d*e*f)
        + 4 * (a*d*f*g + b*c*e*h)
    )
    return delta
# Passo 5: Hiperdeterminante
    delta = calcular_hipderdeterminante(lista)

    # Casos do teorema
    if abs(delta) < 1e-12:  # Δ(T) = 0
        return f"Δ(T) = 0: posto 2"
    else:  # Δ(T) diferente de 0
        if delta > 0 and corpo == "R":
            return f"Δ(T) = {delta} > 0 sobre ℝ (posto 2) ou diferente de 0 sobre ℂ (posto 3)"
        else:
            return f"Δ(T) = {delta} diferente de 0: posto 3"

# Função principal
def verificar_posto(lista, corpo="R", mostrar=False):
    # Reconstruir el tensor desde la lista
    tensor = np.array([
        [[lista[0], lista[4]], [lista[1], lista[5]]],
        [[lista[2], lista[6]], [lista[3], lista[7]]]
    ], dtype=float)
    # Passo 1: nula
    if passo_1(lista):
        return "A lista é nula, tem posto 0"

    # Passo 2: superdiagonal
    if passo_2(lista):
        return "A lista é superdiagonal, tem posto 2"

    # Passo 3: verificar todas as fatias
    fatias_frontais, fatias_horizontais, fatias_verticais = mostrar_fatias(tensor) if mostrar else (
        [tensor[:, :, k] for k in range(2)],
        [tensor[i, :, :] for i in range(2)],
        [tensor[:, j, :] for j in range(2)]
    )

    todas_fatias = fatias_frontais + fatias_horizontais + fatias_verticais

    # Se todas são singulares -> posto 1
    if all(abs(np.linalg.det(f)) < 1e-12 for f in todas_fatias):
        return "A lista é de posto 1, todas as fatias são singulares"
# Passo 4: múltiplos escalares
    if (passo_4(fatias_frontais, mostrar) or
        passo_4(fatias_horizontais, mostrar) or
        passo_4(fatias_verticais, mostrar)):
        return "O tensor é de posto 2 (existe um par de fatias múltiplas escalares)"

    # Passo 5: Hiperdeterminante de Cayley
    posto_R, delta = passo_5(lista, "R")
    posto_C, _ = passo_5(lista, "C")

    if posto_R == 2:
        return f"Δ(T) = {delta} > 0 (ℝ) ou diferente de 0 (ℂ): posto 2"
    else:
        return f"Δ(T) = {delta}: posto 3"
if __name__ == "__main__":
    print(verificar_posto(lista, mostrar=True))
