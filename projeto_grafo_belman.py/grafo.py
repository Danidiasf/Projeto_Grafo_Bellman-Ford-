# Implementação do algoritmo

import pandas as pd
import numpy as np

def bellman_ford(df, source):
    # Inicializa distâncias para todos os nós como infinito
    distances = {node: np.inf for node in df['Source airport ID'].unique()}
    distances[source] = 0

    # Relaxamento de todas as arestas repetidamente
    for _ in range(len(df) - 1):
        for index, row in df.iterrows():
            source_node = row['Source airport ID']
            dest_node = row['Destination airport ID']
            weight = row['Distance']

            if distances[source_node] + weight < distances[dest_node]:
                distances[dest_node] = distances[source_node] + weight

    # Verifica se há ciclos negativos
    for index, row in df.iterrows():
        source_node = row['Source airport ID']
        dest_node = row['Destination airport ID']
        weight = row['Distance']

        if distances[source_node] + weight < distances[dest_node]:
            print("O grafo contém um ciclo negativo")
            return

    return distances