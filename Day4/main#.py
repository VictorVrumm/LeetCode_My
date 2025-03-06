from typing import List  # Importa a anotação de tipo List do módulo typing

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)  # Define n como o número de linhas/colunas da grid (assumindo uma grid n x n)
        freq = {}  # Dicionário para armazenar a frequência de cada número na grid

        # Armazenar a frequência de cada número na grid
        for row in grid:  # Percorre cada linha da grid
            for num in row:  # Percorre cada número da linha
                freq[num] = freq.get(num, 0) + 1  # Incrementa a frequência do número no dicionário

        missing = -1  # Inicializa a variável missing, que armazenará o número faltante (começa com valor inválido)
        repeat = -1  # Inicializa a variável repeat, que armazenará o número repetido (começa com valor inválido)

        # Verificar números de 1 até n^2 para encontrar os valores faltantes e repetidos
        for num in range(1, n * n + 1):  # Percorre os números de 1 até n^2 (total de elementos na grid)
            if num not in freq:  # Se o número não estiver na grid
                missing = num  # Atribui esse número à variável missing
            elif freq[num] == 2:  # Se o número aparecer duas vezes (ou seja, está repetido)
                repeat = num  # Atribui esse número à variável repeat

        # Retorna uma lista com o número repetido e o número faltante
        return [repeat, missing]

# Teste de caso
if __name__ == "__main__":
    solution = Solution()  # Cria uma instância da classe Solution
    grid = [[1, 3], [2, 2]]  # Exemplo de grid onde 2 está repetido e 4 está faltando
    result = solution.findMissingAndRepeatedValues(grid)  # Chama o método passando a grid
    print(result)  # Imprime o resultado no formato [repetido, faltante]
