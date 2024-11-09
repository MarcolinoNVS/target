class Solution:
    def teste(self, nums, target):
        index_map = {}  # para guardar os numeros

        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return [index_map[complement], i]
            index_map[num] = i

        return []  # caso nao encontre par


# Exemplo de uso:
solution = Solution()
nums = input("Digite 4 numeros separado por espaço: ")
nums_list = [int(num) for num in nums.split()]
target = input("digite numero alvo: ")
target = int(target)
result = solution.teste(nums_list, target)
print(result)  # Isso imprimirá [0, 1] no console
