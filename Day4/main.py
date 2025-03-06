from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = {}

        # Armazenar a frequência de cada número na grid
        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1

        missing = -1
        repeat = -1

        # Verificar números de 1 até n^2 para encontrar os valores faltantes e repetidos
        for num in range(1, n * n + 1):
            if num not in freq:
                missing = num  # Número não presente na grid
            elif freq[num] == 2:
                repeat = num  # Número aparece duas vezes

        return [repeat, missing]

# Teste de caso
if __name__ == "__main__":
    solution = Solution()
    grid = [[1, 3], [2, 2]]  # Exemplo de grid
    result = solution.findMissingAndRepeatedValues(grid)
    print(result)  # Isso vai imprimir o número repetido e o número faltante
