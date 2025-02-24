class Solution(object):
    def calculate_digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums):

        digit_sum_pairs = []

        for number in nums:
            digit_sum = self.calculate_digit_sum(number)
            digit_sum_pairs.append((digit_sum, number))

        digit_sum_pairs.sort()

        max_pair_sum = -1

        for index in range(1, len(digit_sum_pairs)):
            current_digit_sum = digit_sum_pairs[index][0]
            previous_digit_sum = digit_sum_pairs[index - 1][0]

            if current_digit_sum == previous_digit_sum:
                current_sum = (
                    digit_sum_pairs[index][1] + digit_sum_pairs[index - 1][1]
                )
                max_pair_sum = max(max_pair_sum, current_sum)

        return max_pair_sum
    
solution = Solution()

result = solution.maximumSum([10,12,19,14])

print(result)
