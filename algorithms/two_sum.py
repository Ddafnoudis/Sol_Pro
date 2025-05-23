import itertools

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        # Check if the sum of two numbers equals the tartget
        for num in itertools.combinations(self.nums, 2):
            if sum(num) == self.target:
                return nums.index(num[0]), nums.index(num[1])

# List of numbers
nums: list = [5, 10, 2, 33]
# Target num
target: int = 7
# Define the solution class
solution = Solution()
# Call the TwoSum method
result = solution.twoSum(nums, target)
# print the result
print(result)

