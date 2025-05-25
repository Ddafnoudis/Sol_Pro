class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        
        # Iterate through the list of numbers
        for i in range(len(self.nums)):
            # Calculate the sum of the current number with the next number
            for j in range(i + 1, len(self.nums)):
                # Check if the sum equals the target
                if self.nums[i] + self.nums[j] ==self.target:
                    # Return the indices of the two numbers
                    return [i, j]

# List of numbers
nums: list = [5, 10, 2, 33]
# Target num
target: int = 43

# Define the solution class
solution = Solution()
# Call the TwoSum method
result = solution.twoSum(nums, target)
# print the result
print(result)