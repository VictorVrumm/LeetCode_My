class Solution(object):
    
    # Função para calcular a soma dos dígitos de um número
    def calculate_digit_sum(self, num):
        digit_sum = 0  # Inicializa a soma dos dígitos como 0
        while num > 0:  # Enquanto o número for maior que 0
            digit_sum += num % 10  # Adiciona o último dígito à soma
            num //= 10  # Remove o último dígito do número
        return digit_sum  # Retorna a soma dos dígitos

    # Função principal para encontrar a maior soma de pares de números com a mesma soma de dígitos
    def maximumSum(self, nums):
        digit_sum_pairs = []  # Lista para armazenar tuplas (soma dos dígitos, número)

        # Armazenando os números com suas somas de dígitos como pares
        for number in nums:
            digit_sum = self.calculate_digit_sum(number)  # Calcula a soma dos dígitos do número
            digit_sum_pairs.append((digit_sum, number))  # Adiciona o par (soma dos dígitos, número) na lista

        # Ordena os pares de acordo com a soma dos dígitos, e em caso de empate, pelo valor do número
        digit_sum_pairs.sort()

        max_pair_sum = -1  # Inicializa o valor máximo da soma do par como -1 (valor de referência)

        # Percorre a lista ordenada para encontrar a maior soma de pares com a mesma soma de dígitos
        for index in range(1, len(digit_sum_pairs)):  # Começa a partir do segundo elemento
            current_digit_sum = digit_sum_pairs[index][0]  # Soma dos dígitos do número atual
            previous_digit_sum = digit_sum_pairs[index - 1][0]  # Soma dos dígitos do número anterior

            # Verifica se dois números consecutivos têm a mesma soma de dígitos
            if current_digit_sum == previous_digit_sum:
                # Calcula a soma dos dois números
                current_sum = (
                    digit_sum_pairs[index][1] + digit_sum_pairs[index - 1][1]
                )
                # Atualiza a maior soma encontrada até agora
                max_pair_sum = max(max_pair_sum, current_sum)

        return max_pair_sum  # Retorna a maior soma encontrada
    
# Criação de uma instância da classe Solution
solution = Solution()

# Chamada do método maximumSum com uma lista de números
result = solution.maximumSum([10, 12, 19, 14])

# Exibição do resultado
print(result)
