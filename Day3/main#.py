class Solution:
    # Função principal que verifica se o número n pode ser representado como uma soma de potências de 3.
    def checkPowersOfThree(self, n: int) -> bool:
        # A função chama um helper recursivo para verificar as potências de 3 que somam n.
        return self._check_powers_of_three_helper(0, n)

    # Função auxiliar recursiva que verifica as potências de 3 a partir de uma potência específica.
    def _check_powers_of_three_helper(self, power: int, n: int) -> bool:
        # Caso base: se n chega a 0, significa que conseguimos decompor n usando potências de 3.
        if n == 0:
            return True

        # Se 3 elevado à potência atual for maior que n, significa que não é possível usar essa potência
        # para representar o número, pois 3^power já excedeu o valor de n.
        if 3**power > n:
            return False

        # Tentamos duas opções:
        # 1. Usamos a potência de 3 (3^power) e subtraímos de n.
        add_power = self._check_powers_of_three_helper(power + 1, n - 3**power)

        # 2. Não usamos a potência de 3 e verificamos se o número restante pode ser representado
        # usando potências maiores de 3.
        skip_power = self._check_powers_of_three_helper(power + 1, n)

        # Retorna True se pelo menos uma das opções for válida:
        # - Ou ao adicionar a potência de 3 à soma.
        # - Ou ao ignorar a potência de 3 e continuar tentando com potências maiores.
        return add_power or skip_power

# Testando a função
sol = Solution()

# Exemplo de teste, onde 12 pode ser representado como 3^1 + 3^0
# 12 = 9 + 3, então a função deve retornar True
print(sol.checkPowersOfThree(12))  # Exemplo de teste
