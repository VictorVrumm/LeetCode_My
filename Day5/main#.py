from typing import List

class Solution:
    # Definindo o método applyOperations, que recebe uma lista de inteiros e retorna uma nova lista
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Criando uma nova lista (new_nums) com o mesmo tamanho de nums, inicializada com zeros
        new_nums = [0] * len(nums)
        
        # Variável para controlar a posição de inserção na lista new_nums
        count = 0
        
        # Índice para percorrer a lista de números
        i = 0

        # Laço de repetição que percorre a lista até o penúltimo elemento
        while i < len(nums) - 1:
            # Verificando se o elemento atual não é zero
            if nums[i] != 0:
                # Verificando se o elemento atual é igual ao próximo
                if nums[i] == nums[i + 1]:
                    # Se forem iguais, multiplicamos o valor por 2 e colocamos em new_nums
                    new_nums[count] = nums[i] * 2
                    
                    # Como os dois elementos foram combinados, pulamos o próximo
                    i += 1  
                else:
                    # Se não forem iguais, apenas copiamos o valor para new_nums
                    new_nums[count] = nums[i]
                
                # Incrementando o índice para a próxima posição disponível em new_nums
                count += 1
            # Incrementando i para passar para o próximo par de elementos
            i += 1
        
        # Verificando se existe um último elemento em nums que não foi processado
        if i < len(nums) and nums[i] != 0:
            # Colocamos o último elemento na posição correta de new_nums
            new_nums[count] = nums[i]

        # Retorna a lista modificada
        return new_nums


# Testando a função
solution = Solution()

# Exemplo de teste com uma lista
test_case = [1,2,2,1,1,0]
result = solution.applyOperations(test_case)

# Imprimindo o resultado para verificar o que a função fez
print(result)  # Esperado: [1, 4, 2, 0, 0, 0]
